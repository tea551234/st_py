#!/bin/bash


getToken=$(curl -k -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"moxa"}' https://192.168.225.1/api/v1/login)
TOKEN=$(echo $getToken | jq -r '.data.token')
# echo $TOKEN 
sleep 3
curl -k -X POST -H "Content-Type: application/gzip" -H "Cookie: token=$TOKEN" --data-binary "@/mnt/c/Users/archcyber_C0063/Downloads/export_config.tar.gz" https://192.168.225.1/api/v1/configuration


# COOKIE="token=551nau?xJnHeJBCuXCtD,U-tJPdR6?VrAGEB0!v6mz,t09NGuDHng!dmOh3aTfsciWaFtwuFsovcU8f?8jZ?jAkXHLYXnNwv6x0iqdOI59hJy1ep,A1Q0Jx4dSK4o7i"
# curl -k -X POST -H "Content-Type: application/gzip" -H "Cookie: $COOKIE" --data-binary "@/mnt/c/Users/archcyber_C0063/Downloads/export_config.tar.gz" https://192.168.225.1/api/v1/configuration  