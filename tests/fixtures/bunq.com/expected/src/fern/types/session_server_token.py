

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionServerToken(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the Token.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Session token is the token the client has to provide in the "X-Bunq-Client-Authentication" header for each API call that requires a Session (only the creation of a Installation and DeviceServer don't require a Session).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
