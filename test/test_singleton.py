import unittest

from patterns.singleton.database import DatabaseConnection


class TestSingleton(unittest.TestCase):

    def test_unique_instance(self):
        conexion1 = DatabaseConnection()
        conexion2 = DatabaseConnection()

        self.assertIs(conexion1, conexion2)

    def test_connection_status(self):
        conexion = DatabaseConnection()

        self.assertEqual(
            conexion.get_status(),
            "Conectado"
        )


if __name__ == "__main__":
    unittest.main()