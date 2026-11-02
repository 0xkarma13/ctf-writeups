# WebNet0

**Category:** Forensics
**Difficulty:** Hard

## Overview

Along with the capture file I downloaded, the challenge also gave me a key file. I figured I'd have to use that key to be able to see the data, because I had already solved a challenge like this before.

## What I did

It turned out the way I expected, but honestly I got stuck for about 20–30 minutes. The reason: I had only loaded the key in one place in Wireshark:

`Preferences → Protocols → TLS → (Pre)-Master-Secret log filename`

That wasn't enough on its own. I also had to add it here:

`Preferences → Protocols → TLS → RSA keys list → Edit...`

Once I did that, I could finally see the data that was encrypted before, and Wireshark showed me several HTTP packets. I found the flag inside them.

## Flag

`academy{nongshim.shrimp.crackers}`

## Takeaway

If a challenge gives you a pcap and a key together, the key is probably there to decrypt the TLS traffic in Wireshark. Check that it's set in **all** the places it needs to be, not just one. That mistake cost me about half an hour.
