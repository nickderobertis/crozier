

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .brand_bug_input_background_style import BrandBugInputBackgroundStyle
from .brand_bug_input_corner import BrandBugInputCorner
from .brand_bug_input_target_scope import BrandBugInputTargetScope


class BrandBugInput(UniversalBaseModel):
    """
    A mark needs a logo image, text, or both. Sizes are percentages of the screen so one instance reads the same at any panel resolution.
    """

    name: str
    corner: BrandBugInputCorner
    image_asset_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageAssetId"),
        pydantic.Field(alias="imageAssetId", description="A ready image in the Media library."),
    ] = None
    """
    A ready image in the Media library.
    """

    text: str
    width_percent: typing_extensions.Annotated[
        int, FieldMetadata(alias="widthPercent"), pydantic.Field(alias="widthPercent")
    ]
    text_size_percent: typing_extensions.Annotated[
        int, FieldMetadata(alias="textSizePercent"), pydantic.Field(alias="textSizePercent")
    ]
    opacity_percent: typing_extensions.Annotated[
        int, FieldMetadata(alias="opacityPercent"), pydantic.Field(alias="opacityPercent")
    ]
    margin_percent: typing_extensions.Annotated[
        int, FieldMetadata(alias="marginPercent"), pydantic.Field(alias="marginPercent")
    ]
    text_color: typing_extensions.Annotated[str, FieldMetadata(alias="textColor"), pydantic.Field(alias="textColor")]
    background_style: typing_extensions.Annotated[
        BrandBugInputBackgroundStyle, FieldMetadata(alias="backgroundStyle"), pydantic.Field(alias="backgroundStyle")
    ]
    starts_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startsAt"), pydantic.Field(alias="startsAt")
    ] = None
    ends_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="endsAt"), pydantic.Field(alias="endsAt")
    ] = None
    enabled: bool
    priority: int
    target_scope: typing_extensions.Annotated[
        BrandBugInputTargetScope, FieldMetadata(alias="targetScope"), pydantic.Field(alias="targetScope")
    ]
    target_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="targetIds"), pydantic.Field(alias="targetIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
