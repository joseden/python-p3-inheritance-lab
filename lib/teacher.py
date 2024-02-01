#!/usr/bin/env python

from user import User

import random

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Teacher(User):  # Teacher class inherits from User
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)  # Call User's constructor
        self.knowledge = knowledge  # Store the teacher's knowledge

    def teach(self):
        return random.choice(self.knowledge)  # Randomly select and return a piece of knowledge

        