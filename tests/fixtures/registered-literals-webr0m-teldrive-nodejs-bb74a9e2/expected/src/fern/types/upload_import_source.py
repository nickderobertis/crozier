

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .upload_import_source_type import UploadImportSourceType


class UploadImportSource(UniversalBaseModel):
    type: UploadImportSourceType
    path: typing.Optional[str] = None
    url: typing.Optional[str] = None
    headers: typing.Optional[typing.Dict[str, str]] = None
    destination_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="destinationPath"), pydantic.Field(alias="destinationPath")
    ] = None
    exclude: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
