import json
import os

FILE_NAME = "todo_list.json"

def load_task() :
    # Check if the file exists

    if os.path.exists(FILE_NAME) :
        with open(FILE_NAME , "r") as file :
            return json.load(file)

    else :
         return[]  # Return an empty list if no file exists .


    #  Core Function for adding and saving .
def save_tasks(tasks) :
    with open(FILE_NAME , "w") as file:
        json.dump(tasks , file , indent= 3)

def add_task(tasks_list) :

    task_name = input("What do you need to do : ")

    new_task = {
        "name" : task_name , 
        "status" : "pending"
    }       
    tasks_list.append(new_task)
    save_tasks(tasks_list)
    print(f"Added Task : {task_name} . ")

    # Viewing saved task.....

def view_task(tasks_list) :
    print("===TO Do List===")
    if len(tasks_list) == 0 :
        print("You Don't have any task yet . ")
    else :
        for index , task in enumerate(tasks_list) :
            print(f" {index + 1}. {task['name']} - [{task['status']}]")

    print("---" * 30)

      # Controle Flow----

def main() :
        my_tasks = load_task()

      # Keep running loop while execution usin while .....

        while True :
          print("\n 1. Add a Task . ") 
          print("\n 2. View Tasks . ") 
          print("\n 3. Quite . ")

          choice = input("Choose an option ( 1 / 2 / 3 ) : ")

          if choice == "1" :
              add_task(my_tasks)
          elif choice == "2" :
              view_task(my_tasks)
          elif choice == "3" :
              print("Good Bye ")
              break        # this stop the loop 
          else :
              print("Invalid Input , Please try again...")

if __name__ == "__main__" :
    main() 


            

        