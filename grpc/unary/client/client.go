// client.go
package main

import (
	"context"
	"log"
	"time"

	pb "1_/proto"

	"google.golang.org/grpc"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewMyServiceClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	r, err := c.MyFunction(ctx, &pb.MyNumber{Value: 10})
	log.Printf("gRPC result: %v", r.Value)
	if err != nil {
		log.Fatalf("could not call MyFunction: %v", err)
	}
}
