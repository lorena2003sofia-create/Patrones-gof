import unittest

from patterns.decorator.performance_decorator import (
    Agent,
    PerformanceDecorator
)


class TestDecorator(unittest.TestCase):

    def test_agent_description(self):

        agent = Agent()

        self.assertEqual(
            agent.get_description(),
            "Agente"
        )

    def test_decorator_description(self):

        agent = Agent()

        decorated = PerformanceDecorator(agent)

        self.assertEqual(
            decorated.get_description(),
            "Agente con KPI de desempeño"
        )


if __name__ == "__main__":
    unittest.main()