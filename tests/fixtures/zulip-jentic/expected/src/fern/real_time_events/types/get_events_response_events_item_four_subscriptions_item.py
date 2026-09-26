

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetEventsResponseEventsItemFourSubscriptionsItem(UniversalBaseModel):
    """
    Dictionary containing details about the unsubscribed channel.
    """

    stream_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the channel.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the channel.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
