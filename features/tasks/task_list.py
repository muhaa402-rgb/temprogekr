from typing import List, Dict, Any

def get_task_list(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    if not tasks:
        return {
            "success": True,
            "is_empty": True,
            "message": "Список задач пуст",
            "tasks": []
        }

    formatted_tasks = []
    for task in tasks:
        status_text = "Выполнена" if task.get("completed", False) else "Не выполнена"
        formatted_tasks.append({
            "id": task.get("id"),
            "title": task.get("title"),
            "status": status_text
        })

    return {
        "success": True,
        "is_empty": False,
        "tasks": formatted_tasks
    }


def print_task_list(tasks: List[Dict[str, Any]]) -> None: # соо в кансоль 
    result = get_task_list(tasks)
    if result["is_empty"]:
        print(result["message"])
        return
    for item in result["tasks"]:
        print(f"{item['id']}. {item['title']} — [{item['status']}]")
