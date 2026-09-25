

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .check_messages_match_narrow_response_messages_value import CheckMessagesMatchNarrowResponseMessagesValue


class CheckMessagesMatchNarrowResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    messages: typing.Optional[typing.Dict[str, CheckMessagesMatchNarrowResponseMessagesValue]] = pydantic.Field(
        default=None
    )
    """
    A dictionary with a key for each queried message that matches the narrow,
    with message IDs as keys and search rendering data as values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
