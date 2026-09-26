

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReplyReply(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description that may be added to the interactive options presented (available only on interactive lists).
    """

    id: str = pydantic.Field()
    """
    An identifier to help identify the exact interactive message response.
    """

    title: str = pydantic.Field()
    """
    The title displayed on the interactive option chosen.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
