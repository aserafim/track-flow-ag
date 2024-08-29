Diagrama de classes do Projeto

+----------------+        1              *        +----------------+
|    Cliente     |<--------------------------------|    Projeto    |
+----------------+                                 +----------------+
| - id: int      |                                 | - id: int      |
| - nome: str    |                                 | - nome: str    |
+----------------+                                 | - cliente_id: int|
                                                   +----------------+
                                                         1   |
                                                             |
                                                             |
                                                             |  *
                                                   +----------------+
                                                   |   Atividade    |
                                                   +----------------+
                                                   | - id: int      |
                                                   | - descricao: str|
                                                   | - projeto_id: int|
                                                   +----------------+
