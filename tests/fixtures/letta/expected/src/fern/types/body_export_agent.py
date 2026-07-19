

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .agent_file_schema import AgentFileSchema
from .letta_serialize_schemas_pydantic_agent_schema_agent_schema import (
    LettaSerializeSchemasPydanticAgentSchemaAgentSchema,
)


class BodyExportAgent(UniversalBaseModel):
    spec: typing.Optional[AgentFileSchema] = None
    legacy_spec: typing.Optional[LettaSerializeSchemasPydanticAgentSchemaAgentSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
