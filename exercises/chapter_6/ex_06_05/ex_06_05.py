text = "X-DSPAM-Confidence:    0.8475"

sppos = text.find(' ')

number = text[sppos:].lstrip()

print(float(number))
