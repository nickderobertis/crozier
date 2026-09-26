

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_widget_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetBlendMode,
)
from .doc_annotations_list200response_annotations_item_widget_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle,
)
from .doc_annotations_list200response_annotations_item_widget_color import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetColor,
)
from .doc_annotations_list200response_annotations_item_widget_field_family import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily,
)
from .doc_annotations_list200response_annotations_item_widget_flags import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetFlags,
)
from .doc_annotations_list200response_annotations_item_widget_font_color import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetFontColor,
)
from .doc_annotations_list200response_annotations_item_widget_font_family import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily,
)
from .doc_annotations_list200response_annotations_item_widget_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_widget_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo,
)
from .doc_annotations_list200response_annotations_item_widget_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetInteriorColor,
)
from .doc_annotations_list200response_annotations_item_widget_page import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetPage,
)
from .doc_annotations_list200response_annotations_item_widget_rect import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRect,
)
from .doc_annotations_list200response_annotations_item_widget_ref import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetRef,
)
from .doc_annotations_list200response_annotations_item_widget_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetReplyType,
)
from .doc_annotations_list200response_annotations_item_widget_text_align import (
    DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemWidget(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemWidgetRef
    page: DocAnnotationsList200ResponseAnnotationsItemWidgetPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemWidgetIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemWidgetFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemWidgetRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemWidgetBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetReplyType],
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
    color: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetColor] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemWidgetBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    font_family: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetFontFamily],
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(alias="fontFamily"),
    ] = None
    font_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")
    ] = None
    font_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemWidgetFontColor],
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ] = None
    text_align: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemWidgetTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    field_family: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily,
        FieldMetadata(alias="fieldFamily"),
        pydantic.Field(alias="fieldFamily"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
