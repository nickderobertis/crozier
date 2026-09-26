

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_blend_mode import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactBlendMode,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_flags import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFlags,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_font_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFontColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_font_family import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFontFamily,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_identity_quality import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactIdentityQuality,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_in_reply_to import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactInReplyTo,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_interior_color import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactInteriorColor,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_page import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactPage,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_quad_points_item import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItem,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_rect import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRect,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_ref import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_reply_type import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactReplyType,
)
from .doc_annotations_list_all200response_pages_item_annotations_item_redact_text_align import (
    DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactTextAlign,
)
from .pdf_annotation_actions import PdfAnnotationActions


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedact(UniversalBaseModel):
    ref: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRef
    page: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFlags
    rect: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactReplyType],
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
        typing.List[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]
    color: DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactColor
    opacity: float
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    overlay_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="overlayText"), pydantic.Field(alias="overlayText")
    ] = None
    repeat: bool
    font_family: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFontFamily,
        FieldMetadata(alias="fontFamily"),
        pydantic.Field(alias="fontFamily"),
    ]
    font_size: typing_extensions.Annotated[float, FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")]
    font_color: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactFontColor,
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ]
    text_align: typing_extensions.Annotated[
        DocAnnotationsListAll200ResponsePagesItemAnnotationsItemRedactTextAlign,
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
