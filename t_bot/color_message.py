
def color_return(message: str, color: str) -> str:

    color_code = {
        "green": "\033[32m{}\033[0m",
        "red": "\033[31m{}\033[0m",
        "blue": "\033[34m{}\033[0m"
        }
    return color_code[color].format(message)  