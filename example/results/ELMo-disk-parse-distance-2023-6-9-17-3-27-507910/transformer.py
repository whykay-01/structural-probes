import os

# get the path of the current working directory
path = os.getcwd()
new_document = open(path + "/output.tex", "x")

new_document.write("\documentclass{article}\n")
new_document.write("\usepackage{tikz}\n")
new_document.write("\usetikzlibrary{external}\n")
new_document.write("\tikzexternalize\n")
new_document.write("\begin{document}\n")
new_document.write("\begin{tikzpicture}\n")

# read the tikz file

tikz_file = open(path + "/dev.tex", "r")

for line in tikz_file:
    new_document.write(line)

new_document.write("\end{tikzpicture}\n")
new_document.write("\end{document}\n")

new_document.close()
tikz_file.close()
print("All the operations successfully completed. Open the output.tex file to see the intermediary result.")
