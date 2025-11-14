import os

# The container's primary function (prints the greeting to stdout)
def run_app():
    # Retrieve the NAME environment variable set in the Dockerfile
    name = os.environ.get("NAME", "World")
    
    # Print a confirmation message. This output goes to ECS/CloudWatch Logs.
    print(f"Hello, {name} from the automated ECS pipeline!")
    print("Application logic executed successfully.")

# Run the function when the script starts
if __name__ == "__main__":
    run_app()