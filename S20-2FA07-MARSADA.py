import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = datetime.date(year, month, day)

formatted_date = event_date.strftime("%B %d, %Y")
weekday = event_date.strftime("%A")
month_name = event_date.strftime("%B")

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", formatted_date)
print("Year:", year)
print("Month:", month_name)
print("Day:", day)
print("Weekday:", weekday)
