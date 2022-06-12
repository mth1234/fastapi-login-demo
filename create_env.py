import pathlib
import os


if __name__ == "__main__":
    root = pathlib.Path(__file__).parent

    env_file = root / ".env"

    if env_file.exists():
        print(".env file already exists. Exiting...")
    else:
        with open(env_file, "w") as f:
            f.write(f"SECRET={os.urandom(24).hex()}")