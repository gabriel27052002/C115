from database import Database
from writeAJson import writeAJson
from questionario_crud import QuestionarioCRUDDatabase
from Questionario_CLI import questionarioCLI

db = Database(database="Trabalho_1_C115-L1", collection="Questionario")
questionario_crud = QuestionarioCRUDDatabase(database=db)

questionarioAUX = questionarioCLI(questionario_crud)
questionarioAUX.run()

