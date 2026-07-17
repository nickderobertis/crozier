

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_config_type import JobConfigType
from .job_id import JobId
from .job_status import JobStatus
from .reset_config import ResetConfig


class JobRead(UniversalBaseModel):
    config_id: typing_extensions.Annotated[str, FieldMetadata(alias="configId"), pydantic.Field(alias="configId")]
    config_type: typing_extensions.Annotated[
        JobConfigType, FieldMetadata(alias="configType"), pydantic.Field(alias="configType")
    ]
    created_at: typing_extensions.Annotated[int, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    id: JobId
    reset_config: typing_extensions.Annotated[
        typing.Optional[ResetConfig], FieldMetadata(alias="resetConfig"), pydantic.Field(alias="resetConfig")
    ] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    status: JobStatus
    updated_at: typing_extensions.Annotated[int, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
