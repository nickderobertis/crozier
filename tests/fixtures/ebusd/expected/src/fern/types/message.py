

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field import Field
from .field_def import FieldDef
from .message_condition import MessageCondition
from .message_id import MessageId
from .seconds import Seconds
from .symbol import Symbol
from .symbols import Symbols


class Message(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    the message name.
    """

    passive: bool = pydantic.Field()
    """
    true when this is a passive message.
    """

    write: bool = pydantic.Field()
    """
    true for a write message, false for a read message.
    """

    level: typing.Optional[str] = pydantic.Field(default=None)
    """
    the access level for the message (only with full).
    """

    pollprio: typing.Optional[int] = pydantic.Field(default=None)
    """
    the poll priority of the message (only with full).
    """

    condition: typing.Optional[MessageCondition] = pydantic.Field(default=None)
    """
    the condition(s) in case of a conditional message (only with full).
    """

    lastup: Seconds = pydantic.Field()
    """
    the time in UTC seconds of the last update of the message (0 for never).
    """

    qq: typing.Optional[Symbol] = pydantic.Field(default=None)
    """
    limited source master address (only with def or data).
    """

    zz: typing.Optional[Symbol] = pydantic.Field(default=None)
    """
    destination master or slave address.
    """

    id: typing.Optional[MessageId] = pydantic.Field(default=None)
    """
    the message ID composed of PBSB and further master data bytes (only with def), or an array thereof in case of a chained message.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    the message comment (only with verbose).
    """

    master: typing.Optional[Symbols] = pydantic.Field(default=None)
    """
    the last seen master data bytes (only with raw and if available).
    """

    slave: typing.Optional[Symbols] = pydantic.Field(default=None)
    """
    the last seen slave data bytes (only with raw and if available).
    """

    fields: typing.Optional[typing.Dict[str, Field]] = pydantic.Field(default=None)
    """
    the decoded fields the message is composed of (only if available).
    """

    decodeerror: typing.Optional[str] = pydantic.Field(default=None)
    """
    set to the error message instead of fields in case of a decoding error.
    """

    fielddefs: typing.Optional[typing.List[FieldDef]] = pydantic.Field(default=None)
    """
    the field definitions the message is composed of (only with def).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
