from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.fitness_class import FitnessClass
from models.member import Member
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

members_blueprint = Blueprint("members", __name__)