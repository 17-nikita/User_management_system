

import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# --- Add project root to sys.path ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# --- Load .env for DATABASE_URL ---
load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))

# --- Alembic Config ---
config = context.config
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL"))

# --- Logging ---
fileConfig(config.config_file_name)

# --- Import Base and models so metadata is populated ---
from core.connections.database import Base

from services.users.profile import models
from services.users import models
# --- Target metadata ---
target_metadata = Base.metadata

# --- Offline / Online migration functions ---
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
