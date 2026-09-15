is_year_leap_as_str = input("Напишите год вашего рождения: ")
is_year_leap = int(is_year_leap_as_str)

if (is_year_leap % 4 == 0):
    print("год", is_year_leap, ": True")
else:
    print("год", + is_year_leap, ": False")
