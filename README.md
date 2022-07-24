# Py Obfuscate
Playing around with Python based on obfuscated Javascript stuff


## Usage
```
pyin.py ARG

Obfuscate some text into a Python program which generates the original text. Surround resulting obfuscated text with a `print(OBFUSCATED TEXT)` to get the original back.

ARG:    A filename to read the contents and obfuscate or
        some text to obfuscate
```

```bash
# generated an obfuscated version of pyin.py
python3 pyin.py pyin.py > pyin_obfuscated.py

# pyin_obfuscated.py works exactly the same as pyin.py
python3 pyin_obfuscated.py 'Hello, World!'
# ... tons of craziness
# ...
```
