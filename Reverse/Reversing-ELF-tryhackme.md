# TryHackMe: Reversing ELF — My Write-up

Room: https://tryhackme.com/room/reverselfiles

**Tools I used:** `chmod`, `strings`, `ltrace`, `strace`, IDA, CyberChef

The room has 8 crackmes. Here's how I went through each one.

---

## Crackme 1

This one was simple, I just had to run it.

```bash
chmod +x crackme1
./crackme1
```

## Crackme 2

When I ran it, it said it needs a password. I found the password with `strings`.

```bash
./crackme2 <password>
```

## Crackme 3

Same thing, it asked for a password. I used the same method as above, but this time the password was encrypted with base64, so I decoded it with CyberChef.

## Crackme 4

Honestly, this one was a bit harder than I expected. I thought it would be easier.

The hint was `strcpy`, which means we need to look at the assembly, because we don't have the C code at all. So we have to reverse it with IDA.

I opened it in IDA and tried to understand the logic. The first thing I saw was: if something happens, it's correct, and if not, it's wrong. As soon as I saw that, without looking at the rest of the code, I went to the assembly and flipped the jump:

```
jz ==> jnz
```

I thought it should work now, so I entered a wrong password and it said it's correct. But there was no flag anywhere. I just wanted it to tell me "correct", but when I went to see where the flag gets printed, I found out it doesn't print a flag at all. So I had to actually understand the code.

After a lot of research on what the code was doing and understanding its structure, I found that it has two strings made of hex values. One thing I didn't get at first was that they end with `LL`. I knew the concept, but I didn't know how it shows up in code. It's the `long long` concept: if you want to fit a big value in one variable and use more memory, you use this. I had even written this in my own C practice code.

This is why I say: the more challenges you look at and solve, and the more you work with whatever is in front of you, the better you get.

Then, in one of the functions, I saw that those two numbers are used, so I had to see what that function does. Inside it, the number you give it gets XORed with 24.

Another thing: those strings are little-endian. What does that mean? In simple words, you reverse the bytes (swap them).

For example, this was the first string:

```
7B 17 56 14 49 7B 5D 49
```

Because `strcmp` and `get_pwd` read the string from the lower address to the higher one, the first byte of the string is `49`, not `7B`. So before the XOR, I have to reverse the bytes of each number:

```
49 5D 7B 49 14 56 17 7B
```

In CyberChef:

1. From Hex
2. Swap endianness
3. XOR with 24 (hex)

And the flag comes out.

## Crackme 5

First I check all the possible commands:

```
strings
ltrace
strace
```

and then I go into IDA. When I opened the C-code (pseudocode) view, I saw this:

![crackme5 pseudocode](images/crackme5-pseudocode.png)

By the way, this screenshot is from after I reversed the condition. Like last time, I flipped the condition in the assembly to see what would happen.

But when I looked closer, it says: if the user's input is equal to this string, print "Good game":

```
OfdlDSA|3tXb32~X3tX@sX`4tXtz
```

Now, what was the hint of the question? It was:

> What will be the input of the file to get output Good game?

So it should be this. Honestly, I've played so many CTFs that when I see a string like this I don't doubt it like I used to. And yes, this was the right answer, right in front of our eyes.

I think the previous one was a bit more complicated, or maybe it wasn't and I just didn't pay attention. Anyway, let's move on.

## Crackme 6

The title/hint of the challenge: *Analyze the binary for the easy password*.

The first thing I got suspicious about was a function called `compare_pwd`, because it said that if there's user input, go ahead based on this function. So I went inside it.

Inside it, another function caught my eye, called `my_secure_test`. It said if this is non-zero, print "not correct", and if it's zero, print "correct". So I went into it:

```c
__int64 __fastcall my_secure_test(_BYTE *a1)
{
  if ( *a1 != 49 )
    return 0xFFFFFFFFLL;
  if ( a1[1] != 51 )
    return 0xFFFFFFFFLL;
  if ( a1[2] != 51 )
    return 0xFFFFFFFFLL;
  if ( a1[3] != 55 )
    return 0xFFFFFFFFLL;
  if ( a1[4] != 95 )
    return 0xFFFFFFFFLL;
  if ( a1[5] != 112 )
    return 0xFFFFFFFFLL;
  if ( a1[6] != 119 )
    return 0xFFFFFFFFLL;
  if ( a1[7] != 100 )
    return 0xFFFFFFFFLL;
  if ( a1[8] != 0 )
    return 0xFFFFFFFFLL;
  return 0;
}
```

The answer has to be inside this.

The problem was that at first I thought these numbers were hex, but with a little help I realized they're decimal. So I wrote a very simple script that converts them to characters, and that's how I got the answer:

```
[49, 51, 51, 55, 95, 112, 119, 100, 0]
```

## Crackme 7

Challenge hint: *Analyze the binary to get the flag*.

This one is a simple program. When you run it, it has 3 options you can choose from:

- `name`: you give your name and it says hello
- `add number`: you give two numbers and it adds them
- exit

So let's go into IDA. As soon as I got in, I understood what's going on. If you focus, you can see it too:

![crackme7 pseudocode](images/crackme7-menu-pseudocode.png)

The number `31337`: if we enter it, it gives the flag. So I enter this number and it gives me the flag.

## Crackme 8 (the last one)

Challenge hint: *Analyze the binary and obtain the flag*.

First we open it. It asks for a password, and when I enter something wrong it says I don't have access. So we have to find the right password or the flag.

Right at the start, an idea came to my mind: what if I reverse this condition? Does it work? Let's try.

I changed the first condition, and I saw there's one more condition, so I decided to go inside and see what it is. Honestly, it was much simpler than I thought: it says if the password is equal to this number, give the flag:

```
-889262067
```

I got the flag, but I wanted to see if I could change the second condition too and still get the flag.

And you know what interesting thing happened? I solved it. There were 2 conditions in this program, I changed both of them, and I got the flag. So we were able to crack this program in 2 ways and get the flag.

![crackme8 patched graph](images/crackme8-patched-graph.png)

---

## Things I picked up

- Flipping a condition (`jz` → `jnz`) can make the program say "correct", but that doesn't give you the flag if the flag is never printed. Sometimes you really have to understand the code.
- `LL` at the end of a number means `long long`.
- Strings in memory can be little-endian, so swap the bytes before doing anything else (like XOR).
- Numbers in IDA can be decimal, not only hex. Check before converting.
- The more challenges you solve, the better you get.
