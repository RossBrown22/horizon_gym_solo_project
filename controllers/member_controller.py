from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    fitness_classes = fitness_class_repository.fitness_classes(member)
    return render_template("members/show.html", member=member, fitness_classes=fitness_classes)

@members_blueprint.route("/members/create")
def show_members_create():
    return render_template("create_members/index.html")

@members_blueprint.route("/members", methods = ['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name  = request.form['last_name']
    age        = request.form['age']
    new_member = Member(first_name, last_name, age)
    member_repository.save(new_member)
    return redirect("/members")