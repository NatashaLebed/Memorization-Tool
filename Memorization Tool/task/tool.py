from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flashcard.db')
Base = declarative_base()


class MyClass(Base):
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    first_column = Column(String)
    second_column = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_cards():
    question, answer = '', ''
    while not question:
        question = input('Question:\n')
    while not answer:
        answer = input('Answer:\n')
    new_data = MyClass(first_column=question, second_column=answer)
    session.add(new_data)
    session.commit()


def practice_cards():
    for card in flashcard:
        print('Question: ' + card.first_column)
        action = input('Please press "y" to see the answer or press "n" to skip:\n')
        if action == 'y':
            print(f'Answer: {card.second_column}')
        elif action == 'n':
            continue
        else:
            print(f'{action} is not an option')


while True:
    print("\n1. Add flashcards\n2. Practice flashcards\n3. Exit")
    choice = input()
    if choice == '1':
        while True:
            action = input("\n1. Add a new flashcard\n2. Exit\n")
            if action == '1':
                add_cards()
            elif action == '2':
                break
            else:
                print(f'{action} is not an option')
    elif choice == '2':
        flashcard = session.query(MyClass).all()
        if len(flashcard) == 0:
            print('There is no flashcard to practice!\n')
        else:
            practice_cards()
    elif choice == '3':
        print('Bye!')
        exit()
    else:
        print(f'{choice} is not an option')

