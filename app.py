from flask import Flask , render_template
import todo_list

app = Flask(__name__)

@app.route('/')  

def home() :
    my_tasks = todo_list.load_task()

    return render_template('index.html' , tasks = my_tasks)


        # return f"<h1> Web app is running! </h1> <p> You have {len(my_tasks)} tasks. "

if __name__ == "__main__" :
    app.run(debug=True)
