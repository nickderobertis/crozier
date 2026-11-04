

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...types.user import User
from .me_get_response_tier import MeGetResponseTier


class MeGetResponse(User):
    """
    Your user information, with tier and email included
    """

    tier: typing.Optional[MeGetResponseTier] = pydantic.Field(default=None)
    """
    Your account tier
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Your email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
