from my_python_project.services.greeter import build_welcome_message

def main() -> None:
    message = build_welcome_message("Tech Lap", role="Laravel & Python Dev")
    print(message)

if __name__ == "__main__":
    main()