import unittest

from patterns.command.agent_command import (
    CreateAgentCommand,
    DeleteAgentCommand
)


class TestCommand(unittest.TestCase):

    def test_create_command(self):

        command = CreateAgentCommand()

        self.assertEqual(
            command.execute(),
            "Agente creado"
        )

    def test_delete_command(self):

        command = DeleteAgentCommand()

        self.assertEqual(
            command.execute(),
            "Agente eliminado"
        )


if __name__ == "__main__":
    unittest.main()