# Wireshark doo dooo do doo… (picoCTF)

**Platform:** picoCTF (it's now behind a login on CyLab Academy)
**Difficulty:** Medium

## What I did

Like I usually do, before opening Wireshark I tried the usual suspects on the file:

```bash
strings file
exiftool file
binwalk -e file
```

Nothing useful came out of any of them.

So I opened the file in Wireshark. It had a lot of HTTP and TCP packets. The first thing I did was go to the HTTP section, right-click, and choose **Follow → HTTP Stream**.

I just kept scrolling through the streams, and on one of the pages I noticed some text that looked like a flag, but scrambled.

I copied it into CyberChef, applied **ROT13**, and the flag popped out.

## Takeaway

- `strings`, `exiftool` and `binwalk` were a dead end here, so for a pcap, go straight to Wireshark and Follow HTTP Stream.
- If you see flag-looking text that's scrambled, try a simple cipher like ROT13 first.
