

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagesEventTopicLinksItem(UniversalBaseModel):
    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original link text present in the topic.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expanded target url which the link points to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
