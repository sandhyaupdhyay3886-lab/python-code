#Given a dictionary of student names and their marks, print only the names of students who scored above 75
marks={"rahul":76,
       "sohan":65,
       "rita":89,
       "rohit":45
}
for name, marks in marks.items():
    if marks>75:
        print(name)