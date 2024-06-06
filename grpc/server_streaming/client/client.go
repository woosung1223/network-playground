package main

import (
	"context"
	"log"
	"time"

	pb "2_/proto"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewServerStreamingClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)

	defer cancel()

	stream, err := c.GetServerResponse(ctx, &pb.Number{Value: 5})

	for {
		res, err := stream.Recv()
		if err != nil {
			log.Fatalf("failed to receive: %v", err)
		}
		log.Printf("Received: %v", res.GetMessage())
	}
}
