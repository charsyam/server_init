import sys, os

target = "../%s/"%(sys.argv[1])

exts = [
        ".java",
        ".proto",
        ".g"
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
                if "tajo" in line:
                    if ext == ".proto" and "import" in line:
                        pass
                    else:
                        newline = line.replace('tajo','org.apache.tajo')
                        print fullpath
                        line = newline

                t.write(line)

            t.close()

    if '.git' in dirnames:
        pass

