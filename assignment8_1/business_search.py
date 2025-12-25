def is_valid_business_id(business_id):
    # example of a valid business ID: 0112038-9
    WEIGHTS = [7, 9, 10, 5, 8, 4, 2]
    split_id = business_id.split('-')
    number, check = split_id[0], split_id[1]
    weighted_sum = 0
    for i in range(len(number)):
        weighted_sum += int(number[i]) * WEIGHTS[i]
    remainder = weighted_sum % 11
    code = -1
    if remainder == 0:
        code = 0
    elif remainder >= 2:
        code = 11 - remainder
    return int(check) == code

def businesses_from_file(filename):
    name_id_dict = {}
    try:
        source = open(filename, "r")

        for line in source:
            line = line.rstrip()
            parts = line.split(",")
            part_id = parts[1].strip()
            if is_valid_business_id(part_id):
                name_id_dict[part_id] = parts[0]
            else:
                print(f"WARNING: Incorrect business id: {line}")
        source.close()
        print(f"Read {len(name_id_dict)} valid company/companies.")

    except OSError:
        print(f"ERROR: Could not open file {filename}")

    return name_id_dict

def main():
    print("Business search")
    filename = input("Which file to read?\n")
    read_business = businesses_from_file(filename)
    if len(read_business) > 0:
        search = input("What would you like to search for (enter for all)?\n")
        filtered = {}
        for b_id in read_business:
            if search in b_id or search in read_business[b_id]:
                filtered[read_business[b_id]] = b_id

        print("Search results:\n")
        print("Name                           | Business ID")
        print("-------------------------------+------------")
        for b_name in filtered:
            print(f"{b_name:<30s} | {filtered[b_name]}")

    else:
        print("No businesses found: quitting...")

main()
