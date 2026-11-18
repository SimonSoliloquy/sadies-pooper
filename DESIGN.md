# Sadie's Pooper: design v2

From the interviews on 2026-11-17 and 2026-11-18. This replaces the first draft. Simon approved it and the numbers on 2026-11-18; the first version went live that day. Later rulings are dated where they appear.

## What it is
A silly 2D side-on runner, played 1v1. Ky, a medium black dog, runs ahead pooping brown swirled poop piles. Sadie, with long curly blonde hair, chases after them and scoops them up. The screen scrolls on its own from the living room out to the garden gate in about 2 minutes. It's built for phones held sideways and also plays on a computer. It always plays landscape (Simon, 2026-11-18): on a phone held upright the whole game, menu included, is turned sideways so it starts horizontal; turning the phone straightens it out. On Android it also goes full screen and locks sideways when a game starts. It's one `index.html` deployed on Vercel from GitHub, like Linkshot.

## Feel
- Silly and mild: cute brown swirl poops, stink lines, no splatter.
- Comic-book art (Simon, 2026-11-18: "more comic book style"): heavy ink outlines, hard-edged shadows with halftone dots, a blue rim light on Ky's glossy black fur, a Ben-Day-dot sky, a black panel frame, and sound effects lettered in bursts and speech bubbles (PLOP!, SCOOP!, PFFFT!, BONK!, WOOF!).
- Ky's dash is a **fart boost**, with a honk and a little brown cloud. The cloud is just for looks.
- Sadie's dash is a **hair-whoosh**: her curly hair spins like a propeller.
- Tapping Ky makes Ky bark.

## Modes
- Play Sadie against a computer Ky, or play Ky against a computer Sadie.
- Difficulty: Easy, Normal or Hard.
- 2 players on the same screen: Sadie's controls on the left half, Ky's on the right.
- Online high scores: a best-Sadie table and a best-Ky table on the shared leaderboard Worker. Scores are multiplied by the difficulty: Easy ×0.75, Normal ×1, Hard ×1.5.

## The route
1. Living room, with the rug and the couch.
2. Sadie's shoes by the back door.
3. The pink roses.
4. The vegetable garden.
5. The garden gate: the finish.

## Controls
- **Moving:** slide your thumb left and right on your half of the screen to push ahead or fall back while the screen scrolls. On a keyboard, use left/right keys.
- **Ky's buttons:** Jump, Fart-dash, Poop.
- **Sadie's buttons:** Jump, Hair-whoosh dash. Scooping is automatic: run over a poop.
- **Keyboard:** Sadie uses A/D to move, W to jump and S to dash. Ky uses the arrow keys to move, ↑ to jump, ↓ to poop and Right Shift to fart-dash.
- Bump into toys or flower pots on the ground and you tumble back.
- **Ky always stays in front of Sadie** (Simon, 2026-11-18). She can't get past him: running or whooshing into him stops her at his tail. If he tumbles back into her he pushes her back, and if she has nowhere left to go he gets shoved forward.

## Scoring: "poop tug"
- Every poop Sadie scoops is a point for Sadie. Every poop she misses (it scrolls off behind her) is a point for Ky.
- A poop dropped on a sneaky spot is a big poop worth 3, to whoever wins it. The sneaky spots are Sadie's shoes, the couch, the pink roses and the vegetable garden.
- Most points at the gate wins.

## Power-ups (two each; each works only for its own player)
- **Ky: food scraps** give more poop ammo (+2).
- **Ky: chilli** makes the next poop a giant golden swirl (worth 5).
- **Sadie: leash** snaps onto Ky the moment she picks it up. Ky can't poop for 4 seconds and gets dragged back a little.
- **Sadie: pooper-scooper** gives her a longer reach for a few seconds (6 s).
- **Ky's poop supply:** starts at 3, +1 every 4 seconds, up to 5.

## Art
Drawn by Claude as comic-book-style vector cartoons (SVG shapes inked and shaded in code), with no image model (Simon, 2026-11-18). This spends Claude tokens, not ComfyUI time. Every part of the art is drawn this way: Sadie, Ky, the poop, the props, the house and the garden. Drawing in vector lets the parts animate: legs run, hair whooshes, the fart cloud puffs, ears bounce.

- **Sadie** (from Simon's photos, 2026-11-18): drawn as an adult woman, not childish (Simon, 2026-11-18, changed from a kid). Extremely long, crimped-wavy, golden blonde hair falling past her waist; this is her signature. (The photos are paler, almost platinum; Simon prefers golden in a cartoon.) Freckles, blue eyes, an oversized denim jacket over a striped top, dark navy flared jeans.
- **Ky** (from Simon's photos, 2026-11-18): a lean, medium-sized dog with very dark chocolate-black, short, glossy fur. Huge upright pointy ears are the signature feature. A slim, narrow muzzle, warm amber-brown eyes, and a little grey on the chin. No white chest and no tan markings.

## Sound
- **Music:** a silly loop with a tuba and kazoo feel, made with Google's Lyria through the Gemini API. There's a mute button.
- **Sound effects:** farts, scoops, plops and barks.
