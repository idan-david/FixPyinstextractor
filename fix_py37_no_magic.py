import sys
if len(sys.argv) != 2:
    print("fix.py [.pyc]")
    exit()

fname = sys.argv[1]

with open(fname, "rb") as o:
    data = o.read()

with open(fname + "_fixed.pyc", "wb") as o:
    o.write(bytes.fromhex("420d0d0a00000000e8be875d68300000"))
    o.write(data)