def main():
    source = open('test.txt', 'r')
    for line in source:
        line = line.rstrip()
        print(line)
    source.close()
main()