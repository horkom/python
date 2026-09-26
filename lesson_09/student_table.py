from sqlalchemy import create_engine
from sqlalchemy.sql import text


class StudentTable:
    __scripts = {
        "select": text(
            "SELECT * FROM students"
        ),
        "select_by_id": text(
            "SELECT * FROM students WHERE id = :id"
        ),
        "insert": text(
            "INSERT INTO students (first_name, last_name, email) "
            "VALUES (:first_name, :last_name, :email)"
        ),
        "update": text(
            "UPDATE students SET first_name = :first_name, "
            "last_name = :last_name, email = :email "
            "WHERE id = :id"
        ),
        "delete": text(
            "DELETE FROM students WHERE id = :id"
        ),
        "get_max_id": text(
            "SELECT MAX(id) FROM students"
        ),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_students(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_by_id(self, student_id):
        return self.__db.execute(
            self.__scripts["select_by_id"], id=student_id
        ).fetchall()

    def create(self, first_name, last_name, email):
        self.__db.execute(
            self.__scripts["insert"],
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

    def update(self, student_id, first_name, last_name, email):
        self.__db.execute(
            self.__scripts["update"],
            id=student_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

    def delete(self, student_id):
        self.__db.execute(self.__scripts["delete"], id=student_id)

    def get_max_id(self):
        return self.__db.execute(
            self.__scripts["get_max_id"]
        ).fetchall()[0][0]
