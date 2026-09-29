

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .graph_ql_name import GraphQlName
from .remote_relationship_remote_relationship_definition import RemoteRelationshipRemoteRelationshipDefinition


class RemoteSchemaMetadataRemoteRelationshipDefinition(UniversalBaseModel):
    relationships: typing.Optional[typing.List[RemoteRelationshipRemoteRelationshipDefinition]] = None
    type_name: GraphQlName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(RemoteSchemaMetadataRemoteRelationshipDefinition)
