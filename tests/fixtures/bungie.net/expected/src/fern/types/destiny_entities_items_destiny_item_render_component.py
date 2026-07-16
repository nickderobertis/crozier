

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyEntitiesItemsDestinyItemRenderComponent(UniversalBaseModel):
    """
    Many items can be rendered in 3D. When you request this block, you will obtain the custom data needed to render this specific instance of the item.
    """

    art_regions: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]],
        FieldMetadata(alias="artRegions"),
        pydantic.Field(
            alias="artRegions",
            description="A dictionary for rendering gear components, with:\r\nkey = Art Arrangement Region Index\r\nvalue = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.",
        ),
    ] = None
    """
    A dictionary for rendering gear components, with:
    key = Art Arrangement Region Index
    value = The chosen Arrangement Index for the Region, based on the value of a stat on the item used for making the choice.
    """

    use_custom_dyes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="useCustomDyes"),
        pydantic.Field(
            alias="useCustomDyes", description="If you should use custom dyes on this item, it will be indicated here."
        ),
    ] = None
    """
    If you should use custom dyes on this item, it will be indicated here.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
