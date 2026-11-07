

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UploadCopyrightsItem(UniversalBaseModel):
    copyright: typing.Optional[str] = pydantic.Field(default=None)
    """
    Copyright Information
    """

    file_path: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="filePath"),
        pydantic.Field(
            alias="filePath", description="Path of the files for which the copyright information is provided"
        ),
    ] = None
    """
    Path of the files for which the copyright information is provided
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
