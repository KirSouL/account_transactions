from utils import from_founds, to_founds, date_operation
from loadfile import sorted_executed_operation


def main():
    list_operation = sorted_executed_operation()[:5]

    for item in list_operation:
        from_ = from_founds(item)

        if from_ is None:
            print(f"{date_operation(item)} {item["description"]}\n"
                  f"{to_founds(item)}\n"
                  f"{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{date_operation(item)} {item["description"]}\n"
                  f"{from_} -> {to_founds(item)}\n"
                  f"{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n")


if __name__ == "__main__":
    main()
