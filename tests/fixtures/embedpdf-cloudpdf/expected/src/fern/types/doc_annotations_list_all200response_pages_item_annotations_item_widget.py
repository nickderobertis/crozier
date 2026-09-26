

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_border_style import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetBorderStyle,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_field_family import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_font_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFontColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_font_family import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFontFamily,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_widget_text_align import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidget(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetReplyType],
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
    color: typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetColor] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    font_family: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFontFamily],
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(alias="fontFamily"),
    ] = None
    font_size: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")
    ] = None
    font_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFontColor],
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ] = None
    text_align: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]
    field_object_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="fieldObjectNumber"), pydantic.Field(alias="fieldObjectNumber")
    ]
    field_family: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily,
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
