import sys

# takes input from an tab delimited file from
# the NCBI genomes database and spits out json

filename = sys.argv[1]

def process(str):
    if str=="-":
        return ""
    else:
        return str


f=open(filename, 'r')

for i in range(0,2):
    f.readline()

for line in f:
    fields = line.split("\t")
    if (len(fields) == 10):
	    print("[\"chr\", \"%s\", %d, %d, \"%s\", \"%s\"]," % (
	        fields[3], # strand
	        int(fields[1]), # start
	        int(fields[2]), # end
	        fields[8], # VNG name
	        process(fields[7]), # common name 
	    ))
