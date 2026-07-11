from fastapi import FastAPI, HTTPException
from database import get_connection
from models import Task

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task API is running"}

#GET TASKS
@app.get("/tasks")
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM task")
    rows = cur.fetchall()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "completed": row[2]
        })

    cur.close()
    conn.close()

    return tasks

#GET TASK BY ID
@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM task WHERE id=%s",
        (task_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": row[0],
        "title": row[1],
        "completed": row[2]
    }

#Create TASKS
@app.post("/tasks")
def create_task(task: Task):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO task(title, is_completed)
        VALUES (%s, %s)
        RETURNING id;
        """,
        (task.title, task.completed)
    )

    task_id = cur.fetchone()[0]

    conn.commit()

    cur.close()
    conn.close()

    return {
        "message": "Task created successfully",
        "id": task_id,
        "title": task.title,
        "is_completed": task.completed
    }

# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE task
        SET title=%s,
            is_completed=%s
        WHERE id=%s
        RETURNING id,title,is_completed
        """,
        (task.title, task.completed, task_id)
    )

    updated = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if updated is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "message": "Task Updated Successfully",
        "task": {
            "id": updated[0],
            "title": updated[1],
            "completed": updated[2]
        }
    }

# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM task
        WHERE id=%s
        RETURNING id
        """,
        (task_id,)
    )

    deleted = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    if deleted is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "message": "Task Deleted Successfully"
    }