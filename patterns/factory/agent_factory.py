class AgentePhone:

    def canal(self):
        return "PHONE"


class AgenteChat:

    def canal(self):
        return "CHAT"


class AgenteEmail:

    def canal(self):
        return "EMAIL"


class AgentFactory:

    @staticmethod
    def crear_agente(tipo):

        if tipo == "PHONE":
            return AgentePhone()

        elif tipo == "CHAT":
            return AgenteChat()

        elif tipo == "EMAIL":
            return AgenteEmail()

        return None