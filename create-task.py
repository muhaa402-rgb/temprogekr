
tasks = []


def create_task(title: str):
    # Проверяем, что название передано
    if not title or not title.strip():
        return {
            "success": False,
            "error": "Название задачи обязательно"
        }

    # Удаляем лишние пробелы по краям
    title = title.strip()

    # Проверяем длину названия
    if len(title) > 100:
        return {
            "success": False,
            "error": "Название не должно превышать 100 символов"
        }

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)

    return {
        "success": True,
        "task": task
    }
