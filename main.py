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
    



def dataToJson(data: dict) -> None:
    
    with open("summary.json", "w") as f: 
        json.dump(data, f, indent=4)

def main():
    print("Init")
    run = Run(1,1,1,1,True,"This is second Test")
    data = run.summarizeRun()
    dataToJson(data)


if __name__ == "__main__":
    main()




