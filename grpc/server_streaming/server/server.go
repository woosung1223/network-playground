package main

import (
	"container/list"
	"log"
	"net"
	"time"

	pb "2_/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedServerStreamingServer
}

func (s *server) GetServerResponse(req *pb.Number, stream pb.ServerStreaming_GetServerResponseServer) error {
	messages := list.New()
	messages.PushBack("message #1")
	messages.PushBack("message #2")
	messages.PushBack("message #3")
	messages.PushBack("message #4")
	messages.PushBack("message #5")

	log.Printf("Server processing gRPC server-streaming %v.", req.Value)

	for e := messages.Front(); e != nil; e = e.Next() {
		res := &pb.Message{Message: e.Value.(string)}
		if err := stream.Send(res); err != nil {
			return err
		}
		time.Sleep(time.Millisecond * 500)
	}
	return nil
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterServerStreamingServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
