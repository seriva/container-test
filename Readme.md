## About

Simple sample projects to showcase image size and container/k8s deployment memory footprint for the following languages:

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

This will return the following JSON message:

```shell
{
  "messsage": "Hello, world!"
}
```

The docker files are all multi-stage builds and use `Alphine` base images as these are small, secure and generally well maintained.

## Building and running the images/containers locally

To build and run the containers you can use the snippets below from the respective folders:

```shell
#`Hello, world!`
docker build -t container-name .
docker run -it  container-name:latest

#`Hello, world!` rest API
docker build -t container-name .
docker run -p 8080:8080 container-name:latest
```

## Deploying on K8s

For the K8s deployment, only the `Hello, world!` rest API examples where used with preprepared images which can be found here:

- https://hub.docker.com/repository/docker/luukvv/rust-hello-world-api
- https://hub.docker.com/repository/docker/luukvv/go-hello-world-api
- https://hub.docker.com/repository/docker/luukvv/csharp-hello-world-api
- https://hub.docker.com/repository/docker/luukvv/python-hello-world-api
- https://hub.docker.com/repository/docker/luukvv/java-hello-world-api

To deploy them you can use the `deploy.yml` files below from the respective folders:

```shell
kubectl apply -f build -t deploy.yml
```

This will create a simple Deployment with 3 replicas and a nodeport to run the requests against.

## How results where gathered

### Locally

All local builds and runs where done with where done with `docker-19.03-12-stable` under Windows 10 Professional.

Image size was determinded with:

```shell
docker image ls
```

Container runtime memory usage was determinded with:

```shell
docker stats
```

### K8s deployment

K8s deployment runtime memory usage was determinded by aggregating memory usage for each pod. The memory usage per pod was measured with the [K8s metric server](https://github.com/kubernetes-sigs/metrics-server).

### Request simulation

The requests against the `Hello, world!` rest API examples where executed with the `HelloWorldApi/apitest.py` python script.

# Results

### `Hello, world!` locally

Memory was measured after the `Hello, world!` message waiting for key input.

| Image | Size | Memory |
|---|---|---|
| rust-hello-world | 8.77MB | 844KiB |
| go-hello-world | 7.77MB | 7.164MiB |
| csharp-hello-world | 87.3MB | 5.355MiB |
| python-hello-world | 42.7MB | 5.062MiB |
| java-hello-world | 345MB | 11.38MiB |

### `Hello, world!` rest API locally

Memory was measured after running a 1000 requests against the API`s.

| Image | Size | Memory |
|---|---|---|
| rust-hello-world-api | 10.9MB | 904KiB |
| go-hello-world-api | 13MB | 7.195MiB |
| csharp-hello-world-api | 105MB | 28.86MiB |
| python-hello-world-api | 46.3MB | 34.7MiB |
| java-hello-world-api | 361MB | 116MiB |

### `Hello, world!` K8s deployment

Memory was measured after running a 10000 requests against the API`s through a nodeport

| Image | Size | Memory usage for 3 pods |
|---|---|---|
| rust-hello-world-api | 10.9MB | 3MiB |
| go-hello-world-api | 13MB | 21MiB |
| csharp-hello-world-api | 105MB | 96MiB |
| python-hello-world-api | 46.3MB | 73MiB |
| java-hello-world-api | 361MB | 363MiB |

## Notes

The Alpine base images really help out `C#`, `Java` and `Python` as using the normal ones would increase the size of them 2 to 8 fold. The `Rust` and `Go` images on the other hand could even be made smaller if the `scratch` base image is used.
