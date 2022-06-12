from app.db import engine
from app.db.models import Base


def create_tables(_args=None):
    """
    Creates the tables specified in app.db.models

    Args:
        _args: Arguments parsed from the command line when used from the cli
    """
    # Needed for the models to be discovered
    from app.db.models import User, Post  # noqa F401
    print(f"Creating database at: {engine.url}")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()