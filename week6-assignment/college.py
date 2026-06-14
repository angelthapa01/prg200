import datetime

# this program generates an exam schedule from a starting date

college_name = "Bhaktapur Multiple Campus"

start_date = "2025-05-01"

exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]


def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d")


def get_exam_date(start_str, days):
    start = parse_date(start_str)

    # add the required number of days
    exam_date = start + datetime.timedelta(days=days)

    return exam_date.strftime("%Y-%m-%d")


def print_schedule(start_str, exams):
    print(college_name)
    print("exam schedule")

    for subject, days in exams:
        print(subject, "-", get_exam_date(start_str, days))


print_schedule(start_date, exams)