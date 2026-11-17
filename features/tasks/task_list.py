from typing import List, Dict, Any

def get_task_status_text(task: Dict[str, Any]) -> str:
    if "status" in task:
        return task["status"]
    
    is_completed = task.get("completed", False)
    return "Выполнена" if is_completed else "Не выполнена"


def format_task_list(tasks: List[Dict[str, Any]]) -> str: 
    if not tasks:
        return "Список задач пуст"
    lines = []
    for index, task in enumerate(tasks, start=1):
        title = task.get("title", "Без названия")
        status = get_task_status_text(task)
        lines.append(f"{index}. {title} — [{status}]")
    return "\n".join(lines)


def display_tasks(tasks: List[Dict[str, Any]]) -> None: # соо в кансоль 
    output = format_task_list(tasks)
    print(output)

