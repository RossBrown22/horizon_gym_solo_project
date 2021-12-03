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