def monthConvertor():
    monthConversion = {
        "jan": "January",
        "feb": "Feburary",
        "mar": "March",
        "apr": "April",
        "may": "May",
        "june": "June",
        "jul": "July",
        "aug": "August",
        "sept": "September",
        "oct": "October",
        "nov": "Novemeber",
        "dec": "December"
    }

    month = input("Enter month you would like to convert: ")
    if month.lower() not in monthConversion:
        monthConvertor()
    else:
        print(monthConversion.get(month))


monthConvertor()
