#task 1
def hello():
    return "Hello!"

#task 2

def greet(name):
    return f"Hello, {name}!"

#task 3

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Unknown operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


#task 4

def data_type_conversion(value, type):
    try:
        match type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
            case _:
                return f"Conversion to '{type}' is not supported."
    except ValueError:
        return f"You can't convert {value} into a {type}."

#task 5
def grade(*args):

    try:
        if not args:
            return "Invalid data was provided."
        avg = sum(args) / len(args)
    except Exception:
        return "Invalid data was provided."

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

#task 6
def repeat(string, count):

    new_string = ""
    for i in range(count):
        new_string += string

    return new_string


#task 7
def student_scores(mode, **kwargs):
    if not kwargs:
        return "No scores provided."

    if mode == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif mode == "mean":
        average = sum(kwargs.values()) / len(kwargs)
        return average
    else:
        return "Invalid mode."

#task 8
def titleize(title):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = title.lower().split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in little_words:
            result.append(word)
        else:
            result.append(word.capitalize())

    return ' '.join(result)

#task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

#task 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            i = 0
            while i < len(word):
                if word[i] in vowels or (word[i] == 'q' and i + 1 < len(word) and word[i+1] == 'u'):
                    break
                i += 1
            if word[i:i+2] == "qu":
                i += 2
            result.append(word[i:] + word[:i] + "ay")

    return ' '.join(result)