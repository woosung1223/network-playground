package main

import (
	"container/list"
	"io"
	"log"
	"net"
	"time"

	pb "4_/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedBidirectionalServer
}

func (s *server) GetServerResponse(stream pb.Bidirectional_GetServerResponseServer) error {
	messages := list.New()

	for {
		msg, err := stream.Recv()
		if err == io.EOF {
			for e := messages.Front(); e != nil; e = e.Next() {
				msg := e.Value.(string)
				if err := stream.Send(&pb.Message{Message: msg}); err != nil {
					log.Fatalf("failed to send message: %v", err)
				}
				log.Printf("Sent message: %s", msg)
				time.Sleep(500 * time.Millisecond)
			}
		}
		if err != nil {
			return err
		}

		log.Printf("Received message: %s", msg.GetMessage())
		messages.PushBack(msg.GetMessage())
	}
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterBidirectionalServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
