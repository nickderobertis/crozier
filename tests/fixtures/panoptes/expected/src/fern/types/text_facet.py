

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TextFacet(UniversalBaseModel):
    property: typing.Optional[str] = pydantic.Field(default=None)
    """
    Property which this searches in.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human readable name of the facet.
    """

    start_open: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="startOpen"),
        pydantic.Field(alias="startOpen", description="Whether this facet should be expanded initially"),
    ] = None
    """
    Whether this facet should be expanded initially
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
