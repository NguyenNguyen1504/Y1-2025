def main():
    m = input("Enter the mother's alleles (BB, Bb, or bb): \n")
    f = input("Enter the father's alleles (BB, Bb, or bb): \n")

    if m == "BB" or f == "BB":
        print("Their child is 100% likely to have brown eyes.")
    elif m == "bb" and f == "bb":
        print("Their child is 100% likely to have blue eyes.")
    elif m == "Bb" and f == "Bb":
        print("Their child is 75% likely to have brown eyes and 25% likely to have blue eyes.")
    else:
        print("Their child is 50% likely to have brown eyes and 50% likely to have blue eyes.")

main()