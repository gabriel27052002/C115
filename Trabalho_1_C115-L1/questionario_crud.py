from pymongo import MongoClient
from bson.objectid import ObjectId

class QuestionarioCRUDDatabase:
    def __init__(self, database):
        self.db = database

    def create_questionario(self, pergunta, altenativaA, altenativaB, altenativaC, altenativaD, resposta):
        try:
            res = self.db.collection.insert_one({"pergunta": pergunta, "alternativaA": altenativaA, "alternativaB": altenativaB, "alternativaC": altenativaC, "alternativaD": altenativaD, "resposta": resposta})
            print(f"Questionario created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating questionario: {e}")
            return None

    def read_questionario_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Questionario found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading questionario: {e}")
            return None
    
    def update_questionario(self, id: str, pergunta, altenativaA, altenativaB, altenativaC, altenativaD, resposta):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"pergunta": pergunta, "alternativaA": altenativaA, "alternativaB": altenativaB, "alternativaC": altenativaC, "alternativaD": altenativaD, "resposta": resposta}})
            print(f"Questionario updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating questionario: {e}")
            return None

    def delete_questionario(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Questionario deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting questionario: {e}")
            return None
