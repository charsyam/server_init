import sys, os

target = "../%s/"%(sys.argv[1])

exts = [
        ".java",
        ".proto",
        ".g",
        ".xml"
        ]
for dirname, dirnames, filenames in os.walk('.'):
    for subdirname in dirnames:
        pass

    for filename in filenames:
        name, ext = os.path.splitext(filename)
        if (ext in exts):
            fullpath = os.path.join(dirname, filename)
            newpath = target+fullpath
            f = open(fullpath)
            t = open(newpath, "w")
            lines = f.readlines()
            for line in lines:
                if "import tajo" in line:
                    newline = line.replace('import tajo','import org.apache.tajo')
                    print fullpath
                    line = newline
                elif "package tajo" in line:
                    newline = line.replace('package tajo','package org.apache.tajo')
                    print fullpath
                    line = newline
                elif "java_package = \"tajo" in line:
                    newline = line.replace('java_package = \"tajo','java_package = \"org.apache.tajo')
                    print fullpath
                    line = newline
                elif "import static tajo" in line:
                    newline = line.replace('import static tajo', 'import static org.apache.tajo')
                    print fullpath
                    line = newline
                elif "tajo." in line:
                    newline = line.replace('tajo.', 'org.apache.tajo.')
                    print fullpath
                    line = newline
            

                t.write(line)

            t.close()

    if '.git' in dirnames:
        pass

