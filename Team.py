class Team:
    def __init__(self,teamId,teamName):
        self.teamId = teamId
        self.teamName = teamName


    def __str__(self) -> str:
        return f"Team ID: {self.teamId} ,Team Name: {self.teamName}"
    
    def getTeamId(self):
        return self.teamId
    def getTeamName(self):
        return self.teamName