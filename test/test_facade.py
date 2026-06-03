import unittest

from patterns.facade.callcenter_facade import CallCenterFacade


class TestFacade(unittest.TestCase):

    def test_create_agent(self):

        facade = CallCenterFacade()

        self.assertEqual(
            facade.create_agent(),
            "Agente creado"
        )

    def test_list_agents(self):

        facade = CallCenterFacade()

        self.assertEqual(
            facade.list_agents(),
            "Lista de agentes"
        )


if __name__ == "__main__":
    unittest.main()