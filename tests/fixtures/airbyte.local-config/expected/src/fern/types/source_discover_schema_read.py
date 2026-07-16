

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .airbyte_catalog import AirbyteCatalog
from .catalog_diff import CatalogDiff
from .connection_status import ConnectionStatus
from .synchronous_job_read import SynchronousJobRead


class SourceDiscoverSchemaRead(UniversalBaseModel):
    """
    Returns the results of a discover catalog job. If the job was not successful, the catalog field will not be present. jobInfo will aways be present and its status be used to determine if the job was successful or not.
    """

    breaking_change: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="breakingChange"), pydantic.Field(alias="breakingChange")
    ] = None
    catalog: typing.Optional[AirbyteCatalog] = None
    catalog_diff: typing_extensions.Annotated[
        typing.Optional[CatalogDiff], FieldMetadata(alias="catalogDiff"), pydantic.Field(alias="catalogDiff")
    ] = None
    catalog_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="catalogId"), pydantic.Field(alias="catalogId")
    ] = None
    connection_status: typing_extensions.Annotated[
        typing.Optional[ConnectionStatus],
        FieldMetadata(alias="connectionStatus"),
        pydantic.Field(alias="connectionStatus"),
    ] = None
    job_info: typing_extensions.Annotated[
        SynchronousJobRead, FieldMetadata(alias="jobInfo"), pydantic.Field(alias="jobInfo")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
