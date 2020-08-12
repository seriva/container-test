## About

Simple project to showcase image size and container memory footprint of simple `Hello, world!` applications in:

- Rust
- Go
- C#
- Python
- Java

All projects only contain the necessary code and no additional frameworks/libaries. The docker files are all multi-stage builds and use `Alphine` base images as these are small, secure and generally well maintained.

## Building and running

To build and run the containers you can use the snippets bellow:

```shell
docker build -t rust-hello-world .
docker run -it  rust-hello-world:latest

docker build -t go-hello-world .
docker run -it go-hello-world:latest

docker build -t csharp-hello-world .
docker run -it  csharp-hello-world:latest

docker build -t python-hello-world .
docker run -it python-hello-world:latest

docker build -t java-hello-world .
docker run -it java-hello-world:latest
```

## Results

All these builds and runs where done with where done with `docker-19.03-12-stable` under Windows 10 Proffesional.

Image size was determinded with:

```shell
docker image ls
```

Runtime memory usage was determinded with:

```shell
docker stats
```

### Image size

| Image | Size |
|---|---|
| rust-hello-world | 8.77MB |
| go-hello-world | 7.77MB |
| csharp-hello-world | 87.3MB |
| python-hello-world | 42.7MB |
| java-hello-world | 345MB |

### Container memory usage

| Container | Memory |
|---|---|
| rust-hello-world | 844KiB |
| go-hello-world | 7.164MiB |
| csharp-hello-world | 5.355MiB |
| python-hello-world | 5.062MiB |
| java-hello-world | 11.38MiB |

## Notes

The Alpine base images really help out `C#`, `Java` and `Python` as using the normal ones would increase the size of them 2 to 8 fold. The `Rust` and `Go` images on the other hand could even be made smaller if the `scratch` base image is used.

Memory usage for the simple `Hello, world!` examples does not reflect a real world application scenario as `C#`, `Java` and `Python` would for sure use more overhead as they are interpreted languages abstracted from bare metal. Also frameworks/libraries used like for example `Spring` for `Java` might greatly increase the memory consumption.
