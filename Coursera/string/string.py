
text = "X-DSPAM-Confidence:    0.8475"

print(text)

find = text.find(':') + 1

print('find ', find)

print(float(text[find:]))
