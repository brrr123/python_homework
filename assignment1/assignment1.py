#Task 1
def hello():
    return "Hello!"

#Task 2
def greet (name):
    return f"Hello, {name}!"

#Task 3
def calc (a,b, operation="multiply"):
    try:
        match operation:
            case "multiply":
                return a*b
            case "add":
                return a+b
            case "subtract":
                return a-b
            case "divide":
               return a/b
            case "modulo":
                return a%b
            case "int_divide":
                return int(a)/int(b)
            case "power":
                return a**b

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."

#Task 5
def grade (*args):
    try:
        mean = sum(args)/len(args)
        if mean >= 90:
            return "A"
        elif mean >= 80:
            return "B"
        elif mean >= 70:
            return "C"
        elif mean >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

#Task 6
def repeat (string, count):
    output = ""
    for i in range(count):
        output += string
    return output

#Task 7
def student_scores (ops, **kwargs):
        if ops == "mean":
            return sum(kwargs.values())/len(kwargs)
        elif ops == "best":
            return max(kwargs, key=kwargs.get)

#Task 8
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
    return " ".join(words)

#Task 9
def hangman(secret, guess):
    output =""
    for letter in secret:
        if letter in guess:
            output += letter
        else:
            output += "_"
    return output

#Task 10
def pig_latin(input):
    words = input.split()
    vowels = "aeiou"
    output = []
    for word in words:
        qu_pos = word.find("qu")
        if qu_pos != -1:
            output.append(word[qu_pos+2:] + word[:qu_pos+2] + "ay")
        elif word[0] in vowels:
            output.append(word + "ay")
        else:
            for index, char in enumerate(word):
                if char in vowels:
                    output.append(word[index:] + word[:index] + "ay")
                    break
    return " ".join(output)