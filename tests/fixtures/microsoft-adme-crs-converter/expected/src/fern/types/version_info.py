

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connected_outer_service import ConnectedOuterService


class VersionInfo(UniversalBaseModel):
    artifact_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="artifactId"), pydantic.Field(alias="artifactId")
    ] = None
    branch: typing.Optional[str] = None
    build_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="buildTime"), pydantic.Field(alias="buildTime")
    ] = None
    commit_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="commitId"), pydantic.Field(alias="commitId")
    ] = None
    commit_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="commitMessage"), pydantic.Field(alias="commitMessage")
    ] = None
    connected_outer_services: typing_extensions.Annotated[
        typing.Optional[typing.List[ConnectedOuterService]],
        FieldMetadata(alias="connectedOuterServices"),
        pydantic.Field(alias="connectedOuterServices"),
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
