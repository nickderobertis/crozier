

import enum


class FernApiEnvironment(enum.Enum):
    PRODUCTION = "https://fai.buildwithfern.com"
    DEVELOPMENT = "https://fai-dev.buildwithfern.com"
    LOCAL = "http://localhost:8080"
