

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatedGroup(UniversalBaseModel):
    """
    A successfully created group chat.
    """

    id: str = pydantic.Field()
    """
    The internal chat ID of the created group.
    """

    mxid: str = pydantic.Field()
    """
    The Matrix room ID of the portal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
