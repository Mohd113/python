if __name__ == '__main__':
    ifile = open("C:\\Users\\Chiefan\\Documents\\delivery1.txt", "r")
    fline = int(ifile.readline())
    count = 1
    for i in range(0, fline):
        cline = int(ifile.readline())
        time = 0
        for k in range(0, cline):
            time += int(ifile.readline())
        time *= 2
        print str(i+1) + ". " + str(time)
