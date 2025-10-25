#!/usr/bin/env bash
# co robi: Wysyła testowy POST do publicznego backendu (tunel Quick Tunnel)
set -euo pipefail
API_URL="${1:?Podaj URL backendu, np. https://humor-classroom-archived-hereby.trycloudflare.com}"
curl -s -X POST "$API_URL/api/ideas" \
  -H "Content-Type: application/json" \
  -d '{"title":"smoke","content":"test"}' | jq .
