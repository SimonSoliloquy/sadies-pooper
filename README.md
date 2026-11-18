# Sadie's Pooper

A silly 1v1 side-on runner. Ky the dog poops brown swirls in sneaky spots; Sadie chases after them with a bag, from the living room out to the garden gate. Play Sadie or Ky against the computer (Easy, Normal, Hard), or two players on one screen. Play at https://sadies-pooper.vercel.app.

- `index.html`: the whole game (plain canvas 2D, no libraries, no build step). All the art is drawn in code.
- `DESIGN.md`: the agreed design.
- `art/svg/`: the approved character drawings the in-game art is traced from (`preview.html` shows them together).
- `tools/make_music.py`: makes the music loop with Google's Lyria (Gemini API) into `music/loop.mp3`. Until that file exists the game plays a tuba-and-kazoo loop made in code.

High scores go to the shared leaderboard Worker (`leaderboards.ai-wizards.workers.dev`, boards `sadies-pooper-sadie` and `sadies-pooper-ky`). Pushing to `main` deploys to production on Vercel (project `sadies-pooper`).
