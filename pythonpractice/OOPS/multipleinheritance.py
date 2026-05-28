class TeamMember:
    def __init__(self, name , uid):
        self.name = name
        self.uid = uid

class Workers:
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle

class TeamLeader(TeamMember, Workers):
    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Workers.__init__(self, pay, jobtitle)

        print("Name: {}, Pay: {}, Exp: {}".format(self.name,self.pay,self.exp))

TL = TeamLeader("Shobana", 1001, "50000", "Scrum Master", 5)