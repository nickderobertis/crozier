

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubscribeRequestSubscriptionsItem(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    The name of the channel.
    
    Clients should use the `max_stream_name_length` returned by the
    [`POST /register`](/api/register-queue) endpoint to determine
    the maximum channel name length.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [description](/help/change-the-channel-description)
    to use for a new channel being created, in text/markdown format.
    
    See the help center article on [message formatting](/help/format-your-message-using-markdown) for details on Zulip-flavored Markdown.
    
    Clients should use the `max_stream_description_length` returned
    by the [`POST /register`](/api/register-queue) endpoint to
    determine the maximum channel description length.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
