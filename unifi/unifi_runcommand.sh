#!/bin/bash 

docker run -d \
    --name rrp-unifi \
    --restart=unless-stopped \
    -p 8080:8080 -p 8443:8443 \
    -v unifi_data:/usr/lib/unifi/data  \
    -v unifi_data:/usr/lib/unifi/logs \
    -v unifi_data:/var/log/supervisor \
    goofball222/unifi:latest
