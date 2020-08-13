FROM golang:1.14.5 AS builder
WORKDIR /
COPY main.go .
RUN GOOS=linux CGO_ENABLED=0 go build -o helloworld .

FROM alpine:latest
WORKDIR /
COPY --from=builder /helloworld .
ENTRYPOINT ["/helloworld"]
EXPOSE 8080
