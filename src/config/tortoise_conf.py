from src.config.settings import DATABASE_URI

TORTOISE_ORM = {
    "connections": {"default": DATABASE_URI},
    "apps": {
        "models": {
            "models": ["src.app.user.models", "src.app.auth.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
