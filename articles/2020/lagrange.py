import sys

pts = []
for i in range(1,len(sys.argv),2):
	pts.append([int(sys.argv[i]), int(sys.argv[i+1])])

output = "P(x) = "

for i in pts:
	nr = ""
	dr = ""
	for r in pts:
		if r is i:
			continue
		dr += "({})".format(i[0]-r[0])
		if r[0] < 0:
			nr += "(x+{})".format(-r[0])
		else:
			nr += "(x-{})".format(r[0])
	output += "\\frac{{{2}{0}}}{{{1}}} + ".format(nr,dr,i[1])

print(output)
