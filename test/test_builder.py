import unittest

from patterns.builder.agent_builder import AgentBuilder


class TestBuilder(unittest.TestCase):

    def test_create_agent(self):

        agent = (
            AgentBuilder()
            .set_agent_id("CHAT001")
            .set_team_manager("Carlos")
            .set_channel("CHAT")
            .build()
        )

        self.assertEqual(
            agent.agent_id,
            "CHAT001"
        )

    def test_assign_channel(self):

        agent = (
            AgentBuilder()
            .set_channel("EMAIL")
            .build()
        )

        self.assertEqual(
            agent.channel,
            "EMAIL"
        )


if __name__ == "__main__":
    unittest.main()