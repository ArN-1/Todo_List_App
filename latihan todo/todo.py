import sqlite3

def create_table():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, status INTEGER NOT NULL)")
    conn.commit()
    conn.close()

def main():
    create_table()

    # Tambahkan logika CRUD (Create, Read, Update, Delete) disini

def create_task(name):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO tasks (name, status) VALUES (?, 0)", (name,))
        conn.commit()
        conn.close()

def read_tasks():
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        tasks = c.fetchall()
        conn.close()
        return tasks

def update_task(task_id, name, status):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE tasks SET name = ?, status = ? WHERE id = ?", (name, status, task_id))
        conn.commit()
        conn.close()

def delete_task(task_id):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    main()
