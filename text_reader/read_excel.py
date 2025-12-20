import csv

def main():
    with open("grade.csv","r") as source:
        for row in source:
            print(row)

main()
