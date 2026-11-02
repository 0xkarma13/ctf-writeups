# Trivial Flag Transfer Protocol

**Category:** Forensics | **Difficulty:** Medium
**Given file:** a `.pcap`

## My approach

First I tried the usual command-line tools on the file:

```bash
strings file
exiftool file
binwalk -e file
```

None of them gave me anything useful.

## Opening the pcap in Wireshark

As soon as I opened the pcap, I saw a lot of TFTP packets, so right away I figured the flag was most likely hidden somewhere in this protocol.

A quick note on TFTP: it's an old protocol (I'd say it's pretty outdated by now) used for transferring files. It runs over UDP port 69, and people still use it on small networks because it's so simple and hassle-free.

### Where I wasted time

I spent almost 20 minutes looking around. First I scrolled through everything from top to bottom. I could see some images being moved around, but I didn't realize it was TFTP and not HTTP, so I kept using Export Objects → HTTP and it showed nothing.

In the end I looked at more of the data to check whether they might have sent the flag word by word, but that wasn't it either. Then it suddenly hit me: these are TFTP transfers. So I went to:

`File → Export Objects → TFTP`

and downloaded everything:

- `instructions.txt`
- `picture1.bmp`
- `picture2.bmp`
- `picture3.bmp`
- `plan`
- `program.deb`

## Going through the files

### picture1.bmp (a dead end)

When I checked `picture1.bmp`, I noticed that one pixel was black, and that made me suspicious.

I have to be honest, I got a bit confused here. I found the pixel's coordinates in GIMP: `311, 221`. But when I ran it in my script, it didn't come out right. The pixel is completely black, so all its values should be 0, but they weren't.

### instructions.txt

I found this string in `instructions.txt`:

```
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

If you ROT13 it, you get a simple readable text:

```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```

It basically says TFTP isn't secure, so we have to hide the flag somewhere. So now it was clear the flag is hidden.

### plan

The plan is the other file. Inside it there's this:

```
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```

With ROT13 it becomes:

```
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

It tells me to go look at the photos, and it also mentions `DUEDILIGENCE`, which looked like it could be the password.

## Finding the flag

So I ran `steghide` on all the images, and in the end I found the flag in the **third** picture.

The first picture was just a distraction. I'd say it was a false positive.

## Flag

```
academy{h1dd3n_1n_pLa1n_51GHT_18375919}
```
