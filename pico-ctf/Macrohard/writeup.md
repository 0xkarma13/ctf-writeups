# MacroHard WeakEdge (picoCTF)

**Platform:** picoCTF
**Category:** Forensics
**Difficulty:** Medium

## What I did

I'll be honest: at first I thought this was a pcap file. Then I looked closer and saw it's actually a `.pptm`, which is a PowerPoint file.

Out of habit I still ran the usual commands on it:

```bash
strings *
exiftool *
binwalk -e *
```

`binwalk` was the only one that gave me output, so it had clearly extracted something. I went inside and found several folders, and I checked them one by one. One of them was named `hidden`, which made it obvious there was something in there.

Inside was a string of base64. I decoded it and got the flag.

## Takeaway

- A `.pptm` (like `.docx` and `.xlsx`) is basically a zip archive, which is why `binwalk -e` was able to unpack it.
- When a folder is literally called `hidden`, look in it first.
