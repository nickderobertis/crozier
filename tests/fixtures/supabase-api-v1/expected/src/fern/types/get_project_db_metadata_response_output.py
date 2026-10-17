

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_project_db_metadata_response_output_databases_item import GetProjectDbMetadataResponseOutputDatabasesItem


class GetProjectDbMetadataResponseOutput(UniversalBaseModel):
    databases: typing.List[GetProjectDbMetadataResponseOutputDatabasesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
