import logging
import functools

# one time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        pos_params = args if args else "none"
        kw_params = kwargs if kwargs else "none"
        result = func(*args, **kwargs)
        log_message = f"function: {func_name}\npositional parameters: {pos_params}\nkeyword parameters: {kw_params}\nreturn: {result}\n"
        logger.log(logging.INFO, log_message)
        
        return result
    return wrapper


@logger_decorator
def hello_world():
    print("Hello, World!")


@logger_decorator
def always_true(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello_world()
    always_true(1, 2, 3, "test")
    return_decorator(name="John", age=30, city="New York")