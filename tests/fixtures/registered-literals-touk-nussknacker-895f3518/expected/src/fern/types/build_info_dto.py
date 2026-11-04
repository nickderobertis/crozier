

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .map_model_info import MapModelInfo
from .map_string import MapString


class BuildInfoDto(UniversalBaseModel):
    name: str
    git_commit: typing_extensions.Annotated[str, FieldMetadata(alias="gitCommit"), pydantic.Field(alias="gitCommit")]
    build_time: typing_extensions.Annotated[str, FieldMetadata(alias="buildTime"), pydantic.Field(alias="buildTime")]
    version: str
    processing_type: typing_extensions.Annotated[
        MapModelInfo, FieldMetadata(alias="processingType"), pydantic.Field(alias="processingType")
    ]
    global_build_info: typing_extensions.Annotated[
        typing.Optional[MapString], FieldMetadata(alias="globalBuildInfo"), pydantic.Field(alias="globalBuildInfo")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
