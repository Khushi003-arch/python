#class data
marks=[8,81,52,4,50]
attendance=[15,20,25,85,96]
result=["pass","fail","pass","fail","pass"]

#univariate:

print("Average marks of students",sum(marks)/len(marks))
print("highest marks of student",max(marks))
print("lowest marks of student",min(marks))



print("==========================================================")

#biavariate analysis: (here we use two variable for the analytics)


for m in marks:
    if m >= 40:
        print(f"marks {m} result: pass")
    else:
        print(f"marks {m} result :fail")

print("===========================================")

# now count how many students are fail and pass:

pass_count=0
fail_count=0

for m in marks:
    if m >= 40:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1

print(f"pass students are: {pass_count}")
print(f"fail students are: {fail_count}")