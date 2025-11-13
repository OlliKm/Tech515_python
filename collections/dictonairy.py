
student1 = {'name' : ['Susan Smith']}
stream = { 'tech'}
completed_lessons = int(4)
completed_lesson_names = {"Tech Basics", "python Basics", "SQL integration"}

Student_info = (
    f"name: {', '.join(student1)}\n"
    f"selected stream: {', '.join(stream)}\n"
    f"completed classes: {completed_lessons}\n"
    f"Completed lesson names: {', '.join(completed_lesson_names)}"
)

print(Student_info)
print(type(Student_info))

#trying to broaden understanding of using keys and values
data_dict = {'key' : ['values','values2','values3','values4'],
             'key2' : ['values5','values6','values7','values8'],}

tickers = ['values', 'values2', 'values3', 'values4']
data_dict['tickers'] = tickers

print(data_dict['tickers'])