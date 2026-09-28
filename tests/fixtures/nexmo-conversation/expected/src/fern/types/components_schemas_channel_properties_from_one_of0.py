

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ComponentsSchemasChannelPropertiesFromOneOf0(UniversalBaseModel):
    """
    Connect to an App User
    """

    type: str = pydantic.Field()
    """
    The type of connection. Must be `app`
    """

    user: str = pydantic.Field()
    """
    The username to connect to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
