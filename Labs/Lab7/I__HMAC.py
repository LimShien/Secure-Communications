"""
Write a Python or Node.js program which will prove the following:
Type: HMAC-MD5
Message: Hello
Password: qwerty123
Hex: c3a2fa8f20dee654a32c30e666cec48e
Base64: 7376b67daf1fdb475e7bae786b7d9cdf47baeba71e738f1e
"""
import hmac
import hashlib
import base64


message = bytes('Hello', "utf-8")
password = bytes('qwerty123', "utf-8")

s =hmac.new(password,message,hashlib.md5).hexdigest()

print(hmac.new(password,message,hashlib.md5).hexdigest())
print(base64.b64decode(s).hex())