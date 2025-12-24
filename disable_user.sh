#!/bin/bash

USER=$1

if [ -z "$USER" ]; then
  echo "Usage: $0 <username>"
  exit 1
fi

sudo usermod -L $USER
echo "[+] User $USER disabled"
