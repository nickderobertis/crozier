

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .findings import Findings


class UploadLicensesItem(UniversalBaseModel):
    file_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="filePath"),
        pydantic.Field(alias="filePath", description="Relative file path"),
    ] = None
    """
    Relative file path
    """

    findings: typing.Optional[Findings] = None
    clearing_status: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
