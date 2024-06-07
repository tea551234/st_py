def log_function(fucn):
    def wrapper(*args, **kwargs):
        print(f"function start!")
        print(f"args: {args}")
        ret = fucn(*args, **kwargs)
        print(f"function end!")
        return ret
    return wrapper
@log_function
def fib(n):
    if n<=1: 
        return n
    return fib(n-1)+fib(n-2)
fib(3)