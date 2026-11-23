

import enum


class FernApiEnvironment(enum.Enum):
    PRODUCTION = "https://api.runtime.example.com"
    SANDBOX = "https://sandbox.runtime.example.com"
