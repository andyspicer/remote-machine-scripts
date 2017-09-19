#! /bin/bash

docker pull sematext/sematext-agent-docker
docker run -d --name sematext-agent --restart=always \
  -e LOGSENE_TOKEN=63d04666-5151-443b-84db-5ded5533ff7f \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /etc/localtime:/etc/localtime:ro \
  sematext/sematext-agent-docker
