import sys

filename = sys.argv[1]

def process(str):
    if str=="-":
        return ""
    else:
        return str

print("transcriptRefChrFwd = [")
plus = True

f=open(filename, 'r')

for line in f:
    fields = line.strip().split("\t")
    if (plus and fields[1]=='-'):
        plus = False
        print("]\n")
        print("transcriptRefChrRev = [")

    print("[%d, %d, %s]," % (
        int(fields[2]), # start
        int(fields[3]), # end
        fields[4] # value
    ))

print("]")