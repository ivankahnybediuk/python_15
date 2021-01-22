from functools import wraps

"""
Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
 passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a
 valid email string
Email validations:
https://help.xmatters.com/ondemand/trial/valid_email_format.htm
https://en.wikipedia.org/wiki/Email_address
# """
class Email():
    def __init__(self):
        self.__validate = " "

    @property
    def validate(self):
        return self.__validate

    @validate.setter
    def validate(self, mail):
        if "@" in mail:
            prefix = mail.split("@")[0]
            domain = mail.split("@")[1]


            def prefix_check():
                if len(prefix) > 0 and prefix[-1].isalpha() or prefix[-1].isdigit(): return True

            def domain_check():
                symbols = list(domain)
                for i in symbols:
                    if i.isalpha() or i.isdigit() or i == "-":
                        continue
                    elif i == ".":
                        if domain.count(".") != 1:
                            raise ValueError("Недопустимое значение")
                        elif domain.count(".") == 1 and len(domain.split(".")[1]) >= 2:
                            continue
                        else:
                            raise ValueError("Недопустимое значение")
                    else:
                        raise ValueError("Недопустимое значение")
                return True

            if prefix_check() and domain_check():
                self.__validate = mail
            else:
                raise ValueError("Недопустимое значение")
        else:
            raise ValueError("Недопустимое значение")


if __name__ == "__main__":
    pr = Email()
    print(pr.validate)
    pr.validate = 'ianna@gmail.com'
    print(pr.validate)


"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers. 
You should implement a method that allows you to add workers to 
a Boss. You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters 
and setters instead!
You can refactor the existing code.
"""

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []
    def __str__(self):
        if self.workers:
            for i in self.workers:
                return (self.name + " " + i.name)
        else:
            return ("У"+self.name+"нет работников")

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.__boss = boss
        self.__boss.workers.append(self)

    @property
    def boss(self):
        return self.__boss
    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            new_boss.workers.append(self)
            self.__boss.workers.remove(self)
            self.__boss = new_boss
        else:
            raise ValueError("Недопустимое значение")

if __name__ == "__main__":
    boss1 = Boss(1, "Василий", "Компания А")
    boss2 = Boss(2, "Галина", "Компания Б")
    worker = Worker(1, "Ivan", "Компания", boss1)
    print("Босса зовут - " + worker.boss.name)
    print(boss1)
    print(boss2)
    worker.boss = boss2
    print("Босса зовут - " + worker.boss.name)
    print(boss1)
    print(boss2)

"""
Task 3

Write a class TypeDecorators which has several methods for converting results of functions to a 
specified type (if it's possible):
methods:
to_int
to_str
to_bool
to_float
Don't forget to use @wraps
```
class TypeDecorators:
    pass
@TypeDecorators.to_int
def do_nothing(string: str):
    return string
@TypeDecorators.to_bool
def do_something(string: str):
    return string
assert do_nothing('25') == 25
assert do_something('True') is True
"""
class TypeDecorators:
    def to_int(func):
        @wraps(func)
        def wrapper(arg):
            try:
               arg = int(arg)
            except ValueError:
                print("НЕвозможно выполнить")
                return
            return arg
        return wrapper
    def to_str(func):
        @wraps(func)
        def wrapper(arg):
            try:
               arg =  str(arg)
            except ValueError:
                print("НЕвозможно выполнить")
                return
            return arg
        return wrapper
    def to_bool(func):
        @wraps(func)
        def wrapper(arg):
            try:
               arg =  bool(arg)
            except ValueError:
                print("НЕвозможно выполнить")
                return
            return arg
        return wrapper
    def to_float(func):
        @wraps(func)
        def wrapper(arg):
            if arg.lower() == "true":
                arg = True
            else:
                arg = False
            return arg
        return wrapper

@TypeDecorators.to_int
def do_something(string: str):
    return string



print(type(do_something("0")))
print(do_something("hh"))