

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ProcessVersionValidationResponseDto(UniversalBaseModel):
    process_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="processName"), pydantic.Field(alias="processName")
    ]
    is_latest: typing_extensions.Annotated[bool, FieldMetadata(alias="isLatest"), pydantic.Field(alias="isLatest")]
    local_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="localVersion"), pydantic.Field(alias="localVersion")
    ]
    latest_deployed_version: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="latestDeployedVersion"),
        pydantic.Field(alias="latestDeployedVersion"),
    ] = None
    latest_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="latestVersion"), pydantic.Field(alias="latestVersion")
    ]
    modified_by: typing_extensions.Annotated[str, FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
