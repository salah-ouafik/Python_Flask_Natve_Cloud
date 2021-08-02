FROM golang:alpine

LABEL maintainer="OUAFIK Salaheddine"

COPY . /go/src/app

WORKDIR /go/src/app

RUN go build -o helloworld main.go

EXPOSE 6111

CMD ["./helloworld"]

