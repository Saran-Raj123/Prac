class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

class ProjectManagementSystem:
    def __init__(self):
        self.projects = []
        self.completed_projects = []

    def load_projects(self):
        # Load projects from a file or database
        pass

    def save_projects(self):
        # Save projects to a file or database
        pass

    def display_projects(self):
        print("Incomplete projects:")
        for project in self.projects:
            print(" ", project)
        print("Completed projects:")
        for project in self.completed_projects:
            print(" ", project)

    def filter_projects_by_date(self, date):
        filtered_projects = [project for project in self.projects if project.start_date > date]
        for project in filtered_projects:
            print(" ", project)

    def add_project(self):
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yyyy): ")
        priority = input("Priority: ")
        estimate = float(input("Cost estimate: $"))
        completion = float(input("Percent complete: "))
        project = Project(name, start_date, priority, estimate, completion)
        self.projects.append(project)

    def update_project(self):
        self.display_projects()
        project_choice = int(input("Project choice: "))
        project = self.projects[project_choice]
        new_completion = float(input("New Percentage: "))
        new_priority = input("New Priority: ")
        project.completion = new_completion
        project.priority = new_priority

    def run(self):
        while True:
            print("- (L)oad projects")
            print("- (S)ave projects")
            print("- (D)isplay projects")
            print("- (F)ilter projects by date")
            print("- (A)dd new project")
            print("- (U)pdate project")
            print("- (Q)uit")
            choice = input(">>> ").lower()
            if choice == 'l':
                self.load_projects()
            elif choice == 's':
                self.save_projects()
            elif choice == 'd':
                self.display_projects()
            elif choice == 'f':
                date = input("Show projects that start after date (dd/mm/yyyy): ")
                self.filter_projects_by_date(date)
            elif choice == 'a':
                self.add_project()
            elif choice == 'u':
                self.update_project()
            elif choice == 'q':
                print("Thank you for using custom-built project management software.")
                break





