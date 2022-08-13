import os
import re
import subprocess
import glob

# *** Tool executing procedure ***
# Kakadu application should be installed 
# Install Kakadu application exe path should capture in the "jp2.ini" file within the <path></path> tag.
# get the Input file directory
# Tool will convert the TIFF tag into JPEG2000 the same location Input file directory

print("\n *** TIFF to JPEG 2000 Conversion *** \n")

filepath = input(" Enter the File path: ")

text_file = filepath + "/" + "error.log"

jp2 = "jp2.ini"

# check the exiftool file present
if os.path.exists(jp2):
	pass
else:
	print("\n jp2.ini tool is missing")
	f = open(text_file, "a+")
	f.write(str("jp2.ini tool is missing\n"))
	f.close()
	exit()

#reading the tag.ini file
fo = open(jp2, "r+", encoding="utf-8")
val1 = fo.read()
text = re.search(r"<path>(.*)</path>", str(val1))
val2 = str("\"") + text.group(1) + str("\"")
val3 = text.group(1)

if os.path.exists(val3):
	pass
else:
	print("\n kdu_compress.exe path is not correct")
	f = open(text_file, "a+")
	f.write(str("kdu_compress.exe path is not correct\n"))
	f.close()
	exit()

for fname in glob.glob(filepath + "/" + "*.tif"):
	input_file = str("\"") + fname + str("\"")
	print(input_file)
	name = os.path.basename(fname)
	splitname = os.path.splitext(name)[0]
	jp2_filename = str("\"") + filepath + "/" + splitname + ".jp2" + str("\"")
	conversion = val2 + " " + "-i"+ " " + input_file + " "  + "-o" + " " + jp2_filename + " " + "-rate" + " " + "-,4,2,1,0.7,0.5,0.35,0.25,0.18,0.125,0.088,0.0625,0.04419,0.03125,0.0221,0.015625" + " "  + "Cmodes=BYPASS" + " " + "Cuse_sop=yes" + " " + "Cuse_eph=yes" + " " + "-quiet" + " " + "-double_buffering" + " " + "8" + " " + "-num_threads" + " " + "4" + " " + "Clevels=6" + " " + "Cprecincts={256,256},{256,256},{128,128}" + " " + "Corder=RPCL" + " " + "ORGtparts=R" + " " + "Cblk={64,64}" + " " + "ORGgen_plt=yes" + " " + "Creversible=yes" + " " + "Stiles={1024,1024}"
	subprocess.call(conversion)
print("\n*** JP2 Conversion Completed ***")
