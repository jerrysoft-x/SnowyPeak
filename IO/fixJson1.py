with open(r'C:\Users\JJLI\Downloads\0_51c4a08c45984ab19290f08a7e2d6dcd_1.json', 'r') as f:
    with open(r'C:\Users\JJLI\Downloads\output.json', 'w') as output:
        output.write('[')
        for l in f.readlines():
            output.write(l.strip() + ',\n')
        output.write(']')