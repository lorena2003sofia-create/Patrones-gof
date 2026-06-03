# Manual de Pruebas Unitarias - Patrones GoF

## Descripción General

Se implementaron 14 pruebas unitarias correspondientes a los 7 patrones GoF desarrollados en el proyecto Centro de Gestión de Agentes y Canales de Atención. Cada patrón cuenta con dos casos de prueba que permiten verificar su funcionamiento principal.

Las pruebas fueron desarrolladas utilizando el módulo `unittest` de Python.

## Comando de Ejecución

```bash
python3 -m unittest discover -s test -v
```

---

## Detalle de las Pruebas

### Singleton

| # | Prueba                 | Qué verifica                                                  | Resultado esperado                         |
| - | ---------------------- | ------------------------------------------------------------- | ------------------------------------------ |
| 1 | test_unique_instance   | Verifica que DatabaseConnection mantenga una única instancia. | Ambas referencias apuntan al mismo objeto. |
| 2 | test_connection_status | Verifica el estado de la conexión.                            | El estado retornado es "Conectado".        |

### Factory Method

| # | Prueba            | Qué verifica                                    | Resultado esperado                                       |
| - | ----------------- | ----------------------------------------------- | -------------------------------------------------------- |
| 3 | test_create_chat  | Verifica la creación de un agente de tipo Chat. | Se crea correctamente el agente solicitado.              |
| 4 | test_invalid_type | Verifica el manejo de tipos no válidos.         | Se genera la respuesta esperada para un tipo incorrecto. |

### Builder

| # | Prueba              | Qué verifica                                               | Resultado esperado                        |
| - | ------------------- | ---------------------------------------------------------- | ----------------------------------------- |
| 5 | test_create_agent   | Verifica la creación de un agente utilizando AgentBuilder. | El agente se construye correctamente.     |
| 6 | test_assign_channel | Verifica la asignación del canal de atención.              | El canal queda configurado correctamente. |

### Decorator

| # | Prueba                     | Qué verifica                                               | Resultado esperado                            |
| - | -------------------------- | ---------------------------------------------------------- | --------------------------------------------- |
| 7 | test_agent_description     | Verifica la descripción básica del agente.                 | Se muestra la información esperada.           |
| 8 | test_decorator_description | Verifica la información agregada por PerformanceDecorator. | La descripción incluye información adicional. |

### Facade

| #  | Prueba            | Qué verifica                                               | Resultado esperado               |
| -- | ----------------- | ---------------------------------------------------------- | -------------------------------- |
| 9  | test_create_agent | Verifica la creación de agentes mediante CallCenterFacade. | El agente se crea correctamente. |
| 10 | test_list_agents  | Verifica el listado de agentes.                            | Se obtiene la lista esperada.    |

### Command

| #  | Prueba              | Qué verifica                                      | Resultado esperado                     |
| -- | ------------------- | ------------------------------------------------- | -------------------------------------- |
| 11 | test_create_command | Verifica la ejecución del comando de creación.    | La operación se ejecuta correctamente. |
| 12 | test_delete_command | Verifica la ejecución del comando de eliminación. | La operación se ejecuta correctamente. |

### Strategy

| #  | Prueba            | Qué verifica                           | Resultado esperado              |
| -- | ----------------- | -------------------------------------- | ------------------------------- |
| 13 | test_aht_strategy | Verifica el cálculo del indicador AHT. | El valor calculado es correcto. |
| 14 | test_acw_strategy | Verifica el cálculo del indicador ACW. | El valor calculado es correcto. |

---
## Evidencia de Ejecución

```

Resultado obtenido:

```text
test_assign_channel (test_builder.TestBuilder) ... ok
test_create_agent (test_builder.TestBuilder) ... ok
test_create_command (test_command.TestCommand) ... ok
test_delete_command (test_command.TestCommand) ... ok
test_agent_description (test_decorator.TestDecorator) ... ok
test_decorator_description (test_decorator.TestDecorator) ... ok
test_create_agent (test_facade.TestFacade) ... ok
test_list_agents (test_facade.TestFacade) ... ok
test_create_chat (test_factory.TestFactory) ... ok
test_invalid_type (test_factory.TestFactory) ... ok
test_connection_status (test_singleton.TestSingleton) ... ok
test_unique_instance (test_singleton.TestSingleton) ... ok
test_acw_strategy (test_strategy.TestStrategy) ... ok
test_aht_strategy (test_strategy.TestStrategy) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.000s

OK
```

Resumen de resultados:

```text

 OK  Singleton - instancia única
 OK  Singleton - estado de conexión
 OK  Factory Method - creación de agente
 OK  Factory Method - validación de tipo
 OK  Builder - creación de agente
 OK  Builder - asignación de canal
 OK  Decorator - descripción base
 OK  Decorator - información adicional
 OK  Facade - creación de agente
 OK  Facade - listado de agentes
 OK  Command - creación
 OK  Command - eliminación
 OK  Strategy - cálculo AHT
 OK  Strategy - cálculo ACW

```
Todas las pruebas finalizaron correctamente, validando el funcionamiento de los siete patrones implementados en el proyecto.

