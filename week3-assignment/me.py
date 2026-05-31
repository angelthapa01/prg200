jobs = []


def add_job():
    company = input("Enter company name: ")
    jobs.append(company)
    print("Job added")


def view_jobs():
    print("\nApplied Jobs:")

    for job in jobs:
        print(job)


def remove_job():
    company = input("Enter company name to remove: ")

    if company in jobs:
        jobs.remove(company)
        print("Job removed")

    else:
        print("Job not found")


while True:
    print("\n1. Add Job")
    print("2. View Jobs")
    print("3. Remove Job")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_job()

    elif choice == "2":
        view_jobs()

    elif choice == "3":
        remove_job()

    elif choice == "4":
        print("Program Ended")
        break

    else:
        print("Invalid choice")