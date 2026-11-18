

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .page_post_response_data_annotations_annotations_item_block_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes,
)
from .page_post_response_data_annotations_annotations_item_bold_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes,
)
from .page_post_response_data_annotations_annotations_item_code_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes,
)
from .page_post_response_data_annotations_annotations_item_custom_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes,
)
from .page_post_response_data_annotations_annotations_item_highlighting_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes,
)
from .page_post_response_data_annotations_annotations_item_image_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemImageAttributes,
)
from .page_post_response_data_annotations_annotations_item_inline_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes,
)
from .page_post_response_data_annotations_annotations_item_italics_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes,
)
from .page_post_response_data_annotations_annotations_item_link_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes,
)
from .page_post_response_data_annotations_annotations_item_metadata_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes,
)
from .page_post_response_data_annotations_annotations_item_reference_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes,
)
from .page_post_response_data_annotations_annotations_item_strikethrough_attributes import (
    PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes,
)


class PagePostResponseDataAnnotationsAnnotationsItem_Block(UniversalBaseModel):
    type: typing.Literal["block"] = "block"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Metadata(UniversalBaseModel):
    type: typing.Literal["metadata"] = "metadata"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Bold(UniversalBaseModel):
    type: typing.Literal["bold"] = "bold"
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Italics(UniversalBaseModel):
    type: typing.Literal["italics"] = "italics"
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough(UniversalBaseModel):
    type: typing.Literal["strikethrough"] = "strikethrough"
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Highlighting(UniversalBaseModel):
    type: typing.Literal["highlighting"] = "highlighting"
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Inline(UniversalBaseModel):
    type: typing.Literal["inline"] = "inline"
    start: float
    end: float
    attributes: typing.Optional[PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes] = None
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Link(UniversalBaseModel):
    type: typing.Literal["link"] = "link"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Reference(UniversalBaseModel):
    type: typing.Literal["reference"] = "reference"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Image(UniversalBaseModel):
    type: typing.Literal["image"] = "image"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemImageAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Custom(UniversalBaseModel):
    type: typing.Literal["custom"] = "custom"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PagePostResponseDataAnnotationsAnnotationsItem_Code(UniversalBaseModel):
    type: typing.Literal["code"] = "code"
    start: float
    end: float
    attributes: PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes
    app_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, str]]],
        FieldMetadata(alias="appAttributes"),
        pydantic.Field(alias="appAttributes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PagePostResponseDataAnnotationsAnnotationsItem = typing_extensions.Annotated[
    typing.Union[
        PagePostResponseDataAnnotationsAnnotationsItem_Block,
        PagePostResponseDataAnnotationsAnnotationsItem_Metadata,
        PagePostResponseDataAnnotationsAnnotationsItem_Bold,
        PagePostResponseDataAnnotationsAnnotationsItem_Italics,
        PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough,
        PagePostResponseDataAnnotationsAnnotationsItem_Highlighting,
        PagePostResponseDataAnnotationsAnnotationsItem_Inline,
        PagePostResponseDataAnnotationsAnnotationsItem_Link,
        PagePostResponseDataAnnotationsAnnotationsItem_Reference,
        PagePostResponseDataAnnotationsAnnotationsItem_Image,
        PagePostResponseDataAnnotationsAnnotationsItem_Custom,
        PagePostResponseDataAnnotationsAnnotationsItem_Code,
    ],
    pydantic.Field(discriminator="type"),
]
