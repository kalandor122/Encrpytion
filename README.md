# Encryption Project

A simple encryption and decryption tool in Python.

## Overview

This project implements a basic encryption cipher that converts messages into numeric sequences using positional indices, then applies mathematical transformations with random keys.

## Files

- **encrypt.py** - Encryption script that encodes a message
- **decode.py** - Decryption script that decodes an encrypted message

## How It Works

### Encryption (main.py)
1. Converts each letter to its alphabet position (a=1, b=2, etc.)
2. Generates two random keys (x: 1-9, y: 1-999)
3. Combines positions with mathematical operations
4. Outputs three components needed for decryption

### Decryption (decode.py)
1. Takes the encrypted message and two keys as input
2. Reverses the mathematical operations
3. Converts numeric positions back to letters

## Usage

```bash
python encrypt.py
# Enter your message when prompted
# Note the three keys generated

python decode.py
# Enter key 1, key 2, and encrypted message when prompted
```

## Limitations

- Doesn't support spaces!
- Only supports lowercase letters
- Simple substitution cipher; not cryptographically secure
- For educational purposes only
