#!/usr/bin/env bash
# co robi: wysyła testowego POST do publicznego backendu (tunel)
set -euo pipefail
API_URL="${1:?Podaj URL backendu, np. https://api-kroniki.moja-domena}"
curl -s -X POST "$API_URL/api/ideas" \
  -H "Content-Type: application/json" \
  -d '{"title":"smoke","content":"test"}' | jq .
