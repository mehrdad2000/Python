import sys
from Crypto.Cipher import DES
import binascii
from Crypto.Util.strxor import strxor  # Import the strxor function

def macIso9797_m1_alg3(key, msg):
    return macIso9797_alg3(key, msg, "00")

def macIso9797_alg3(key, msg, pad_start):
    key_len = int(len(key) / 2)

    if key_len != 16:
        raise ValueError("Key length should be 16 digits")

    # Force header padding
    msg += pad_start

    # Padding with "00" to ensure total length is a multiple of 8 bytes
    lenRestOfData = int((len(msg) / 2) % 8)
    msg += "00" * (8 - lenRestOfData)

    loopNum = int(len(msg) / 16)  # Each DES block is 8 bytes (16 hex characters)

    bufferOutput = binascii.unhexlify("00" * 8)

    keya = binascii.unhexlify(key[0:16])
    keyb = binascii.unhexlify(key[16:])

    for i in range(loopNum):
        tdesa = DES.new(keya, DES.MODE_ECB)

        data = msg[i * 16 : (i + 1) * 16]  # Process one DES block (16 hex characters)

        bufferOutput = strxor(binascii.unhexlify(data), bufferOutput)
        bufferOutput = tdesa.encrypt(bufferOutput)

    tdesb = DES.new(keyb, DES.MODE_ECB)
    bufferOutput = tdesb.decrypt(bufferOutput)

    tdesa = DES.new(keya, DES.MODE_ECB)
    bufferOutput = tdesa.encrypt(bufferOutput)

    return bufferOutput


macKey = "1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A1A"


message = "0600E238010188C10004000000000000000516603799000000000089000002241839561775171540100224100066037990660379953988234527017990001      1111111100487500111033011O10040003Y8        C245DE39851740D00245900000000000000000000000160000000000000000"

hexMessage = bytes(message, encoding="utf-8").hex()

print("MAC Key: " + macKey)
print("MAC: " + macIso9797_m1_alg3(macKey, hexMessage).hex())

