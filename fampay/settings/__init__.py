from dotenv import load_dotenv

if load_dotenv("FAMPAY_ENV") == "prod":
    from .prod import *
elif load_dotenv("FAMPAY_ENV") == "staging":
    from .staging import *
else:
    from .dev import *
