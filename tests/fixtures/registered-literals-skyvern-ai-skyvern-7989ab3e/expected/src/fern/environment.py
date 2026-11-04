

import enum


class FernApiEnvironment(enum.Enum):
    CLOUD = "https://api.skyvern.com"
    STAGING = "https://api-staging.skyvern.com"
    LOCAL = "http://localhost:8000"
