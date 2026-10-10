

import enum


class FernApiEnvironment(enum.Enum):
    PRIMARY = "https://passes.groundstation.test"
    FAILOVER = "https://failover.groundstation.test"
