def check_student_age(age):
 
  if 10 <= age <= 20:
    print("Student is eligible for enrollment.")
  else:
    print("Student is not eligible for enrollment.")

student_age = int(input("Enter the student's age: "))
check_student_age(student_age)