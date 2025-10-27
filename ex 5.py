# Excersice 5:days of the months

# Step 1: Creating a dictionary
month_days={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
  }

month = int(input("Enter the month number (1-12): "))

if month in month_days:
    leap=input("Is it leap year? (yes/no): ").strip().lower()
    if month ==2: #basically Feb
      if leap == "yes":
          print("29 days")
          
    else:
            print("28 days")
else:
        print(f"{month_days[month]} days")
                                                                            
   else:
    print("Invalid month number")