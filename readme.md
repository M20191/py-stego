# Py-Stego
<p align=center><a href="#"><img title="build" src="https://img.shields.io/badge/status-FINISH-green?style=for-the-badge&logo=github"><a></p>
<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue?style=flat-square&logo=python"></a>
  <a href="#"><img src="https://img.shields.io/badge/LINUX-blue?style=flat-square&logo=linux"></a>
  <a href="#"><img src="https://img.shields.io/badge/WINDOWS-blue?style=flat-square&logo=windows"></a>
</p>

<p>
    Py-Stego is a open source project dedicated to steganography text in images PNG
</p>

---

### 📄 File Support
* PNG

## 🛠 Downloading repo, cd path and install requirements:
```bash
git clone https://github.com/M20191/py-stego && cd py-stego/ && pip install -r requirements.txt
```
## 🐍 Usage Encode
```bash
python/python3 main.py --text "Secret!!" --encode to_encode.png
```
## 🐍 Usage Decode
```bash
python/python3 main.py --decode to_encode_encoded.png
```
## 📌 Arguments
```bash
Usage: py/python3 main.py [-h] [-t] {-e,-d}

Arguments:
  -h, --help         Show this help message
  -t, --text         Text to encode
  -e, --encode       Image file to encode data
  -d, --decode       Image to decode data
```
## 🔒 Normal image
![normal](to_encode.png)

## 🔐 Encrypted image
![encrypted](encode/to_encode_encoded.png)
