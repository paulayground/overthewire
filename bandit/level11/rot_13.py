import codecs
import sys

rot13_sentence = sys.stdin.read().strip()

decrypted = codecs.encode(rot13_sentence, 'rot_13')

print("".join(decrypted))
