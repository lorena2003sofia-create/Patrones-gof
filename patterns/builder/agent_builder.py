class Agent:

    def __init__(self):
        self.agent_id = ""
        self.team_manager = ""
        self.channel = ""


class AgentBuilder:

    def __init__(self):
        self.agent = Agent()

    def set_agent_id(self, agent_id):
        self.agent.agent_id = agent_id
        return self

    def set_team_manager(self, manager):
        self.agent.team_manager = manager
        return self

    def set_channel(self, channel):
        self.agent.channel = channel
        return self

    def build(self):
        return self.agent