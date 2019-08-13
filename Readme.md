![LOGO](https://www.mediafire.com/convkey/e8c7/hbtduchh0f0bmzvzg.jpg)
![Name](https://img.shields.io/badge/Encryption-MEA-brightgreen)
[![Website](https://img.shields.io/website/https/justpowerful.github.io/Multiplying-encryption-algorithm?down_message=down&up_message=up)](https://justpowerful.github.io/Multiplying-encryption-algorithm)
[![Issues](https://img.shields.io/bitbucket/issues-raw/JustPowerful/Multiplying-encryption-algorithm)](https://github.com/JustPowerful/Multiplying-encryption-algorithm/issues)


 - Check out the official code [website](https://justpowerful.github.io/Multiplying-encryption-algorithm/)
 - BTC donate : ``3HUFJF46DimtGdg6mXsPFHWApmFCHcawKy``

# About the project :
- the idea is not totally mine , my friend asked me if i can make an encryption algorithm to challenge the group to decrypt it , it was fun , i sent them "hello world" encrypted and decrypted and i told them to decrypt a another phrase .
- the project is not totally completed you'll find some errors and bugs , if you want to report bugs just use [Issues Report](https://github.com/JustPowerful/Multiplying-encryption-algorithm/issues) 
- you can also contribute to make the project more and more better !

## How to use ?
- first you need to import the script , like this :

```python
import mea
```
you can find an example on ``example.py``

- String Encryption Method :

```python
import mea
api = mea.MEA()

ENCRYPTED = api.encrypt("Hello World")
print(ENCRYPTED)
```

- String Decryption Method :

```python
import mea
api = mea.MEA()

DECRYPTED = api.decrypt("ЦÊØØÞ@®ÞäØÈ")
print(DECRYPTED)
```

- List encryption :

```python
from mea import LIST

lst = LIST()

# returns a encrypted list
enclist = lst.enlist("hello world")
```

- List decryption:

```python
from mea import LIST

lst = LIST()

# returns a decrypted list
declist = lst.delist("208 202 216 216 222 64 238 222 228 216 200") # don't forget to add the space between every ascii
```


## Authors :

- [JustPowerful](https://github.com/JustPowerful)
