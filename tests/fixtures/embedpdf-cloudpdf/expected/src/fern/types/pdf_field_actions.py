

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_tree import PdfActionTree


class PdfFieldActions(UniversalBaseModel):
    keystroke: typing.Optional[PdfActionTree] = None
    format: typing.Optional[PdfActionTree] = None
    validate_: typing_extensions.Annotated[
        typing.Optional[PdfActionTree], FieldMetadata(alias="validate"), pydantic.Field(alias="validate")
    ] = None
    calculate: typing.Optional[PdfActionTree] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
