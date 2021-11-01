from utils import parse_report


def main():
    file_path = input("Insert file path:")
    minimum_count = int(input("Insert The minimum count number:"))
    if minimum_count > 0:
        parse_report(minimum_count, file_path)
    else:
        print(f"you should insert Positive numbers for minimum count of words.")


if __name__ == '__main__':
    main()
