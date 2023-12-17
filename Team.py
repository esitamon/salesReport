class Team:
    def __init__(self,teamId,teamName):
        self.teamId = teamId
        self.teamName = teamName
    
    def __eq__(self, __value: object) -> bool:
        pass
    
    def __hash__(self) -> int:
        return hash(self.teamId)
    
    def __str__(self) -> str:
        return f"{self.teamId} {self.teamName}"
    