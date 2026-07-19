

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class TemplatesGetTemplateSnapshotResponseRelationshipsItem(UniversalBaseModel):
    agent_entity_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="agentEntityId"), pydantic.Field(alias="agentEntityId")
    ]
    block_entity_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="blockEntityId"), pydantic.Field(alias="blockEntityId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
