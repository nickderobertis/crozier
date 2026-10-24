

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.api_key import ApiKey


class CreateSubAccountApiKeyResponse(ApiKey):
    secret_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    One-time secret key. Store it immediately. Exact
    successful idempotent replays return the same secret
    during the 5-minute encrypted replay window.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
