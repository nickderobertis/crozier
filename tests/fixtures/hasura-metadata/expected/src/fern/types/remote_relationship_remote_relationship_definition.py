

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .remote_relationship_remote_relationship_definition_definition import (
    RemoteRelationshipRemoteRelationshipDefinitionDefinition,
)


class RemoteRelationshipRemoteRelationshipDefinition(UniversalBaseModel):
    definition: RemoteRelationshipRemoteRelationshipDefinitionDefinition
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(RemoteRelationshipRemoteRelationshipDefinition)
