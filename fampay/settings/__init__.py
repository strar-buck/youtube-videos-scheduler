from decouple import config

if config("FAMPAY_ENV") == "prod":
    from .prod import *
elif config("FAMPAY_ENV") == "staging":
    from .staging import *
else:
    from .dev import *
