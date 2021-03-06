def days_in_month(year, month):
  if year < 0 or month < 1 or month > 12:
    return "invalid input"
  else:
    isleap = True
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          print("Leap year.")
        else:
          isleap = False
          print("Not leap year.")
      else:
        print("Leap year.")
    else:
      isleap = False
      print("Not leap year.")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap == True:
      month_days[1] = 29
    return f"{month_days[month-1]}"

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
