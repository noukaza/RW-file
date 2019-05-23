file_content = open("file.txt", "r")
out_put_file = open("out.txt", "w")
index = 00000
for line in file_content:
  splitLine = line.split("=")
  out = "C" + str(index).zfill(5) + "=" + splitLine[1]
  index += 1
  out_put_file.write(out)
file_content.close()
out_put_file.close()