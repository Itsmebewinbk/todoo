from toodoo.model import users,todoo
def login_required(fn):
    def wrapping(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("You must login")
    return wrapping
session={}

def authenicate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user_data=[user for user in users if user["username"]==username and user["password"]==password]
    return user_data
class SignInView:

    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenicate(username=username,password=password)
        if user:
            print("success")
            session["user"]=user[0]

        else:
            print("You must Login")


class ViewAllTodos:
    @login_required
    def get(self,*args,**kwargs):
        return todoo
obj=ViewAllTodos()
print(obj.get())

class CreateNewTodo:
    @login_required
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        todoo.append(kwargs)
        return todoo

create=CreateNewTodo()
(create.post(
    todoId=9,
    task_name="ebill",completed=True
))

class ViewMyTodo:
    @login_required
    def get(self,*args,**kwargs):
        userId=session["user"]["id"]
        print(userId)
        qs=[post for post in todoo if post["userId"]==userId]
        return qs
ob=SignInView()
ob.post(username="anu",password="Password@123")
print(session)

objec=ViewMyTodo()
print(objec.get())



class DetailView:
    def get_obj(self,todo):
        #todoId = kwargs.get("todoId")
        data = [post for post in todoo if post["todoId"] == todo]
        return data
    @login_required
    def get(self,*args,**kwargs):

        todoId=kwargs.get("todoId")
        data=self.get_obj(todoId)
        # data=[post for post in todoo if post["todoId"]==todoId]
        return data
    @login_required
    def remove(self,*args,**kwargs):

        todoId = kwargs.get("todoId")
        data = self.get_obj(todoId)
        # data=[post for post in todoo if post["todoId"]==todoId]
        data=data[0]
        todoo.remove(data)
        return todoo
    @login_required
    def put(self,*args,**kwargs):
        todoId = kwargs.get("todoId")
        instance=self.get_obj(todoId)
        # instance = [post for post in todoo if post["todoId"] == todoId]
        data=kwargs.get("data")
        instance=instance[0]
        instance.update(data)
        return instance

ob=DetailView()
print(ob.get(todoId=5))
print(ob.remove(todoId=5))
data={"title":"Hello There","task_name":"pay the bill","completed":False}
print(ob.put(todoId=1,data=data))

@login_required
def LogOut():
    user=session.pop("user")
    print(f"The user {user['username']} have been logged out")
LogOut()























