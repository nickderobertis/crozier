

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .elastic_metadata import ElasticMetadata
from .project_data_index_with_status_record_properties_value import ProjectDataIndexWithStatusRecordPropertiesValue
from .project_data_index_with_status_schema_key import ProjectDataIndexWithStatusSchemaKey
from .project_data_index_with_status_source import ProjectDataIndexWithStatusSource
from .project_data_index_with_status_view_of import ProjectDataIndexWithStatusViewOf


class ProjectDataIndexWithStatus(UniversalBaseModel):
    source: ProjectDataIndexWithStatusSource
    name: str
    documents: int
    health: str
    status: str
    creation_date: str
    metadata: typing.Optional[ElasticMetadata] = None
    description: str
    schema_key: typing.Optional[ProjectDataIndexWithStatusSchemaKey] = None
    type: str
    view_of: typing.Optional[ProjectDataIndexWithStatusViewOf] = None
    record_properties: typing.Optional[
        typing.Dict[str, typing.Optional[ProjectDataIndexWithStatusRecordPropertiesValue]]
    ] = None
    provenance: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(ProjectDataIndexWithStatus)
