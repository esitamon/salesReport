class Team:
    def __init__(self,teamId,teamName):
        self.teamId = teamId
        self.teamName = teamName

        
    def __str__(self) -> str:
        return f"{self.teamId} {self.teamName}"
    