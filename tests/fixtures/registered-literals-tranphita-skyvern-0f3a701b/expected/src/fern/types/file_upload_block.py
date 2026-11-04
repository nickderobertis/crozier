

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_storage_type import FileStorageType
from .output_parameter import OutputParameter


class FileUploadBlock(UniversalBaseModel):
    label: str
    output_parameter: OutputParameter
    continue_on_failure: typing.Optional[bool] = None
    model: typing.Optional[typing.Dict[str, typing.Any]] = None
    storage_type: typing.Optional[FileStorageType] = None
    s3bucket: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="s3_bucket"), pydantic.Field(alias="s3_bucket")
    ] = None
    aws_access_key_id: typing.Optional[str] = None
    aws_secret_access_key: typing.Optional[str] = None
    region_name: typing.Optional[str] = None
    path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
