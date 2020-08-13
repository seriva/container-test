## About

Simple sample projects to showcase image size and container memory footprint for the following languages:

- Rust
- Go
- C#
- Python
- Java

### `Hello, world!`

Simple `Hello, world!` examples only containing the necessary code and no additional frameworks/libaries. Only prints `Hello, world!` message and waits for key input to stop. The docker files are all multi-stage builds and use `Alphine` base images as these are small, secure and generally well maintained.

### `Hello, world!` rest API

Simple `Hello, world!` REST Api examples using popular libraries for the language:

- Rust -> warp
- Go -> net/http
- C# -> AspNetCore
- Python -> flask
- Java -> spring

All examples expose a simple API which can be reached here:

`http://127.0.0.1:8080/hello`

Which will return the following JSON message:

```shell
{
  "messsage": "Hello, world!"
}
```

The docker files are all multi-stage builds and use `Alphine` base images as these are small, secure and generally well maintained.

## Building and running

To build and run the containers you can use the snippets below from the respective folders:

```shell
#`Hello, world!`
docker build -t container-name .
docker run -it  container-name:latest

#`Hello, world!` rest API
docker build -t container-name .
docker run -p 8080:8080 container-name:latest
```

## Results

All these builds and runs where done with where done with `docker-19.03-12-stable` under Windows 10 Professional.

Image size was determinded with:

```shell
docker image ls
```

Runtime memory usage was determinded with:

```shell
docker stats
```

### Image size and container memory ussage `Hello, world!`

Memory was measured after the `Hello, world!` message waiting for key input.

| Image | Size | Memory |
|---|---|---|
| rust-hello-world | 8.77MB | 844KiB |
| go-hello-world | 7.77MB | 7.164MiB |
| csharp-hello-world | 87.3MB | 5.355MiB |
| python-hello-world | 42.7MB | 5.062MiB |
| java-hello-world | 345MB | 11.38MiB |

### Image size and container memory ussage `Hello, world!` rest API

Memory was measured after running a 1000 requests against the API`s.

| Image | Size | Memory |
|---|---|---|
| rust-hello-world-api | 10.9MB | 904KiB |
| go-hello-world-api | 13MB | 7.195MiB |
| csharp-hello-world-api | 105MB | 28.86MiB |
| python-hello-world-api | 46.3MB | 34.7MiB |
| java-hello-world-api | 361MB | 116MiB |

## Notes

The Alpine base images really help out `C#`, `Java` and `Python` as using the normal ones would increase the size of them 2 to 8 fold. The `Rust` and `Go` images on the other hand could even be made smaller if the `scratch` base image is used.
