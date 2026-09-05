

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_metadata_get_custom_value import ProjectMetadataGetCustomValue


class ProjectMetadataGet(UniversalBaseModel):
    project_uuid: typing_extensions.Annotated[
        str, FieldMetadata(alias="projectUuid"), pydantic.Field(alias="projectUuid")
    ]
    custom: typing.Optional[typing.Dict[str, ProjectMetadataGetCustomValue]] = pydantic.Field(default=None)
    """
    Custom key-value map
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
