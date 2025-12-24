#!/bin/bash

SERVICE=$1

if [ -z "$SERVICE" ]; then
  echo "Usage: $0 <service>"
  exit 1
fi

sudo systemctl stop $SERVICE
echo "[+] Service $SERVICE stopped"
