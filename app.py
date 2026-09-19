from flask import Flask, render_template, request, redirect, url_for
import todo_list

app = Flask(__name__)

@app.route("/")
def home():
    my_tasks = todo_list.load_task()
    return render_template("index.html", tasks=my_tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_name = request.form.get("task_name")
    if task_name and task_name.strip():
        tasks = todo_list.load_task()
        todo_list.add_task(tasks, task_name.strip())
    return redirect(url_for("home"))

@app.route("/delete/<int:index>", methods=["POST"])
def delete_task(index):
    tasks = todo_list.load_task()
    todo_list.delete_task(tasks, index)
    return redirect(url_for("home"))

@app.route("/complete/<int:index>", methods=["POST"])
def complete_task(index):
    tasks = todo_list.load_task()
    todo_list.complete_task(tasks, index)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)