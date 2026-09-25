

import enum


class FernApiEnvironment(enum.Enum):
    PRODUCTION = "https://paella.billie.io/api/v2"
    SANDBOX = "https://paella-sandbox.billie.io/api/v2"
