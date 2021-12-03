import pdb
from models.fitness_class import FitnessClass
from models.member import Member
from models.booking import Booking
import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository


booking_repository.delete_all()
fitness_class_repository.delete_all()
member_repository.delete_all()

member_1 = Member("Arnold", "Schwarzenegger", 28)
member_repository.save(member_1)

member_2 = Member("Lou", "Ferrigno", 24)
member_repository.save(member_2)

member_3 = Member("Franco", "Columbu", 30)
member_repository.save(member_3)

fitness_class_1 = FitnessClass("Clanging Iron", "Body Building", "10/10/1971", 2)
fitness_class_repository.save(fitness_class_1)

fitness_class_2 = FitnessClass("Tough-Time", "Cardio", "15/10/1971", 1)
fitness_class_repository.save(fitness_class_2)

fitness_class_3 = FitnessClass("Wheelie Fun", "Spinning", "16/10/1971", 2)
fitness_class_repository.save(fitness_class_3)

booking_1 = Booking(member_1, fitness_class_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_1, fitness_class_2)
booking_repository.save(booking_2)

booking_3 = Booking(member_2, fitness_class_3)
booking_repository.save(booking_3)

booking_4 = Booking(member_3, fitness_class_2)
booking_repository.save(booking_4)