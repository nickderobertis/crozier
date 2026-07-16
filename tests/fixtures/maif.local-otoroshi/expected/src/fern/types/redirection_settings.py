

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RedirectionSettings(UniversalBaseModel):
    """
    The configuration for redirection per service
    """

    code: int = pydantic.Field()
    """
    The http redirect code
    """

    enabled: bool = pydantic.Field()
    """
    Whether or not redirection is enabled
    """

    to: str = pydantic.Field()
    """
    The location for redirection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
