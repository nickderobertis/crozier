

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pdf_action_node import PdfActionNode
from .pdf_action_tree_warnings_item import PdfActionTreeWarningsItem


class PdfActionTree(UniversalBaseModel):
    root: typing.Optional[PdfActionNode] = None
    incomplete: bool
    warning_flags: typing_extensions.Annotated[
        int, FieldMetadata(alias="warningFlags"), pydantic.Field(alias="warningFlags")
    ]
    warnings: typing.List[PdfActionTreeWarningsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
