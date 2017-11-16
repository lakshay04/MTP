# skip the first one
inp = raw_input()

s = float(0)
no_val = 0
while True:
    try:
        inp = raw_input()
        no_val += 1
        old_s = s
        s += float(inp)
        print old_s, inp, s
    except:
        break
print s
print no_val
print str((float(s)) / (float(no_val)))
