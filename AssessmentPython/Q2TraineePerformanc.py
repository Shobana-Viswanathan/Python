class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        print(f"Name: {self.name} | Age: {self.age}")
        print(f"Email: {self.email}")


class Trainee(Person):
    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications):
        super().__init__(name, age, email)
        self.batch_id = batch_id
        self.marks = marks
        self.num_projects = num_projects
        self.num_publications = num_publications

    def display_info(self):
        super().display_info()
        print(f"Batch: {self.batch_id}")
        print(f"Marks: {self.marks} Avg: {sum(self.marks)/len(self.marks):.2f}")
        print(f"Projects: {self.num_projects} | Publications: {self.num_publications}")

class SDETTrainee(Trainee):
    def __init__(self, name, age, email, batch_id, marks, num_projects, num_publications, tool_proficiency):
        super().__init__(name, age, email, batch_id, marks, num_projects, num_publications)
        self.tool_proficiency = tool_proficiency

    def compute_aggregate(self):
        avg_marks = sum(self.marks) / len(self.marks)
        aggregate = (avg_marks * 0.6) + (self.num_projects * 5) + (self.num_publications * 3)

        print(f"Tool: {self.tool_proficiency}")
        print(f"Aggregate Score: {aggregate:.2f}")
        return aggregate
        
trainees = []
t1 = SDETTrainee("Viswa", 24, "viswa@example.com", "B2025",[78, 85, 90, 72, 88], 3, 2, "Selenium")
t2 = SDETTrainee("Shobana", 23, "shobana@example.com", "B2025", [65, 70, 68, 74, 72], 2, 1, "Playwright")
trainees.append(t1)
trainees.append(t2)
scores = {}
for t in trainees:
    t.display_info()
    score = t.compute_aggregate()
    scores[t.name] = score















