# Jarrotv2 Story — 50s NFT Sniper Video

A 50-second story video about **Jarrotv2**, a Discord-native NFT sniper bot — built entirely with [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML → MP4), edge-tts voice-over, and an ambient synth score. No stock footage, no external assets beyond fonts: every scene is HTML/CSS/GSAP rendered deterministically.

![preview](jarrotv2_story.mp4)

## The story (6 scenes, all facts from real drop battles)

| Scene | Time | Content |
|---|---|---|
| 1 | 0–6s | **The problem** — every NFT drop comes down to seconds |
| 2 | 6–13s | **Meet Jarrotv2** — Discord chat mockup with a real SNIPE ARMED card (MINT SUKSES, 1437ms T-0) |
| 3 | 13–21s | **Execution engine** — race-to-every-RPC, pre-sign T-30, 1-RPC T-0 broadcast. Metrics: 22.5s→4.5s cold→hot, 16s→1.5s eligibility |
| 4 | 21–32s | **Phase intelligence** — allocation check (`minterQuantityMinted`, not the lying `isEligible` flag), pre-sign T-30, blind broadcast |
| 5 | 32–44s | **Battle-tested** — 12-point smoke gate, retry classifier tested against real API error strings, 6 chains |
| 6 | 44–50s | **CTA** — "Built for the drop. Proven on-chain." |

## Reproduce

```bash
# 1. Clone + install
git clone https://github.com/Mlnglh889/jarrotv2-story.git
cd jarrotv2-story
npm install   # hyperframes CLI deps

# 2. Generate the voice-over (edge-tts, free, ~13s)
pip install edge-tts
python generate_vo.py   # → vo/s1.mp3 … s6.mp3

# 3. Build audio tracks
#    - vo_track.m4a: all VO segments delayed to scene starts, mixed
#    - music_track.m4a: ambient synth drone (ffmpeg sine layers + lowpass)
ffmpeg -y -i vo/s1.mp3 -i vo/s2.mp3 -i vo/s3.mp3 -i vo/s4.mp3 -i vo/s5.mp3 -i vo/s6.mp3 \
  -filter_complex "[0:a]adelay=400:all=1[a0];[1:a]adelay=6800:all=1[a1];[2:a]adelay=13200:all=1[a2];[3:a]adelay=21500:all=1[a3];[4:a]adelay=33000:all=1[a4];[5:a]adelay=44300:all=1[a5];[a0][a1][a2][a3][a4][a5]amix=inputs=6:normalize=0,apad=whole_dur=49.9[out]" \
  -map "[out]" -c:a aac vo_track.m4a

# 4. Render video (HTML → MP4, deterministic)
npm run check     # lint: contrast, timing, structure
npm run render    # → renders/*.mp4

# 5. Mux audio into video
ffmpeg -y -i renders/<your-render>.mp4 -i vo_track.m4a -i music_track.m4a \
  -filter_complex "[2:a]volume=0.5[m];[1:a][m]amix=inputs=2:normalize=0[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -shortest jarrotv2_story.mp4
```

## Technical notes

- **Rendering**: HyperFrames 0.8.163 — screenshot capture, software GL on a 2-core VPS, 49.9s video rendered in ~1m 24s
- **Voice-over**: edge-tts 7.3.1, `en-US-ChristopherNeural`, rate +8%
- **Timing discipline**: each scene duration = its VO duration + 0.55s breathing room, so narration never clips
- **Design**: Discord-native brand (blurple #5865F2), Space Grotesk + JetBrains Mono, solid opaque panels (no see-through glass), all text passes 4.5:1 contrast
- **Zero LLM in the render path** — HTML is the single source of truth; the same file always produces the same video

## Facts behind the scenes

Every number on screen is from real production battles:
- **1437ms T-0** — GLRTCH Genesis merkle mint, broadcast to confirmed
- **22.5s → 4.5s** — nine-fix latency batch (fee clamp EIP-1559, JWT warm-all, keep-alive undici)
- **Allocation check** — Founding Farmers post-mortem: `isEligible: true` while allocation was spent; now `minterQuantityMinted` gates the phase plan
- **12-point smoke gate** — D'Uniformed post-mortem: 4 T-0 bugs that a scripted check would have caught

## License

MIT
