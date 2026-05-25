def salary_increment(salary,rating):
    if rating >= 1 and rating <=4 :
        res = salary * 0.1
        return res + salary
    elif rating >= 4.1 and rating <= 7 :
        res = salary * 0.25
        return res + salary
    elif rating >= 7.1 and rating <= 10 :
        res = salary * 0.3
        return res + salary
    else :
        print("Enter a valid appraisal rating")

salary=int(input("Enter salary:"))
apparaisal_rate = float(input("Enter rating:"))
incremental_salary = salary_increment(salary,apparaisal_rate)
print("Salary is: ",int(incremental_salary))