

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_ink_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemInkBlendMode,
)
from .doc_annotations_list200response_annotations_item_ink_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemInkBorderStyle,
)
from .doc_annotations_list200response_annotations_item_ink_color import (
    DocAnnotationsList200ResponseAnnotationsItemInkColor,
)
from .doc_annotations_list200response_annotations_item_ink_flags import (
    DocAnnotationsList200ResponseAnnotationsItemInkFlags,
)
from .doc_annotations_list200response_annotations_item_ink_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemInkIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_ink_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo,
)
from .doc_annotations_list200response_annotations_item_ink_ink_list_item_item import (
    DocAnnotationsList200ResponseAnnotationsItemInkInkListItemItem,
)
from .doc_annotations_list200response_annotations_item_ink_intent import (
    DocAnnotationsList200ResponseAnnotationsItemInkIntent,
)
from .doc_annotations_list200response_annotations_item_ink_page import (
    DocAnnotationsList200ResponseAnnotationsItemInkPage,
)
from .doc_annotations_list200response_annotations_item_ink_rect import (
    DocAnnotationsList200ResponseAnnotationsItemInkRect,
)
from .doc_annotations_list200response_annotations_item_ink_ref import DocAnnotationsList200ResponseAnnotationsItemInkRef
from .doc_annotations_list200response_annotations_item_ink_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemInkReplyType,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemInk(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemInkRef
    page: DocAnnotationsList200ResponseAnnotationsItemInkPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemInkIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemInkFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemInkRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemInkBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemInkInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemInkReplyType],
        FieldMetadata(alias="replyType"),
        pydantic.Field(alias="replyType"),
    ] = None
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="groupId"), pydantic.Field(alias="groupId")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    actions: typing.Optional[PdfAnnotationActions] = None
    color: DocAnnotationsList200ResponseAnnotationsItemInkColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemInkBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemInkIntent] = None
    ink_list: typing_extensions.Annotated[
        typing.List[typing.List[DocAnnotationsList200ResponseAnnotationsItemInkInkListItemItem]],
        FieldMetadata(alias="inkList"),
        pydantic.Field(alias="inkList"),
    ]
    rotation: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
