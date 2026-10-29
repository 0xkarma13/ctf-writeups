# shark on wire 1

**Category:** Forensics
**Difficulty:** Medium

## What I did

As always, I started with the usual commands:

```bash
strings
binwalk -e
exiftool
```

Nothing special came out of them, so I opened the file in Wireshark.

First I just scrolled through the capture from top to bottom to see what was going on. It used ARP, UDP, TCP and a few other protocols. I started with **Follow → UDP Stream** and **Follow → TCP Stream**.

In the UDP stream there was a fake flag, which told me the real flag was probably somewhere in the UDP traffic.

So I set the filter to `udp` and went through the packets from top to bottom with the arrow keys, paying attention to how they changed. In some of the packets I noticed the data was spelling out the word `academy`. I grabbed the IP of those packets: `10.0.0.2`.

Then I filtered again:

```
ip.addr==10.0.0.2
```

That's where I saw that each character of the flag is in the data of its own packet. You can get the whole flag by writing down each character and moving to the next packet. I did that first just to be sure, and then I also wrote an exploit script for it to improve my coding.

And I got the flag.

## Funny thing I noticed later

When I was looking at it again, I saw that in **Follow → UDP Stream**, on page 6, you can get the whole flag in one place.

## Takeaway

- A fake flag is a hint about where to look: if it's in the UDP stream, the real one is probably in the UDP traffic too.
- If packets keep spelling out something familiar, find their IP and filter on it.
