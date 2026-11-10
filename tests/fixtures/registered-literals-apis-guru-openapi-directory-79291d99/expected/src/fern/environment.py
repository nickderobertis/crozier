

import enum


class FernApiEnvironment(enum.Enum):
    PRODUCTION = "https://production.plaid.com"
    SANDBOX = "https://sandbox.plaid.com"
