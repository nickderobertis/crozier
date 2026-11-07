

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .repository_token_request_intent import RepositoryTokenRequestIntent


class RepositoryTokenRequest(UniversalBaseModel):
    intent: typing.Optional[RepositoryTokenRequestIntent] = pydantic.Field(default=None)
    """
    Access intent for the vended credentials. Only `read` is
    supported today; `write` and `admin` are reserved for future use.
    """

    ttl_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Requested credential lifetime in seconds. Clamped server-side to
    [60, 3600]. Defaults to 900 (15 minutes) if omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
