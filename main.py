t_point = int(input("Enter Num: "))
s_point = int(input("Starting Num: "))
e_point = int(input("End Num: "))
while s_point <= e_point:
    table = t_point * s_point
    print(t_point, "*", s_point, "=", table)
    s_point += 1