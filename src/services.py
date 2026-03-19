tasks=[]
def create_task():  
    title=input("ingrese un titulo: ")
    description=input("ingrese la descripcion: ")
    priority=input("ingrese la prioridad: ")
    status="por hacer"
        
    tasks.append({"title":title,"description":description,"priority":priority,"status":status})    
    for i in tasks:
        print(f"the task {i["title"]} it was crated correctly")
    return tasks
def show_task():
    print("\n---tasks---")
    for i,t in enumerate(tasks):
        print(f"{i+1}. {t["title"]}\nthe description are : {t["description"]}\nwith priority: {t["priority"]} and status: {t["status"]}")



print(create_task())
print(show_task())