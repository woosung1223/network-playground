package main

import (
	"container/list"
	"context"
	"log"
	"time"

	pb "3_/proto"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewClientStreamingClient(conn)

	stream, err := c.GetServerResponse(context.Background())
	if err != nil {
		log.Fatalf("could not get server response: %v", err)
	}

	messages := list.New()
	messages.PushBack("message #1")
	messages.PushBack("message #2")
	messages.PushBack("message #3")
	messages.PushBack("message #4")
	messages.PushBack("message #5")

	for e := messages.Front(); e != nil; e = e.Next() {
		msg := e.Value.(string)
		if err := stream.Send(&pb.Message{Message: msg}); err != nil {
			log.Fatalf("failed to send message: %v", err)
		}
		log.Printf("Sent message: %s", msg)
		time.Sleep(500 * time.Millisecond)
	}

	res, err := stream.CloseAndRecv()
	if err != nil {
		log.Fatalf("failed to receive response: %v", err)
	}
	log.Printf("Response from server: %d messages received", res.GetValue())
}
