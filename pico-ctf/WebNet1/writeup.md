# WebNet1

**Category:** Forensics
**Difficulty:** Hard

## Overview

Just like the first one (WebNet0), this challenge came with a pcap file and a key. So again I guessed I'd have to use the key to get anything useful out of the capture.

## What I did

I used the same Wireshark settings as before:

- `Preferences → Protocols → TLS → (Pre)-Master-Secret log filename`
- `Preferences → Protocols → TLS → RSA keys list → Edit...`

But this time the flag was **not** in the HTTP stream. Wireshark gave me a fake flag that was obviously not the real one.

So I exported the HTTP objects:

`File → Export Objects → HTTP`

I downloaded all of them, and one of them was an image. This was the part where I had to show my stego skills, so I ran:

`exiftool filename`

And with just this first command, I was able to get the flag.

## Takeaway

Decrypting the traffic was only the first half of the challenge. The HTTP stream had a fake flag, and the real one was hidden in the metadata of an image I could only get by exporting the objects. If a flag looks too easy, keep digging.
