FROM rust:latest as builder
WORKDIR /usr/src/helloworld
RUN rustup target add x86_64-unknown-linux-musl
COPY . .
RUN cargo install --target x86_64-unknown-linux-musl --path .

FROM alpine:latest
COPY --from=builder /usr/local/cargo/bin/helloworld /usr/local/bin/helloworld

CMD ["/usr/local/bin/helloworld"]