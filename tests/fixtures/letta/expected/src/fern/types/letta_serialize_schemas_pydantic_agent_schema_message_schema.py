

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .letta_message_content_union import LettaMessageContentUnion


class LettaSerializeSchemasPydanticAgentSchemaMessageSchema(UniversalBaseModel):
    created_at: str
    group_id: typing.Optional[str] = None
    model: typing.Optional[str] = None
    name: typing.Optional[str] = None
    role: str
    content: typing.List[LettaMessageContentUnion]
    tool_call_id: typing.Optional[str] = None
    tool_calls: typing.List[typing.Any]
    tool_returns: typing.List[typing.Any]
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
