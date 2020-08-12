FROM golang:1.14.5 AS builder
WORKDIR /
COPY main.go .
RUN GOOS=linux go build -o helloworld .

FROM alpine:latest
WORKDIR /
COPY --from=builder /helloworld .
CMD ["./helloworld"]