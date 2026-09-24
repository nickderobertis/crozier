

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ui_filter_model import UiFilterModel


class ParsedTableFilter(UniversalBaseModel):
    """
    Model for parsed table filter
    """

    complete_parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[UiFilterModel]],
        FieldMetadata(alias="completeParameters"),
        pydantic.Field(alias="completeParameters"),
    ] = None
    links: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSON query builder links
    """

    needs_offset_update: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="needsOffsetUpdate"),
        pydantic.Field(alias="needsOffsetUpdate", description="Needs offset update (for internal use)"),
    ] = None
    """
    Needs offset update (for internal use)
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    Offset within query
    """

    query_remainder: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="queryRemainder"),
        pydantic.Field(alias="queryRemainder", description="Query remainder"),
    ] = None
    """
    Query remainder
    """

    suggestions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of suggestions
    """

    translate: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Translate (for internal use)
    """

    valid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Query is valid
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
