TORTOISE_ORM = {
    "connections": {"default": "postgres://postgres:123456@localhost:5432/useful_test_tortoise"},
    "apps": {
        "models": {
            "models": ["src.app.user.models", "src.app.auth.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
