import os
from dotenv import load_dotenv
from my_python_project.services.greeter import build_welcome_message

# Load environment variables first
load_dotenv()

# Define main execution logic
def main() -> None:
    app_name = os.getenv("APP_NAME", "Default API")
    print(f"starting {app_name}...")
    
    message = build_welcome_message("Tech Lap", role="Laravel & Python Dev")
    print(message)

# Entry point trigger at the bottom
if __name__ == "__main__":
    main()
