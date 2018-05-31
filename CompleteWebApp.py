from flask import Flask,render_template,request,redirect,url_for
from project import *
from user import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")



@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/add-user', methods=["POST"])
def add_user():
    if request.method == "POST":
        names = request.form['names']
        email = request.form['email']
        password = request.form['password']
        User.create(names=names, email=email,password=password)
    return redirect(url_for('login'))

@app.route('/signin', methods=["POST"])
def signin():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        x= User.get(User.email==email, User.password==password)
        if x:
            return redirect(url_for('projects'))
        else:
            pass
    return redirect(url_for('login'))


@app.route('/save/<int:id>',methods=['POST'])
def save(id):
    project = Project.get(Project.id==id)
    if request.method=="POST":
        project.title = request.form['title']
        project.client = request.form['client']
        project.start_date = request.form['start_date']
        project.end_date = request.form['end_date']
        project.desc = request.form['desc']
        project.save()
    return redirect(url_for("projects"))


@app.route('/edit/<int:id>')
def edit(id):
    project = Project.get(Project.id==id)
    return render_template("edit.html", project=project)



@app.route('/delete/<int:id>')
def delete(id):
    project = Project.get(Project.id==id)
    project.delete_instance()
    return redirect(url_for('projects'))

@app.route('/projects')
def projects():
    projects= Project.select()
    return render_template('projects.html', projects=projects)

@app.route('/new-project')
def newProject():
    return render_template('project_form.html')

@app.route('/add', methods=["POST"])
def add():
    if request.method=='POST':
        title= request.form['title']
        client= request.form['client']
        start_date= request.form['start_date']
        end_date= request.form['end_date']
        desc= request.form['desc']
        Project.create(title=title, client=client,  start_date=start_date, end_date=end_date,desc=desc)
    return redirect(url_for("projects"))
if __name__ == '__main__':
    app.run()
