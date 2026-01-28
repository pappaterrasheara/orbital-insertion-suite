import json
import os
from datetime import datetime



#Creates a json file with a the data from a dictionary. 
def dataToJson(data: dict, name : str) -> None: 
        with open(f'{name}.json', "w") as f: 
            json.dump(data, f, indent=4)

def createFolder(path: str) -> None:
    os.makedirs(path, exist_ok= True)

def dateToString() -> str:
    now = datetime.now()
    month = now.month
    day = now.day
    year = now.year
    hour = now.hour
    minute = now.minute
    second = now.second

    return f'{month}-{day}-{year} at {hour}-{minute}-{second}'
    

class Run:
    def __init__(self, q_limit: float, g_limit: float, q_max: float, g_max: float, passed: bool, description: str):
        self.q_limit = q_limit
        self.g_limit = g_limit
        self.q_max = q_max
        self.g_max = g_max
        self.passed = passed
        self.description = description

    q_limit: float
    g_limit: float
    q_max: float
    g_max: float
    passed: bool
    description: str
    path: str
    

    def summarizeRun(self) -> None:
        data : dict = {"q_limit": self.q_limit,
                  "g_limit": self.g_limit,
                  "q_max": self.q_max,
                  "g_max": self.g_max,
                  "passed": self.passed,
                  "description": self.description}
        self.path = f'runs/Run{dateToString()}'
        createFolder(self.path)

        dataToJson(data, f'{self.path}/summary')

    def __str__(self) -> str:
        return f'{self.q_limit}, {self.g_limit}, {self.q_max}, {self.g_max}, {self.passed}, {self.description}'
    
def extractFromSummaryToRun(run:Run, path:str) -> dict:
        dic: dict
        with open(f'{path}/summary.json', "r") as f:
            dic = json.load(f)
            run.q_limit = dic.get("q_limit", 0)
            run.g_limit = dic.get("g_limit", 0)
            run.q_max = dic.get("q_max", 0)
            run.g_max = dic.get("g_max", 0)
            run.passed = dic.get("passed", False)
            run.description = dic.get("description", "")
        return dic
def extractFromSummary(path :str) -> dict:
    dic: dict
    with open(f'{path}/summary.json', "r") as f:
        dic = json.load(f)
    return dic



def main():
    print("Init")
    run = Run(3,3,33,3,True,"mwahahah ")
    run.summarizeRun()
    input()
    run2 = Run(0,0,0,0,False,"nuuuu")
    extractFromSummaryToRun(run2, run.path)
    print(run2)

    

if __name__ == "__main__":
    main()




