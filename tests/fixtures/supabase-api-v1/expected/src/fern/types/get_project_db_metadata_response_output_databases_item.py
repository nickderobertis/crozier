

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_project_db_metadata_response_output_databases_item_schemas_item import (
    GetProjectDbMetadataResponseOutputDatabasesItemSchemasItem,
)


class GetProjectDbMetadataResponseOutputDatabasesItem(UniversalBaseModel):
    name: str
    schemas: typing.List[GetProjectDbMetadataResponseOutputDatabasesItemSchemasItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
