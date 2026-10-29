# wireshark-tooo-tooo

**Category:** Forensics
**Difficulty:** Medium

## What I did

Before opening Wireshark I ran all the usual commands on the file:

```bash
strings *
exiftool
binwalk -e
```

Nothing special came out of them, so I opened the file in Wireshark.

The first thing I did was go through the streams: **Follow → TCP Stream**, **Follow → UDP Stream**, and **Follow → HTTP Stream**.

In the HTTP stream I found a fake flag, and honestly, it held me up for a while. At first I thought "haha, that easy". But it wasn't. When I looked more carefully, it looked like hex, but it wasn't that either.

Then I went through the other pages and saw that there were almost 30 of these in different shapes, so there was no way they were the flag. At first I actually thought the real flag was hiding inside one of them. Then I thought maybe they were hashes and tried to crack them, but that went nowhere too.

So I went back to Wireshark and this time I looked inside **DNS**. Something interesting caught my eye: some pieces that looked like base64. When I put them together, I got the flag.

I also wrote a small script for it. It's not necessary, but it makes it easier.

## Takeaway

- If you find a bunch of similar-looking "flags" in different shapes, they're decoys. Don't waste time cracking them.
- When one protocol is a dead end, look at the others. DNS had what I needed here.
