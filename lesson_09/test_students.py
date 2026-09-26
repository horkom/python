from student_table import StudentTable


# 🔽 Замените на свои данные!
DB_CONNECTION_STRING = (
    "postgresql://postgres:0909@localhost:5432/qa_lesson"
)

db = StudentTable(DB_CONNECTION_STRING)


def test_add_student():
    first_name = "Иван"
    last_name = "Тестов"
    email = "ivan.test@example.com"

    db.create(first_name, last_name, email)
    new_id = db.get_max_id()

    try:
        rows = db.get_by_id(new_id)

        assert len(rows) == 1
        assert rows[0]["first_name"] == first_name
        assert rows[0]["last_name"] == last_name
        assert rows[0]["email"] == email
    finally:
        db.delete(new_id)


def test_update_student():
    first_name = "Пётр"
    last_name = "Тестов"
    email = "petr.test@example.com"

    db.create(first_name, last_name, email)
    new_id = db.get_max_id()

    new_first_name = "Пётр"
    new_last_name = "Обновлённый"
    new_email = "petr.updated@example.com"

    try:
        db.update(new_id, new_first_name, new_last_name, new_email)

        rows = db.get_by_id(new_id)

        assert len(rows) == 1
        assert rows[0]["first_name"] == new_first_name
        assert rows[0]["last_name"] == new_last_name
        assert rows[0]["email"] == new_email
    finally:
        db.delete(new_id)


def test_delete_student():
    first_name = "Сергей"
    last_name = "Удаляемый"
    email = "sergey.delete@example.com"

    db.create(first_name, last_name, email)
    new_id = db.get_max_id()

    db.delete(new_id)

    rows = db.get_by_id(new_id)

    assert len(rows) == 0
