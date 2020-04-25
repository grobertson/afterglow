import os

class Production():
    SECRET_KEY = os.getenv("AFTERGLOW_SECRET_KEY", "secret")

class Development():
    SECRET_KEY = os.getenv("AFTERGLOW_SECRET_KEY", "secret")
    PORT = os.getenv("AFTERGLOW_PORT", "18181")
    DB_SCHEMA = os.getenv("AFTERGLOW_DB_SCHEMA", "afterglow")
    DB_USER = os.getenv("AFTERGLOW_DB_USER", "afterglow")
    DB_PASSWORD = os.getenv("AFTERGLOW_DB_PASSWORD", "afterglow")
    DAEMONIZE = bool(os.getenv("AFTERGLOW_DAEMONIZE", False))
    SAFE_MODE = bool(os.getenv("AFTERGLOW_", True))
    LOG_LEVEL = os.getenv("AFTERGLOW_LOG_LEVEL", "debug")
    CONFIG_FILE = os.getenv("AFTERGLOW_CONFIG_FILE", "/etc/afterglow/afterglow.yaml")
    RULES_DIRECTORY = os.getenv("AFTERGLOW_RULES", "/etc/afterglow/rules.d/")
    # = os.getenv("AFTERGLOW_", "")
    

config = {
    "production": Production,
    "development": Development
}
