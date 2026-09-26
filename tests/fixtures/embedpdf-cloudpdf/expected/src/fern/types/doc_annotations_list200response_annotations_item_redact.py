

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_redact_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemRedactBlendMode,
)
from .doc_annotations_list200response_annotations_item_redact_color import (
    DocAnnotationsList200ResponseAnnotationsItemRedactColor,
)
from .doc_annotations_list200response_annotations_item_redact_flags import (
    DocAnnotationsList200ResponseAnnotationsItemRedactFlags,
)
from .doc_annotations_list200response_annotations_item_redact_font_color import (
    DocAnnotationsList200ResponseAnnotationsItemRedactFontColor,
)
from .doc_annotations_list200response_annotations_item_redact_font_family import (
    DocAnnotationsList200ResponseAnnotationsItemRedactFontFamily,
)
from .doc_annotations_list200response_annotations_item_redact_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemRedactIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_redact_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo,
)
from .doc_annotations_list200response_annotations_item_redact_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemRedactInteriorColor,
)
from .doc_annotations_list200response_annotations_item_redact_page import (
    DocAnnotationsList200ResponseAnnotationsItemRedactPage,
)
from .doc_annotations_list200response_annotations_item_redact_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_redact_rect import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRect,
)
from .doc_annotations_list200response_annotations_item_redact_ref import (
    DocAnnotationsList200ResponseAnnotationsItemRedactRef,
)
from .doc_annotations_list200response_annotations_item_redact_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemRedactReplyType,
)
from .doc_annotations_list200response_annotations_item_redact_text_align import (
    DocAnnotationsList200ResponseAnnotationsItemRedactTextAlign,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsList200ResponseAnnotationsItemRedact(UniversalBaseModel):
    ref: DocAnnotationsList200ResponseAnnotationsItemRedactRef
    page: DocAnnotationsList200ResponseAnnotationsItemRedactPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemRedactIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemRedactFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemRedactRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemRedactBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemRedactInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemRedactReplyType],
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
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemRedactQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]
    color: DocAnnotationsList200ResponseAnnotationsItemRedactColor
    opacity: float
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemRedactInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    overlay_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="overlayText"), pydantic.Field(alias="overlayText")
    ] = None
    repeat: bool
    font_family: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemRedactFontFamily,
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(alias="fontFamily"),
    ]
    font_size: typing_extensions.Annotated[float, FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")]
    font_color: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemRedactFontColor,
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ]
    text_align: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemRedactTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
