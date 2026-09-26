

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemFreeTextFlags(UniversalBaseModel):
    invisible: bool
    hidden: bool
    print: bool
    no_zoom: typing_extensions.Annotated[bool, FieldMetadata(alias="noZoom"), pydantic.Field(alias="noZoom")]
    no_rotate: typing_extensions.Annotated[bool, FieldMetadata(alias="noRotate"), pydantic.Field(alias="noRotate")]
    no_view: typing_extensions.Annotated[bool, FieldMetadata(alias="noView"), pydantic.Field(alias="noView")]
    read_only: typing_extensions.Annotated[bool, FieldMetadata(alias="readOnly"), pydantic.Field(alias="readOnly")]
    locked: bool
    toggle_no_view: typing_extensions.Annotated[
        bool, FieldMetadata(alias="toggleNoView"), pydantic.Field(alias="toggleNoView")
    ]
    locked_contents: typing_extensions.Annotated[
        bool, FieldMetadata(alias="lockedContents"), pydantic.Field(alias="lockedContents")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
