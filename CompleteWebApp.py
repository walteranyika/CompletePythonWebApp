from flask import Flask,render_template,request,redirect,url_for, session,flash
from project import *
from user import *
app = Flask(__name__)
#heroku
#
app.secret_key="kjhgfghjkljgjnffnffvrvnkkhhkhvdesjk"


@app.route('/logout')
def logout():
    session.clear()
    return  redirect(url_for("login"))


@app.route('/')
def home():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
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
            session["names"]=x.names
            session["id"]=x.id
            session["logged_in"]=True
            return redirect(url_for('projects'))
        else:
            flash("Wrong username or password")
    return redirect(url_for('login'))


@app.route('/save/<int:id>',methods=['POST'])
def save(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    user_id=session.get("id")
    try:
        project = Project.get(Project.id==id, Project.user_id==user_id)
        if request.method=="POST":
            project.title = request.form['title']
            project.client = request.form['client']
            project.start_date = request.form['start_date']
            project.end_date = request.form['end_date']
            project.desc = request.form['desc']
            project.save()
            flash("Project edited succesfully")
    except:
        flash("Could not edit this project")
    return redirect(url_for("projects"))


@app.route('/edit/<int:id>')
def edit(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    try:
        user_id = session.get("id")
        project = Project.get(Project.id==id, Project.user_id==user_id)
        return render_template("edit.html", project=project)
    except:
        flash("Could not find this project")
        return redirect(url_for("projects"))



@app.route('/delete/<int:id>')
def delete(id):
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    try:
        user_id = session.get("id")
        project = Project.get(Project.id==id, Project.user_id==user_id)
        project.delete_instance()
        flash("Project deleted succesfully")
    except:
        flash("Could not delete the project")
    return redirect(url_for('projects'))

@app.route('/projects')
def projects():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    user_id = session.get("id")
    projects= Project.select().where(Project.user_id==user_id)
    return render_template('projects.html', projects=projects)

@app.route('/new-project')
def newProject():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template('project_form.html')

@app.route('/add', methods=["POST"])
def add():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    if request.method=='POST':
        title= request.form['title']
        client= request.form['client']
        start_date= request.form['start_date']
        end_date= request.form['end_date']
        desc= request.form['desc']
        user_id = session.get("id")
        Project.create(title=title, client=client,  start_date=start_date, end_date=end_date,desc=desc, user_id=user_id)
        flash("Project was added successfully")
    return redirect(url_for("projects"))


if __name__ == '__main__':
    app.run()
