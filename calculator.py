import math

# Define allowed names from math module
allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}

# Add some extra built-ins
allowed_names.update({
    'abs': abs,
    'round': round,
    'log': math.log,
    'log10': math.log10
})

def advanced_calculator():
    print("Advanced Calculator (type 'exit' to quit)")
    print("Supported functions: +, -, *, /, %, **, sin, cos, tan, sqrt, factorial, exp, pi, e, abs, round, log, log10")
    
    while True:
        expr = input(">>> ")
        if expr.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            # Evaluate the expression safely
            result = eval(expr, {"__builtins__": {}}, allowed_names)
            print("= ", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    advanced_calculator()
