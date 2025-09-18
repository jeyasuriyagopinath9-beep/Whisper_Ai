version: "3.9"
services:
  whisper:
    build: .
    ports:
      - "9000:9000"
    restart: always
