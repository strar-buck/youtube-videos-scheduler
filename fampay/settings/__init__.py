import os

if os.environ.get("FAMPAY_ENV") == "prod":
    from .prod import *
elif os.environ.get("FAMPAY_ENV") == "staging":
    from .staging import *
else:
    from .dev import *
