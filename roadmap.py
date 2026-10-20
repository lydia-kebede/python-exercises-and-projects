
# Python Career Roadmap Planner

career_goals = {
    "1": "Full-Stack Web Developer",
    "2": "AI Engineer",
    "3": "Problem-Solving Specialist"
}

roadmap = {
    "Full-Stack Web Developer": [
        "HTML and CSS",
        "JavaScript",
        "React",
        "Node.js and backend development",
        "Databases and APIs",
        "Full-stack projects"
    ],
    "AI Engineer": [
        "Python fundamentals",
        "Data structures and algorithms",
        "NumPy and pandas",
        "Machine learning",
        "Deep learning",
        "AI projects"
    ],
    "Problem-Solving Specialist": [
        "Python problem solving",
        "Arrays and strings",
        "Hash maps and sets",
        "Binary search",
        "Stacks and queues",
        "Trees and graphs",
        "LeetCode and Codeforces practice"
    ]
}

completed_skills = []
completed_projects = []
study_hours = 0


def show_career_goals():
    print("\n=== YOUR CAREER GOALS ===")

    for key, goal in career_goals.items():
        print(key + ".", goal)


def show_roadmap():
    print("\n=== CAREER ROADMAP ===")

    for career, skills in roadmap.items():
        print(f"\n{career}:")

        for index, skill in enumerate(skills, start=1):
            if skill in completed_skills:
                status = "Completed"
            else:
                status = "Not completed"

            print(f"{index}. {skill} - {status}")


def complete_skill():
    show_roadmap()

    skill = input("\nEnter the exact skill you completed: ").strip()

    all_skills = []

    for skills in roadmap.values():
        all_skills.extend(skills)

    if skill in all_skills:
        if skill not in completed_skills:
            completed_skills.append(skill)
            print("Skill marked as completed!")
        else:
            print("You already completed this skill.")
    else:
        print("Skill not found. Check the roadmap and try again.")


def add_project():
    project = input("Enter your completed project name: ").strip()

    if project:
        completed_projects.append(project)
        print("Project added successfully!")
    else:
        print("Project name cannot be empty.")


def record_study_hours():
    global study_hours

    try:
        hours = float(input("How many hours did you study? "))

        if hours > 0:
            study_hours += hours
            print("Study hours recorded!")
        else:
            print("Enter a number greater than zero.")

    except ValueError:
        print("Please enter a valid number.")


def show_progress():
    all_skills = []

    for skills in roadmap.values():
        all_skills.extend(skills)

    total_skills = len(all_skills)
    completed_count = len(completed_skills)

    percentage = completed_count / total_skills * 100

    print("\n=== YOUR PROGRESS REPORT ===")
    print(f"Skills completed: {completed_count}/{total_skills}")
    print(f"Overall skill completion: {percentage:.1f}%")
    print(f"Total study hours: {study_hours}")
    print(f"Projects completed: {len(completed_projects)}")

    if completed_projects:
        print("\nYour projects:")

        for project in completed_projects:
            print("-", project)


def save_progress():
    with open("career_progress.txt", "w") as file:
        file.write("CAREER ROADMAP PROGRESS\n")
        file.write("=======================\n")
        file.write(f"Study hours: {study_hours}\n")
        file.write(f"Completed skills: {len(completed_skills)}\n")
        file.write("\nCompleted skills:\n")

        for skill in completed_skills:
            file.write(f"- {skill}\n")

        file.write("\nCompleted projects:\n")

        for project in completed_projects:
            file.write(f"- {project}\n")

    print("Progress saved to career_progress.txt")


def main():
    while True:
        print("\n====== CAREER ROADMAP PLANNER ======")
        print("1. Show career goals")
        print("2. Show learning roadmap")
        print("3. Mark a skill as completed")
        print("4. Add a completed project")
        print("5. Record study hours")
        print("6. View progress report")
        print("7. Save progress")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_career_goals()
        elif choice == "2":
            show_roadmap()
        elif choice == "3":
            complete_skill()
        elif choice == "4":
            add_project()
        elif choice == "5":
            record_study_hours()
        elif choice == "6":
            show_progress()
        elif choice == "7":
            save_progress()
        elif choice == "8":
            save_progress()
            print("Keep learning and building your career!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 8.")


main()
