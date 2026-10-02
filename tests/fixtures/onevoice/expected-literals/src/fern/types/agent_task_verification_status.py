

import typing

AgentTaskVerificationStatus = typing.Union[
    typing.Literal["pending", "running", "verified", "mismatch", "unverifiable", "error", "unsupported"], typing.Any
]
