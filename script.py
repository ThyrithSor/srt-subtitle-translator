import sys
import re
import io

path = sys.argv[1]

# ----------------------------------------------------------

line_list = []

with io.open(path, 'r', encoding='utf-8') as f:
	content = f.readlines()

	ticker = 1
	is_time = False
	byte_order_mark = "\xef\xbb\xbf" # content[0].rstrip()[0]
	for i in range(0, len(content)):

		line = content[i].replace(byte_order_mark, "").rstrip()
		if line == str(ticker):
			ticker = ticker + 1
			is_time = True
		elif is_time:
			is_time = False
		elif line != "":
			line_list = line_list + [i]
	
	fl = open("lines.txt", "w")
	fc = open("untranslated.txt", "w")
	for line in line_list:
		fl.write(str(line) + "\r\n")
		fc.write(content[line])
	fl.close()
	fc.close()

# ----------------------------------------------------------

# with io.open(path, 'r', encoding='utf-8') as f:
# 	contents = f.readlines()

# with io.open("lines.txt", 'r', encoding='utf-8') as f:
# 	lines = f.readlines()

# with io.open("translated.txt", 'r', encoding='utf-8') as f:
# 	translates = f.readlines()

# for i in range(0, len(lines)):
# 	line = lines[i].rstrip()
# 	contents[int(line)] = translates[i]

# f = open("pokemon_detective.srt", "w")
# for i in range(0, len(contents)):
# 	f.write(contents[i])
# f.close()

