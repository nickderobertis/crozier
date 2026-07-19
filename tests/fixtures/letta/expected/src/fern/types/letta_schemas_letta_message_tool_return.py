

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_schemas_letta_message_tool_return_status import LettaSchemasLettaMessageToolReturnStatus
from .letta_schemas_letta_message_tool_return_tool_return import LettaSchemasLettaMessageToolReturnToolReturn
from .letta_schemas_letta_message_tool_return_type import LettaSchemasLettaMessageToolReturnType


class LettaSchemasLettaMessageToolReturn(UniversalBaseModel):
    type: typing.Optional[LettaSchemasLettaMessageToolReturnType] = pydantic.Field(default=None)
    """
    The message type to be created.
    """

    tool_return: LettaSchemasLettaMessageToolReturnToolReturn = pydantic.Field()
    """
    The tool return value - either a string or list of content parts (text/image)
    """

    status: LettaSchemasLettaMessageToolReturnStatus
    tool_call_id: str
    stdout: typing.Optional[typing.List[str]] = None
    stderr: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
