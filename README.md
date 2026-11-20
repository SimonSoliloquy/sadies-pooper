# Sadie's Pooper

A silly 1v1 side-on runner. Ky the dog poops brown swirls in sneaky spots; Sadie chases after them with a bag, from the living room out to the garden gate. Play Sadie or Ky against the computer (Easy, Normal, Hard), or two players on one screen. Play at https://simonsoliloquy.com/sadies-pooper/ (the old https://sadies-pooper.vercel.app forwards there until about 2026-12-19).

- `index.html`: the whole game (plain canvas 2D, no libraries, no build step). All the art is drawn in code.
- `DESIGN.md`: the agreed design.
- `art/svg/`: the approved character drawings the in-game art is traced from (`preview.html` shows them together).
- `tools/make_music.py`: makes the music loop with Google's Lyria (Gemini API) into `music/loop.mp3`. Until that file exists the game plays a tuba-and-kazoo loop made in code.

High scores go to the shared leaderboard Worker (`leaderboards.ai-wizards.workers.dev`, boards `sadies-pooper-sadie` and `sadies-pooper-ky`), all time only: the game asks each board once per page load, and a save is one request whose answer carries the updated list.

Publishing: Cloudflare serves plain files (no Worker code) at `simonsoliloquy.com/sadies-pooper/`. On every push to `main`, Cloudflare's GitHub build runs `tools/cf-build.sh` (copies what the game loads into `.cf/sadies-pooper/`) and then `npx wrangler deploy` (settings in `wrangler.jsonc`). By hand: `sh tools/cf-build.sh && npx wrangler@4.40.0 deploy`. `vercel.json` now only forwards the old Vercel address and goes in about a month.
