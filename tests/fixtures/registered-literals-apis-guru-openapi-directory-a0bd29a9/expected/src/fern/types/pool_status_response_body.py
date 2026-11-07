

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PoolStatusResponseBody(UniversalBaseModel):
    all_with_latest_version: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="allWithLatestVersion"), pydantic.Field(alias="allWithLatestVersion")
    ] = None
    is_environment_pool: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isEnvironmentPool"), pydantic.Field(alias="isEnvironmentPool")
    ] = None
    location: typing.Optional[str] = None
    pool_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="poolCode"), pydantic.Field(alias="poolCode")
    ] = None
    ready_unassigned_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="readyUnassignedCount"), pydantic.Field(alias="readyUnassignedCount")
    ] = None
    ready_unassigned_latest_version_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="readyUnassignedLatestVersionCount"),
        pydantic.Field(alias="readyUnassignedLatestVersionCount"),
    ] = None
    ready_unassigned_not_latest_version_and_idle_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="readyUnassignedNotLatestVersionAndIdleCount"),
        pydantic.Field(alias="readyUnassignedNotLatestVersionAndIdleCount"),
    ] = None
    ready_unassigned_not_latest_version_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="readyUnassignedNotLatestVersionCount"),
        pydantic.Field(alias="readyUnassignedNotLatestVersionCount"),
    ] = None
    resource_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="resourceType"), pydantic.Field(alias="resourceType")
    ] = None
    sku: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
