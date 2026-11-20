#!/bin/sh
# Build the folder Cloudflare serves at https://simonsoliloquy.com/sadies-pooper/ (see wrangler.jsonc).
# Cloudflare's GitHub build runs this and then `npx wrangler deploy` on every push to main.
# By hand: sh tools/cf-build.sh && npx wrangler@4.40.0 deploy
#
# The live game is index.html alone: all the art is drawn in code (art/svg/ is only the source it was
# traced from). It plays music/loop.mp3 when that file exists, else a loop made in code, so the mp3 is
# copied only if it is there.
set -e
cd "$(dirname "$0")/.."
rm -rf .cf && mkdir -p .cf/sadies-pooper
cp index.html .cf/sadies-pooper/
if [ -f music/loop.mp3 ]; then
  mkdir -p .cf/sadies-pooper/music
  cp music/loop.mp3 .cf/sadies-pooper/music/
fi
