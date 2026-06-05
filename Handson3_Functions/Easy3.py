def salary (salary,hike):
    result = salary + (salary * hike / 100)
    return result
salary_old=int(input("Enter your salary:"))
hike=int(input("Enter hike:"))
ans=salary(salary_old,hike)
print("Salary is :",ans) 