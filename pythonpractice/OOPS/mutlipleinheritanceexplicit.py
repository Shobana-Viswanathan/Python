class TeamMember:
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def display(self):
        print(f"TeamMember: {self.name}, UID: {self.uid}")


class Worker:
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle   

    def display(self):
        print(f"Pay: {self.pay}, JobTitle: {self.jobtitle}")


class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)

    def display(self):
        TeamMember.display(self)
        Worker.display(self)
        print(f"Experience: {self.exp}")



tl = TeamLeader("Shobana", 101, 50000, "Tester", 5)


tl.display()