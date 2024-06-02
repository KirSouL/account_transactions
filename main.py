from utils import get_mask, date_operation
from loadfile import sorted_executed_operation


def main():
    list_operation = sorted_executed_operation()[:5]

    for item in list_operation:
        date_ = date_operation(item["date"])

        if "from" in item:
            from_ = get_mask(item["from"].split(" "))
            to_ = get_mask(item["to"].split(" "))
        else:
            from_ = None
            to_ = get_mask(item["to"].split(" "))

        if from_ is None:
            print(f"{date_} {item["description"]}\n"
                  f"{to_}\n"
                  f"{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{date_} {item["description"]}\n"
                  f"{from_} -> {to_}\n"
                  f"{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n")


if __name__ == "__main__":
    main()
