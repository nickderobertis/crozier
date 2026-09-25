

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.scheduled_message import ScheduledMessage


class GetScheduledMessagesResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    scheduled_messages: typing.Optional[typing.List[ScheduledMessage]] = pydantic.Field(default=None)
    """
    Returns all of the current user's undelivered scheduled
    messages, ordered by `scheduled_delivery_timestamp`
    (ascending).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
