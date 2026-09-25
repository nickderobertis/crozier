

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_message_history_response_message_history_item import GetMessageHistoryResponseMessageHistoryItem


class GetMessageHistoryResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    message_history: typing.Optional[typing.List[GetMessageHistoryResponseMessageHistoryItem]] = pydantic.Field(
        default=None
    )
    """
    A chronologically sorted, oldest to newest, array
    of `snapshot` objects, each one with the values of
    the message after the edit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
