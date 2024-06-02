from datetime import datetime


def from_founds(value):

    if "from" in value:
        base_str = value["from"].split(" ")
        accrual_of_funds = value["from"].split(" ")[-1]
        if len(accrual_of_funds) == 16 and len(base_str) == 2:
            new_card = "".join(base_str[0] + " " + (accrual_of_funds[:4] + " " + accrual_of_funds[4:6]
                                                    + "** " + "**** " + accrual_of_funds[-4:]))
            return new_card
        elif len(accrual_of_funds) == 16 and len(base_str) == 3:
            new_card = "".join(base_str[0] + base_str[1] + " " + (accrual_of_funds[:4] + " " + accrual_of_funds[4:6]
                                                                  + "** " + "**** " + accrual_of_funds[-4:]))
            return new_card
        else:
            new_score = "".join(base_str[0] + " " + "**" + accrual_of_funds[-4:])
            return new_score


def to_founds(value):

    if "to" in value:
        base_str = value["to"].split(" ")
        accrual_of_funds = value["to"].split(" ")[-1]
        if len(accrual_of_funds) == 16 and len(base_str) == 2:
            new_card = "".join(base_str[0] + " " + (accrual_of_funds[:4] + " " + accrual_of_funds[4:6]
                                                    + "**" + " " + "****" + " " + accrual_of_funds[-4:]))
            return new_card
        elif len(accrual_of_funds) == 16 and len(base_str) == 3:
            new_card = "".join(base_str[0] + base_str[1] + " " + (accrual_of_funds[:4] + " " + accrual_of_funds[4:6]
                                                                  + "** " + "**** " + accrual_of_funds[-4:]))
            return new_card
        else:
            new_score = "".join(base_str[0] + " " + "**" + accrual_of_funds[-4:])
            return new_score


def date_operation(value):

    date_ = datetime.strftime(datetime.strptime(value["date"], "%Y-%m-%dT%H:%M:%S.%f"), format="%d.%m.%Y")

    return date_
