

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .send_input import SendInput


class Send(UniversalBaseModel):
    """
    A message to send to a node.
    """

    node: str = pydantic.Field()
    """
    The node to send the message to.
    """

    input: typing.Optional[SendInput] = pydantic.Field(default=None)
    """
    The message to send.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
