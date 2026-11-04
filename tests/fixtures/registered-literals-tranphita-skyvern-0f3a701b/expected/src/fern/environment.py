

import enum


class FernApiEnvironment(enum.Enum):
    PRODUCTION = "https://api.skyvern.com"
    STAGING = "https://api-staging.skyvern.com"
    DEVELOPMENT = "http://localhost:8000"
