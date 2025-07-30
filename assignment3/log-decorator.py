import logging

logger = logging.getLogger(__name__ + "parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        positional_parameters = args if args else "none"
        keyword_parameters = kwargs if kwargs else "none"
        result = func(*args, **kwargs)

        log_message = (f"function: {func.__name__} positional parameters: {positional_parameters} keyword parameters: "
                       f"{keyword_parameters} return: {result}")

        logger.log(logging.INFO, log_message)
        return result

    return wrapper


@logger_decorator
def print_message():
    print('Hello World!')


@logger_decorator
def argument_function(*args):
    return True


@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator


print_message()
argument_function(1, 2, 3, 4)
keyword_function(name="Chris", pet="Dog")
