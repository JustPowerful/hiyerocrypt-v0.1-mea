![LOGO](https://www.mediafire.com/convkey/e8c7/hbtduchh0f0bmzvzg.jpg)
![Name](https://img.shields.io/badge/Encryption-MEA-brightgreen)
[![Website](https://img.shields.io/website/https/justpowerful.github.io/Multiplying-encryption-algorithm?down_message=down&up_message=up)](https://justpowerful.github.io/Multiplying-encryption-algorithm)
[![Issues](https://img.shields.io/bitbucket/issues-raw/JustPowerful/Multiplying-encryption-algorithm)](https://github.com/JustPowerful/Multiplying-encryption-algorithm/issues)


 - Check out the official code [website](https://justpowerful.github.io/Multiplying-encryption-algorithm/)

**Note :** *don't use this algorithm for important features like securing passwords, emails, etc .. <a href="https://github.com/JustPowerful/Multiplying-encryption-algorithm#about-the-project-">read about the project</a>*

# About the project :
- Its a project made in a programming event for fun, please don't ever use this project in your important projects since this encryption algorithm is not really secure.
- This project can be used only in python, there's no version for other programming languages.
- This is an old project of mine, there's a lot of mistakes, it was my first to try to learn about encryption so if you want to improve the code or to add more features in the code you can actually contribute.



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
