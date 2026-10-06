

import enum


class FernApiEnvironment(enum.Enum):
    DEFAULT = "http://${HOST_FOR_SWAGGER}:${APISIX_PORT}"
