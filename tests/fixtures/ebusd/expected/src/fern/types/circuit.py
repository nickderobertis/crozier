

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message import Message


class Circuit(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the circuit name.
    """

    zz: typing.Optional[int] = pydantic.Field(default=None)
    """
    the circuit slave address.
    """

    messages: typing.Optional[typing.Dict[str, Message]] = pydantic.Field(default=None)
    """
    the messages with the unique key per circuit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
