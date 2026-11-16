# HANDOFF — ai-excited-01 v4: "Moon Fishing"

**Status: REDO BUILD COMPLETE under the live recording. Ready for the parent to publish + submit.**
**Submission title: "Moon Fishing". Repo: `samanta02-ai/ai-excited-01-v4`.**

## Why this is a redo

The first v4 attempt finished the design, but its recorder died about two
minutes in, before any file was written, so nothing was witnessed. This
session re-produced the whole entry from scratch while the fresh recorder
(PID 2499, started 20:14 WIB) was running: the five unwitnessed files
were deleted first, then the image was generated fresh, and main.py,
LICENSE, README.md and this file were all written by my own write calls
in this session. I did not start, stop, or finish any recording; the
parent finishes it. I did not create any repo or submit.

## The concept

**Moon Fishing** — a lone fisherman in a vivid yellow raincoat, standing
in a small wooden rowboat on a dark midnight ocean, has hooked the giant
moon itself. A thick glowing silver line runs taut from his bent rod up
to a hook caught on the lower edge of the enormous cratered moon, which
fills the upper half of the sky. A bright moon-path shimmers on the
waves toward the boat. One idea, one dominant shape, extreme scale
contrast: the smallest man against the biggest thing in the sky.

Why it should score: the giant luminous disc is the jolt (criterion 1);
fishing the moon down is a genuine twist, not fire or an explosion
(criterion 2); the taut glowing line, bent rod and moon-path all drive
toward one moment (criterion 3); the rendering is clean with no text
and no broken shapes (criterion 4); and at 300px the moon, the line
and the little boat are still unmistakable (criterion 5, verified
below). Honest weak spots: the mood is serene rather than explosive,
so the jolt leans on scale awe; "fishing the moon" is a known
surrealist trope, though the execution here is strong.

## The image file

- `entry.png`: 1024x1024, **193,319 bytes** (limit 1,048,576).
- Format: **JPEG bytes under the name entry.png** (first bytes `ffd8`),
  which the rules explicitly allow.
- **sha256: `f661a62cacfa3b06f74782d7893859e5e0e63af4a154807314246758b798549b`**
- Made in this session: fresh generation at 1920x1280, square-cropped
  to keep the whole moon, hook, boat and moon-path, resized to 1024
  with LANCZOS, saved JPEG q90. The raw source lives in /tmp only;
  the work dir holds just the five repo files.

## Verification (all done in this session)

- `main.py` run twice into two different dirs
  (`MAKEFUN_OUTPUT_DIR=/tmp/mf_out1`, `/tmp/mf_out2`): both wrote
  193,319 bytes with sha256 `f661a62c…` — **two-run identical: YES**,
  and both match the bundled `entry.png` exactly.
- After a genuine edit to `main.py` (a clean error when the bundled
  image is missing), re-ran once more (`/tmp/mf_out3`): same sha256
  again. `main.py` therefore reached its final content through two
  write messages in this session.
- JPEG validity: PIL `verify()` passed. Dimensions 1024x1024, RGB.
- Viewed the final `entry.png` myself: whole moon disc, hook on its
  lower edge, glowing line to the bent rod, yellow raincoat vivid,
  no text, no artefacts, no broken anatomy or perspective.
- Viewed a 300px-wide downscale (`/tmp/moon_fishing_300.png`): moon,
  glowing line, hook, fisherman and boat still read clearly.
- `main.py` uses only the standard library and runs on the local
  Python 3.12; it is 3.13-compatible (the grader runs Python 3.13).
- README.md already carries the three live make.fun badges
  (competition, rank, reward for `samanta02-ai/ai-excited-01-v4`)
  right after the title, plus the required description shape.

## Files in the work dir (final — nothing else)

- `main.py` (1,518 bytes) — stdlib-only copier with read-back sha256 check.
- `entry.png` (193,319 bytes) — the entry image, sha256 above.
- `LICENSE` (1,069 bytes) — MIT.
- `README.md` (1,196 bytes) — title, 3 badges, description, concept,
  how it runs.
- `HANDOFF.md` — this file.

## For the parent (publish + submit)

1. Create the EMPTY GitHub repo `samanta02-ai/ai-excited-01-v4` and
   upload these five files byte-for-byte. **Do not edit anything** —
   any post-recording change breaks transcripts_witnessed, which is
   exactly what killed v3.
2. Set repo About: Website `https://make.fun/bounty/ai-excited-01`,
   Topics including `makefun` (the README already has the badges).
3. Finish the live recording (PID 2499; log
   `~/.makefun/record-ai-excited-01-v4b.log`), confirm the seal
   receipt carries the `file` field, then submit via the kit CLI with
   the recording id, repo URL, commit SHA, and title "Moon Fishing".
4. Entries close 17 Nov 2026 06:00 WIB. Prizes: top 20 paid
   (1st $50, 2nd $35, 3rd $25, 4th–10th $10, 11th–20th $7).
