# Cracking MD5 Hashes with Python and Hashlib

We are using hashlib and argparse modules. We are providing a small dictionary (of 1575 words) so that it is faster to crack. But u may need a bigger dictionary of millions of words for better results.

#### md5crack.py
---------------------------------------------------------------------
```python
import hashlib
import argparse

parser = argparse.ArgumentParser(description="MD5 Cracker")
parser.add_argument("-md5", dest="hash", help="md5 hash", required=True)    # required argument
parser.add_argument("-w", dest="wordlist", help="wordlist", required=True)     # required argument
parsed_args = parser.parse_args()

def main(): 
    hash_cracked = ""
    with open(parsed_args.wordlist) as file:
        for line in file:
            line = line.strip()
            if hashlib.md5(bytes(line,encoding="utf-8")).hexdigest() == parsed_args.hash:
                hash_cracked = line
                print("\nMD5-hash has been successfully cracked. The value is %s."%line)
    if hash_cracked == "":
        print("\nFailed to crack the hash. Try using a bigger/different dictionary.")

if __name__ == "__main__":
    main()

```
---------------------------------------------------------------------

Usage -> python md5crack.py -md5 <hash> -w dict.txt
Output -> Successfully cracked

### Suggested readings:

[dict.txt](https://github.com/SathvikTn/Python-Scripts/blob/master/dict.txt)