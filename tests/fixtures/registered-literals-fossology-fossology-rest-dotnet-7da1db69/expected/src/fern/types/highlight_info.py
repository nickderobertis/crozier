

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .highlight_info_type import HighlightInfoType


class HighlightInfo(UniversalBaseModel):
    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    Start position of the highlight in file
    """

    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    End position of the highlight in file
    """

    type: typing.Optional[HighlightInfoType] = pydantic.Field(default=None)
    """
    Type of highlight
    """

    short_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortName"),
        pydantic.Field(alias="shortName", description="License shortname"),
    ] = None
    """
    License shortname
    """

    ref_start: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="refStart"),
        pydantic.Field(alias="refStart", description="Start of monk diff highlight (relative)"),
    ] = None
    """
    Start of monk diff highlight (relative)
    """

    ref_end: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="refEnd"),
        pydantic.Field(alias="refEnd", description="End of monk diff highlight (relative)"),
    ] = None
    """
    End of monk diff highlight (relative)
    """

    info_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="infoText"),
        pydantic.Field(alias="infoText", description="Tooltip text"),
    ] = None
    """
    Tooltip text
    """

    html_element: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="htmlElement"), pydantic.Field(alias="htmlElement")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
