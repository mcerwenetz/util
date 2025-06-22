"""
    This script reads a CSV file containing identification numbers in the 
    format "Identification (number) and then calculates the total number of 
    missing packages based on the difference between the numbers.

"""
import csv

def main(file_name):
    """ in the main function we read the input file and calculate the number of missing packages """

    list_of_identifications = []
    try:
        with open(file_name, 'r', encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            if "Identification" not in header:
                print("Error: The input file does not contain  'Identification'.")
                return

            column_index = header.index("Identification")


            for row in reader:
                identification_number = row[column_index]
                # get the number between parentheses
                identification_number = int(identification_number.split('(')[1].split(')')[0] )
                list_of_identifications.append(identification_number)

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")



    list_of_identifications = sorted(list_of_identifications)
    missing_package_counter = 0

    for i in range(len(list_of_identifications)-1):
        missing_package_counter += list_of_identifications[i+1]-list_of_identifications[i]


    print(missing_package_counter)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python ip_packloss.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    main(input_file)
