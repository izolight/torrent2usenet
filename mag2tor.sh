#!/bin/bash
[[ "$1" =~ xt=urn:btih:([^&/]+) ]] || exit;
echo "d10:magnet-uri${#1}:${1}e" > "/home/***REMOVED***/.watch/meta-${BASH_REMATCH[1]}.torrent"
