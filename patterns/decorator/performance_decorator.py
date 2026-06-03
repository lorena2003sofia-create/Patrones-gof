class Agent:

    def get_description(self):
        return "Agente"


class PerformanceDecorator:

    def __init__(self, agent):
        self.agent = agent

    def get_description(self):
        return self.agent.get_description() + " con KPI de desempeño"