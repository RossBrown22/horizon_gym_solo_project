from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.member_controller import members
from models.fitness_class import FitnessClass
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)