import sys


f = open(sys.argv[2], 'r', encoding='utf-8')
lines = f.readlines()
f.close()

f = open("timeline.tex", 'w', encoding='utf-8');
f.write("\\newpage \\section{Seznam letopočtů} \mbox{}\\\\ \n")

for line in lines:
  if "\\lp{" in line:
    line = line[(line.find("\\lp")):]

    uroven = 0
    i = 0
    zbyva = 2
    konec = 0
    for x in line:
      i = i + 1
      if x == "{":
        uroven = uroven + 1
      if x == "}":
        uroven = uroven - 1
        if uroven == 0:
          zbyva = zbyva - 1
      if zbyva == 0:
        break
    line = "\indent " + line[:i] + " \\\\ \n"
    f.write(line);

  if "\\section{" in line:
    line = line[(line.find("\\section")+8):]

    uroven = 0
    i = 0
    zbyva = 1
    konec = 0
    for x in line:
      i = i + 1
      if x == "{":
        uroven = uroven + 1
      if x == "}":
        uroven = uroven - 1
        if uroven == 0:
          zbyva = zbyva - 1
      if zbyva == 0:
        break
    line = "\mbox{} \\\\ \\begin{large} \\textbf{"+ line[:i] + "} \\end{large} \mbox{} \\\\ \n"
    f.write(line);

  if "\\subsection{" in line:
    line = line[(line.find("\\subsection")+11):]

    uroven = 0
    i = 0
    zbyva = 1
    konec = 0
    for x in line:
      i = i + 1
      if x == "{":
        uroven = uroven + 1
      if x == "}":
        uroven = uroven - 1
        if uroven == 0:
          zbyva = zbyva - 1
      if zbyva == 0:
        break
    line = "\\textbf" + line[:i] + " \\\\ \n"
    f.write(line);

f.write("\mbox{}")
    
f.close()


import os  
os.system("pdflatex "+sys.argv[1]+" "+sys.argv[2])
