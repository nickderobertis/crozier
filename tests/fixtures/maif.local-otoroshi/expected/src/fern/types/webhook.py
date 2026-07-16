

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Webhook(UniversalBaseModel):
    """
    A callback URL where events are posted
    """

    headers: typing.Dict[str, str] = pydantic.Field()
    """
    Headers to authorize the call or whatever
    """

    url: str = pydantic.Field()
    """
    The URL where events are posted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
