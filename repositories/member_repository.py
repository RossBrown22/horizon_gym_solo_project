from db.run_sql import run_sql
from models.fitness_class import FitnessClass
from models.member import Member

def save(member):
    sql = "INSERT INTO members(first_name, last_name, age) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['id'])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['first_name'], result['last_name'], result['age'], result['id'])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM member WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (first_name, last_name, age) = (%s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.id]
    run_sql(sql, values)

