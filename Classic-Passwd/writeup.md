# TryHackMe: Classic Passwd (Medium)

Short write-up. I solved this one in under 2 minutes, but it's rated medium, so I figured it was still worth writing down.

## What I did

As soon as I got the file, I ran `file` on it to see if I can even run it. It's an ELF.

Then I ran `strings` to see what I could find, and I found something really interesting:

```
THM{%d%d}
```

That's not the flag, it's a format string. The moment I saw it, I understood what was going on: the `%d`s are placeholders for numbers, so the program builds the flag out of two numbers, and those numbers are most likely somewhere inside the code.

I opened the file in IDA and went to `main`. I knew what I was looking for: that `THM` string. It wasn't in `main`, so I looked at another function, and yes, it was there. The two `%d`s were two numbers. I put them in place of the `%d`s and got the flag.

## Takeaway

- `strings` can tell you a lot, even before you open a disassembler. A `%d` inside a flag format means the flag is built from numbers that live in the code.
- If the thing you're looking for isn't in `main`, check the other functions.
