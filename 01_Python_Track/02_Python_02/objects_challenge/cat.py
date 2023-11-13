# CHALLENGE #7

class Cat:
    def __init__(self, name, cat_type, color, age, does_run, does_walk, can_meow):
        # Initialize Cat attributes
        self.name = name
        self.cat_type = cat_type
        self.color = color
        self.age = age
        self.does_run = does_run
        self.does_walk = does_walk
        self.can_meow = can_meow

    def _generate_message(self):
        # Generate a common message about the cat
        return f"I am a {self.name}, My color is {self.color}, My age is {self.age}."

    def run(self):
        # Generate a message about running
        result = self._generate_message()
        if self.does_run:
            print(f"{result} and I Can Run With {self.does_run}")
        else:
            print(result + " and sadly I Can't Run")

    def walk(self):
        # Generate a message about walking
        result = self._generate_message()
        if self.does_walk:
            print(f"{result} and I Can Walk With {self.does_walk}")
        else:
            print(result + " and sadly I Can't Walk")

    def meow(self):
        # Generate a message about meowing
        result = self._generate_message()
        if self.can_meow:
            print(result + " and I Can Meow with a lovely voice")
        else:
            print(result + " and sadly I Can't Meow")
