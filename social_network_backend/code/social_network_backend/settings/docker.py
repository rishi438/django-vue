if IS_DOCKER:  # noqa: F821 # type: ignore #nosec
    assert MIDDLEWARE[:1] == [  # noqa: F821 # type: ignore #nosec
        "django.middleware.security.SecurityMiddleware"
    ]
