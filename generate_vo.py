import asyncio, edge_tts
scenes = [
    ("s1", "Every NFT drop comes down to seconds. Humans are simply too slow."),
    ("s2", "Meet Jarrot v two. A Discord native NFT sniper that never sleeps."),
    ("s3", "It race broadcasts to every R P C. Pre signed at T minus thirty. Blind broadcast at T zero."),
    ("s4", "Phase intelligence. G T D. First come first served. Public. Allocation checks mean no wasted attempts."),
    ("s5", "From twenty two seconds cold, down to four to five seconds hot. Eligibility in one to two seconds. And a twelve point smoke test before every deploy."),
    ("s6", "Jarrot v two. Built for the drop. Proven on chain."),
]
async def gen():
    for k, t in scenes:
        c = edge_tts.Communicate(t, "en-US-ChristopherNeural", rate="+8%")
        await c.save(f"/tmp/my-video/vo/{k}.mp3")
        print(k, "done")
asyncio.run(gen())
