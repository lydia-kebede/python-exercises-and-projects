# class = blueprint or design plan for creating objects
# Attributes = what an object is or has.
# methods = what an object can do. or actions 
class Football:

    def __init__(self,coach,player,referee,staff_members):
        self.coach = coach
        self.player = player
        self.referee = referee
        self.staff_members = staff_members

    def coach_job(self):
        print("The coach is responsible for training player.")
    def train(self):
        print(" " + self.player + " needs to train regularly.")

        # let's create an object
team_barcelona = Football("Xavi", "Messi", "Antonio Mateu Lahoz", "Medical team")
team_aresenal = Football("Mikel Arteta", "Bukayo Saka", "Anthony Taylor", "Medical team")
print(team_barcelona.coach)
print(team_barcelona.player)
print(team_aresenal.coach)
print(team_aresenal.player)
team_barcelona.train()
team_aresenal.coach_job()
# self refers to the current object that is using a method.
