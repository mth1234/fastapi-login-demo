from argparse import ArgumentParser
from app.db import get_session
from app.db.actions import create_user


def create_admin(args):
    session = next(get_session())
    create_user(args.username, args.password, session, is_admin=True)
    print("Admin created.")


if __name__ == "__main__":
    parser = ArgumentParser(description="CLI to register admin user")
    parser.add_argument("username", type=str)
    parser.add_argument("password", type=str)
    create_admin(parser.parse_args())

