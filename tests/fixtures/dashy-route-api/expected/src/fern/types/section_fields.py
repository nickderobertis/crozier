

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .item import Item


class SectionFields(UniversalBaseModel):
    """
    Any subset of a section's fields (used for PATCH).
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Section heading (unique)
    """

    icon: typing.Optional[str] = pydantic.Field(default=None)
    """
    Section icon
    """

    display_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="displayData"),
        pydantic.Field(alias="displayData", description="Per-section display options"),
    ] = None
    """
    Per-section display options
    """

    items: typing.Optional[typing.List[Item]] = pydantic.Field(default=None)
    """
    The links/apps in this section
    """

    widgets: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    Widgets shown in this section
    """

    filtered_items: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="filteredItems"),
        pydantic.Field(alias="filteredItems", description="Items pulled from another source"),
    ] = None
    """
    Items pulled from another source
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
