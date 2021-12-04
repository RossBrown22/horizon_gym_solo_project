from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.member_controller import members
from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)

@fitness_classes_blueprint.route("/classes")
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes = fitness_classes)

@fitness_classes_blueprint.route("/classes/<id>")
def show(id):
    fitness_class = fitness_class_repository.select(id)
    members = member_repository.members(fitness_class)
    return render_template("fitness_classes/show.html", fitness_class=fitness_class, members=members)

@fitness_classes_blueprint.route("/classes/create")
def show_members_create():
    return render_template("create_fitness_classes/index.html")

@fitness_classes_blueprint.route("/classes", methods = ['POST'])
def create_fitness_class():
    name     = request.form['name']
    type     = request.form['type']
    date     = request.form['date']
    duration = request.form['duration']
    new_fitness_class = FitnessClass(name, type, date, duration)
    fitness_class_repository.save(new_fitness_class)
    return redirect("/classes")