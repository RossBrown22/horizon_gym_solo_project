from db.run_sql import run_sql
from models import fitness_class

from models.fitness_class import FitnessClass
from models.member import Member

def save(fitness_class):
    sql = "INSERT INTO fitness_classes(name, type, date, duration) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [fitness_class.name, fitness_class.type, fitness_class.date, fitness_class.duration]
    results = run_sql(sql, values)
    fitness_class.id = results[0]['id']
    return fitness_class


def select_all():
    fitness_classes = []

    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)

    for row in results:
        fitness_class = FitnessClass(row['name'], row['type'], row['date'], row['duration'], row['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes


def select(id):
    fitness_class = None
    sql = "SELECT * FROM fitness_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        fitness_class = FitnessClass(result['name'], result['type'], result['date'], result['duration'], result['id'])
    return fitness_class


def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM fitness_class WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(fitness_class):
    sql = "UPDATE fitness_classes SET (name, type, date, duration = (%s, %s, %s, %s) WHERE id = %s"
    values = [fitness_class.name, fitness_class.type, fitness_class.date, fitness_class.duration, fitness_class.id]
    run_sql(sql, values)


def fitness_classes(member):
    fitness_classes = []

    sql = "SELECT fitness_classes.* FROM fitness_classes INNER JOIN bookings ON bookings.fitness_classes_id = fitness_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        fitness_class = FitnessClass(row['name'], row['type'], row['date'], row['duration'], row['id'])
        fitness_classes.append(fitness_class)

    return fitness_classes

