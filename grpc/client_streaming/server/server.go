package main

import (
	"io"
	"log"
	"net"

	pb "3_/proto"

	"google.golang.org/grpc"
)

type server struct {
	pb.UnimplementedClientStreamingServer
}

func (s *server) GetServerResponse(stream pb.ClientStreaming_GetServerResponseServer) error {
	var messageCount int32
	for {
		msg, err := stream.Recv()
		if err == io.EOF {
			return stream.SendAndClose(&pb.Number{Value: messageCount})
		}
		if err != nil {
			return err
		}
		log.Printf("Received message: %s", msg.GetMessage())
		messageCount++
	}
}

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterClientStreamingServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
