import json

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
    
    def summarizeRun(self) -> dict:
        data = {"q_limit": self.q_limit,
                  "g_limit": self.g_limit,
                  "q_max": self.q_max,
                  "g_max": self.g_max,
                  "passed": self.passed,
                  "description": self.description}
        return data
    def extractFromSummary(self) -> None:
        dic: dict
        with open("summary.json", "r") as f:
            dic = json.load(f)
            self.q_limit = dic.get("q_limit", 0)
            self.g_limit = dic.get("g_limit", 0)
            self.q_max = dic.get("q_max", 0)
            self.g_max = dic.get("g_max", 0)
            self.passed = dic.get("passed", False)
            self.description = dic.get("description", "")
    def __str__(self) -> str:
        return f'{self.q_limit}, {self.g_limit}, {self.q_max}, {self.g_max}, {self.passed}, {self.description}'


def dataToJson(data: dict) -> None:
    
    with open("summary.json", "w") as f: 
        json.dump(data, f, indent=4)

def main():
    print("Init")
    run = Run(1,1,1,1,True,"This is second Test")
    data = run.summarizeRun()
    dataToJson(data)
    run2 = Run(0,0,0,0,False, "")
    run2.extractFromSummary()
    print(run2)

if __name__ == "__main__":
    main()




