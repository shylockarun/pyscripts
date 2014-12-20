import os

def split_file(filepath, lines_per_file=100):
    """splits file at `filepath` into sub-files of length `lines_per_file`
    """
    lpf = lines_per_file
    path, filename = os.path.split(filepath)
    with open(filepath, 'r') as r:
        name, ext = os.path.splitext(filename)
        try:
            w = open(os.path.join(path, '{}_{}{}'.format(name, 0, ext)), 'w')
            for i, line in enumerate(r):
                if not i % lpf:
                    #possible enhancement: don't check modulo lpf on each pass
                    #keep a counter variable, and reset on each checkpoint lpf.
                    w.close()
                    filename = os.path.join(path,
                                            '{}_{}{}'.format(name, i, ext))
                    w = open(filename, 'w')
                w.write(line)
        finally:
            w.close()


"""demonstrates the utility of split_file() function"""
testpath = "divide/"
if not os.path.exists(testpath): os.mkdir(testpath)
testfile = os.path.join(testpath, "div.xml")
split_file(testfile, 1000000)