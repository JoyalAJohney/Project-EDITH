#!/bin/sh
ollama serve &
sleep 10
curl -X POST -H "Content-Type: application/json" -d '{"name":"llava"}' http://localhost:11434/api/pull
wait
