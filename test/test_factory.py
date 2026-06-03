import unittest

from patterns.factory.agent_factory import AgentFactory


class TestFactory(unittest.TestCase):

    def test_create_chat(self):

        agente = AgentFactory.crear_agente("CHAT")

        self.assertEqual(
            agente.canal(),
            "CHAT"
        )

    def test_invalid_type(self):

        agente = AgentFactory.crear_agente("OTRO")

        self.assertEqual(
            agente,
            None
        )


if __name__ == "__main__":
    unittest.main()