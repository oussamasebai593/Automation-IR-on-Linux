#!/bin/bash

IP=$1

if [ -z "$IP" ]; then
  echo "Usage: $0 <IP>"
  exit 1
fi

sudo iptables -A INPUT -s $IP -j DROP
echo "[+] IP $IP blocked"
