

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_annotations_list200response_annotations_item_caret_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemCaretBlendMode,
)
from .doc_annotations_list200response_annotations_item_caret_color import (
    DocAnnotationsList200ResponseAnnotationsItemCaretColor,
)
from .doc_annotations_list200response_annotations_item_caret_flags import (
    DocAnnotationsList200ResponseAnnotationsItemCaretFlags,
)
from .doc_annotations_list200response_annotations_item_caret_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemCaretIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_caret_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo,
)
from .doc_annotations_list200response_annotations_item_caret_intent import (
    DocAnnotationsList200ResponseAnnotationsItemCaretIntent,
)
from .doc_annotations_list200response_annotations_item_caret_page import (
    DocAnnotationsList200ResponseAnnotationsItemCaretPage,
)
from .doc_annotations_list200response_annotations_item_caret_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRect,
)
from .doc_annotations_list200response_annotations_item_caret_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRectDifferences,
)
from .doc_annotations_list200response_annotations_item_caret_ref import (
    DocAnnotationsList200ResponseAnnotationsItemCaretRef,
)
from .doc_annotations_list200response_annotations_item_caret_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemCaretReplyType,
)
from .doc_annotations_list200response_annotations_item_caret_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCaretUnrotatedRect,
)
from .doc_annotations_list200response_annotations_item_circle_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemCircleBlendMode,
)
from .doc_annotations_list200response_annotations_item_circle_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemCircleBorderStyle,
)
from .doc_annotations_list200response_annotations_item_circle_color import (
    DocAnnotationsList200ResponseAnnotationsItemCircleColor,
)
from .doc_annotations_list200response_annotations_item_circle_flags import (
    DocAnnotationsList200ResponseAnnotationsItemCircleFlags,
)
from .doc_annotations_list200response_annotations_item_circle_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemCircleIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_circle_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemCircleInReplyTo,
)
from .doc_annotations_list200response_annotations_item_circle_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemCircleInteriorColor,
)
from .doc_annotations_list200response_annotations_item_circle_page import (
    DocAnnotationsList200ResponseAnnotationsItemCirclePage,
)
from .doc_annotations_list200response_annotations_item_circle_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRect,
)
from .doc_annotations_list200response_annotations_item_circle_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRectDifferences,
)
from .doc_annotations_list200response_annotations_item_circle_ref import (
    DocAnnotationsList200ResponseAnnotationsItemCircleRef,
)
from .doc_annotations_list200response_annotations_item_circle_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemCircleReplyType,
)
from .doc_annotations_list200response_annotations_item_circle_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemCircleUnrotatedRect,
)
from .doc_annotations_list200response_annotations_item_file_attachment_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentBlendMode,
)
from .doc_annotations_list200response_annotations_item_file_attachment_color import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentColor,
)
from .doc_annotations_list200response_annotations_item_file_attachment_file import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFile,
)
from .doc_annotations_list200response_annotations_item_file_attachment_flags import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFlags,
)
from .doc_annotations_list200response_annotations_item_file_attachment_icon import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon,
)
from .doc_annotations_list200response_annotations_item_file_attachment_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_file_attachment_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo,
)
from .doc_annotations_list200response_annotations_item_file_attachment_page import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPage,
)
from .doc_annotations_list200response_annotations_item_file_attachment_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRect,
)
from .doc_annotations_list200response_annotations_item_file_attachment_ref import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef,
)
from .doc_annotations_list200response_annotations_item_file_attachment_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemFileAttachmentReplyType,
)
from .doc_annotations_list200response_annotations_item_free_text_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextBlendMode,
)
from .doc_annotations_list200response_annotations_item_free_text_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextBorderStyle,
)
from .doc_annotations_list200response_annotations_item_free_text_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextColor,
)
from .doc_annotations_list200response_annotations_item_free_text_flags import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextFlags,
)
from .doc_annotations_list200response_annotations_item_free_text_font_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextFontColor,
)
from .doc_annotations_list200response_annotations_item_free_text_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_free_text_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo,
)
from .doc_annotations_list200response_annotations_item_free_text_intent import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextIntent,
)
from .doc_annotations_list200response_annotations_item_free_text_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextInteriorColor,
)
from .doc_annotations_list200response_annotations_item_free_text_line_ending import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextLineEnding,
)
from .doc_annotations_list200response_annotations_item_free_text_page import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextPage,
)
from .doc_annotations_list200response_annotations_item_free_text_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRect,
)
from .doc_annotations_list200response_annotations_item_free_text_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRectDifferences,
)
from .doc_annotations_list200response_annotations_item_free_text_ref import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRef,
)
from .doc_annotations_list200response_annotations_item_free_text_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextReplyType,
)
from .doc_annotations_list200response_annotations_item_free_text_rich_text import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextRichText,
)
from .doc_annotations_list200response_annotations_item_free_text_text_align import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextTextAlign,
)
from .doc_annotations_list200response_annotations_item_free_text_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemFreeTextUnrotatedRect,
)
from .doc_annotations_list200response_annotations_item_highlight_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightBlendMode,
)
from .doc_annotations_list200response_annotations_item_highlight_color import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightColor,
)
from .doc_annotations_list200response_annotations_item_highlight_flags import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightFlags,
)
from .doc_annotations_list200response_annotations_item_highlight_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_highlight_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo,
)
from .doc_annotations_list200response_annotations_item_highlight_page import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightPage,
)
from .doc_annotations_list200response_annotations_item_highlight_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_highlight_rect import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRect,
)
from .doc_annotations_list200response_annotations_item_highlight_ref import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightRef,
)
from .doc_annotations_list200response_annotations_item_highlight_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemHighlightReplyType,
)
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
from .doc_annotations_list200response_annotations_item_line_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemLineBlendMode,
)
from .doc_annotations_list200response_annotations_item_line_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemLineBorderStyle,
)
from .doc_annotations_list200response_annotations_item_line_caption import (
    DocAnnotationsList200ResponseAnnotationsItemLineCaption,
)
from .doc_annotations_list200response_annotations_item_line_color import (
    DocAnnotationsList200ResponseAnnotationsItemLineColor,
)
from .doc_annotations_list200response_annotations_item_line_flags import (
    DocAnnotationsList200ResponseAnnotationsItemLineFlags,
)
from .doc_annotations_list200response_annotations_item_line_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemLineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_line_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_line_intent import (
    DocAnnotationsList200ResponseAnnotationsItemLineIntent,
)
from .doc_annotations_list200response_annotations_item_line_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemLineInteriorColor,
)
from .doc_annotations_list200response_annotations_item_line_leader import (
    DocAnnotationsList200ResponseAnnotationsItemLineLeader,
)
from .doc_annotations_list200response_annotations_item_line_line_endings import (
    DocAnnotationsList200ResponseAnnotationsItemLineLineEndings,
)
from .doc_annotations_list200response_annotations_item_line_line_points import (
    DocAnnotationsList200ResponseAnnotationsItemLineLinePoints,
)
from .doc_annotations_list200response_annotations_item_line_measure import (
    DocAnnotationsList200ResponseAnnotationsItemLineMeasure,
)
from .doc_annotations_list200response_annotations_item_line_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinePage,
)
from .doc_annotations_list200response_annotations_item_line_rect import (
    DocAnnotationsList200ResponseAnnotationsItemLineRect,
)
from .doc_annotations_list200response_annotations_item_line_ref import (
    DocAnnotationsList200ResponseAnnotationsItemLineRef,
)
from .doc_annotations_list200response_annotations_item_line_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemLineReplyType,
)
from .doc_annotations_list200response_annotations_item_link_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemLinkBlendMode,
)
from .doc_annotations_list200response_annotations_item_link_flags import (
    DocAnnotationsList200ResponseAnnotationsItemLinkFlags,
)
from .doc_annotations_list200response_annotations_item_link_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemLinkIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_link_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo,
)
from .doc_annotations_list200response_annotations_item_link_page import (
    DocAnnotationsList200ResponseAnnotationsItemLinkPage,
)
from .doc_annotations_list200response_annotations_item_link_rect import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRect,
)
from .doc_annotations_list200response_annotations_item_link_ref import (
    DocAnnotationsList200ResponseAnnotationsItemLinkRef,
)
from .doc_annotations_list200response_annotations_item_link_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemLinkReplyType,
)
from .doc_annotations_list200response_annotations_item_link_target import (
    DocAnnotationsList200ResponseAnnotationsItemLinkTarget,
)
from .doc_annotations_list200response_annotations_item_polygon_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode,
)
from .doc_annotations_list200response_annotations_item_polygon_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonBorderStyle,
)
from .doc_annotations_list200response_annotations_item_polygon_caption import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonCaption,
)
from .doc_annotations_list200response_annotations_item_polygon_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonColor,
)
from .doc_annotations_list200response_annotations_item_polygon_flags import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonFlags,
)
from .doc_annotations_list200response_annotations_item_polygon_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_polygon_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo,
)
from .doc_annotations_list200response_annotations_item_polygon_intent import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonIntent,
)
from .doc_annotations_list200response_annotations_item_polygon_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonInteriorColor,
)
from .doc_annotations_list200response_annotations_item_polygon_measure import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure,
)
from .doc_annotations_list200response_annotations_item_polygon_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonPage,
)
from .doc_annotations_list200response_annotations_item_polygon_rect import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRect,
)
from .doc_annotations_list200response_annotations_item_polygon_ref import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonRef,
)
from .doc_annotations_list200response_annotations_item_polygon_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonReplyType,
)
from .doc_annotations_list200response_annotations_item_polygon_vertices_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolygonVerticesItem,
)
from .doc_annotations_list200response_annotations_item_polyline_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineBlendMode,
)
from .doc_annotations_list200response_annotations_item_polyline_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle,
)
from .doc_annotations_list200response_annotations_item_polyline_caption import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineCaption,
)
from .doc_annotations_list200response_annotations_item_polyline_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineColor,
)
from .doc_annotations_list200response_annotations_item_polyline_flags import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineFlags,
)
from .doc_annotations_list200response_annotations_item_polyline_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_polyline_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_polyline_intent import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineIntent,
)
from .doc_annotations_list200response_annotations_item_polyline_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineInteriorColor,
)
from .doc_annotations_list200response_annotations_item_polyline_line_endings import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineLineEndings,
)
from .doc_annotations_list200response_annotations_item_polyline_measure import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineMeasure,
)
from .doc_annotations_list200response_annotations_item_polyline_page import (
    DocAnnotationsList200ResponseAnnotationsItemPolylinePage,
)
from .doc_annotations_list200response_annotations_item_polyline_rect import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRect,
)
from .doc_annotations_list200response_annotations_item_polyline_ref import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineRef,
)
from .doc_annotations_list200response_annotations_item_polyline_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineReplyType,
)
from .doc_annotations_list200response_annotations_item_polyline_vertices_item import (
    DocAnnotationsList200ResponseAnnotationsItemPolylineVerticesItem,
)
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
from .doc_annotations_list200response_annotations_item_square_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemSquareBlendMode,
)
from .doc_annotations_list200response_annotations_item_square_border_style import (
    DocAnnotationsList200ResponseAnnotationsItemSquareBorderStyle,
)
from .doc_annotations_list200response_annotations_item_square_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquareColor,
)
from .doc_annotations_list200response_annotations_item_square_flags import (
    DocAnnotationsList200ResponseAnnotationsItemSquareFlags,
)
from .doc_annotations_list200response_annotations_item_square_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemSquareIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_square_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemSquareInReplyTo,
)
from .doc_annotations_list200response_annotations_item_square_interior_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquareInteriorColor,
)
from .doc_annotations_list200response_annotations_item_square_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquarePage,
)
from .doc_annotations_list200response_annotations_item_square_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRect,
)
from .doc_annotations_list200response_annotations_item_square_rect_differences import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRectDifferences,
)
from .doc_annotations_list200response_annotations_item_square_ref import (
    DocAnnotationsList200ResponseAnnotationsItemSquareRef,
)
from .doc_annotations_list200response_annotations_item_square_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemSquareReplyType,
)
from .doc_annotations_list200response_annotations_item_square_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquareUnrotatedRect,
)
from .doc_annotations_list200response_annotations_item_squiggly_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyBlendMode,
)
from .doc_annotations_list200response_annotations_item_squiggly_color import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyColor,
)
from .doc_annotations_list200response_annotations_item_squiggly_flags import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyFlags,
)
from .doc_annotations_list200response_annotations_item_squiggly_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_squiggly_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo,
)
from .doc_annotations_list200response_annotations_item_squiggly_page import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyPage,
)
from .doc_annotations_list200response_annotations_item_squiggly_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_squiggly_rect import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyRect,
)
from .doc_annotations_list200response_annotations_item_squiggly_ref import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyRef,
)
from .doc_annotations_list200response_annotations_item_squiggly_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemSquigglyReplyType,
)
from .doc_annotations_list200response_annotations_item_stamp_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemStampBlendMode,
)
from .doc_annotations_list200response_annotations_item_stamp_flags import (
    DocAnnotationsList200ResponseAnnotationsItemStampFlags,
)
from .doc_annotations_list200response_annotations_item_stamp_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemStampIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_stamp_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemStampInReplyTo,
)
from .doc_annotations_list200response_annotations_item_stamp_page import (
    DocAnnotationsList200ResponseAnnotationsItemStampPage,
)
from .doc_annotations_list200response_annotations_item_stamp_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStampRect,
)
from .doc_annotations_list200response_annotations_item_stamp_ref import (
    DocAnnotationsList200ResponseAnnotationsItemStampRef,
)
from .doc_annotations_list200response_annotations_item_stamp_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemStampReplyType,
)
from .doc_annotations_list200response_annotations_item_stamp_unrotated_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStampUnrotatedRect,
)
from .doc_annotations_list200response_annotations_item_strikeout_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutBlendMode,
)
from .doc_annotations_list200response_annotations_item_strikeout_color import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutColor,
)
from .doc_annotations_list200response_annotations_item_strikeout_flags import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutFlags,
)
from .doc_annotations_list200response_annotations_item_strikeout_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_strikeout_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo,
)
from .doc_annotations_list200response_annotations_item_strikeout_intent import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent,
)
from .doc_annotations_list200response_annotations_item_strikeout_page import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutPage,
)
from .doc_annotations_list200response_annotations_item_strikeout_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_strikeout_rect import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRect,
)
from .doc_annotations_list200response_annotations_item_strikeout_ref import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef,
)
from .doc_annotations_list200response_annotations_item_strikeout_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemStrikeoutReplyType,
)
from .doc_annotations_list200response_annotations_item_text_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemTextBlendMode,
)
from .doc_annotations_list200response_annotations_item_text_color import (
    DocAnnotationsList200ResponseAnnotationsItemTextColor,
)
from .doc_annotations_list200response_annotations_item_text_flags import (
    DocAnnotationsList200ResponseAnnotationsItemTextFlags,
)
from .doc_annotations_list200response_annotations_item_text_icon import (
    DocAnnotationsList200ResponseAnnotationsItemTextIcon,
)
from .doc_annotations_list200response_annotations_item_text_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemTextIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_text_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo,
)
from .doc_annotations_list200response_annotations_item_text_page import (
    DocAnnotationsList200ResponseAnnotationsItemTextPage,
)
from .doc_annotations_list200response_annotations_item_text_rect import (
    DocAnnotationsList200ResponseAnnotationsItemTextRect,
)
from .doc_annotations_list200response_annotations_item_text_ref import (
    DocAnnotationsList200ResponseAnnotationsItemTextRef,
)
from .doc_annotations_list200response_annotations_item_text_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemTextReplyType,
)
from .doc_annotations_list200response_annotations_item_underline_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineBlendMode,
)
from .doc_annotations_list200response_annotations_item_underline_color import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineColor,
)
from .doc_annotations_list200response_annotations_item_underline_flags import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineFlags,
)
from .doc_annotations_list200response_annotations_item_underline_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_underline_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo,
)
from .doc_annotations_list200response_annotations_item_underline_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlinePage,
)
from .doc_annotations_list200response_annotations_item_underline_quad_points_item import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItem,
)
from .doc_annotations_list200response_annotations_item_underline_rect import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRect,
)
from .doc_annotations_list200response_annotations_item_underline_ref import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineRef,
)
from .doc_annotations_list200response_annotations_item_underline_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType,
)
from .doc_annotations_list200response_annotations_item_unsupported_blend_mode import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedBlendMode,
)
from .doc_annotations_list200response_annotations_item_unsupported_flags import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedFlags,
)
from .doc_annotations_list200response_annotations_item_unsupported_identity_quality import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedIdentityQuality,
)
from .doc_annotations_list200response_annotations_item_unsupported_in_reply_to import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo,
)
from .doc_annotations_list200response_annotations_item_unsupported_page import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedPage,
)
from .doc_annotations_list200response_annotations_item_unsupported_rect import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRect,
)
from .doc_annotations_list200response_annotations_item_unsupported_ref import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef,
)
from .doc_annotations_list200response_annotations_item_unsupported_reply_type import (
    DocAnnotationsList200ResponseAnnotationsItemUnsupportedReplyType,
)
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


class DocAnnotationsList200ResponseAnnotationsItem_Highlight(UniversalBaseModel):
    subtype: typing.Literal["highlight"] = "highlight"
    ref: DocAnnotationsList200ResponseAnnotationsItemHighlightRef
    page: DocAnnotationsList200ResponseAnnotationsItemHighlightPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemHighlightIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemHighlightFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemHighlightRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemHighlightBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemHighlightInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemHighlightReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemHighlightColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemHighlightQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Underline(UniversalBaseModel):
    subtype: typing.Literal["underline"] = "underline"
    ref: DocAnnotationsList200ResponseAnnotationsItemUnderlineRef
    page: DocAnnotationsList200ResponseAnnotationsItemUnderlinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemUnderlineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemUnderlineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnderlineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnderlineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnderlineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemUnderlineColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemUnderlineQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Squiggly(UniversalBaseModel):
    subtype: typing.Literal["squiggly"] = "squiggly"
    ref: DocAnnotationsList200ResponseAnnotationsItemSquigglyRef
    page: DocAnnotationsList200ResponseAnnotationsItemSquigglyPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquigglyIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemSquigglyFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemSquigglyRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquigglyBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquigglyInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquigglyReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemSquigglyColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemSquigglyQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Strikeout(UniversalBaseModel):
    subtype: typing.Literal["strikeout"] = "strikeout"
    ref: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRef
    page: DocAnnotationsList200ResponseAnnotationsItemStrikeoutPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemStrikeoutFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemStrikeoutRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStrikeoutBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemStrikeoutColor
    opacity: float
    quad_points: typing_extensions.Annotated[
        typing.List[DocAnnotationsList200ResponseAnnotationsItemStrikeoutQuadPointsItem],
        FieldMetadata(alias="quadPoints"),
        pydantic.Field(alias="quadPoints"),
    ]
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Circle(UniversalBaseModel):
    subtype: typing.Literal["circle"] = "circle"
    ref: DocAnnotationsList200ResponseAnnotationsItemCircleRef
    page: DocAnnotationsList200ResponseAnnotationsItemCirclePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemCircleFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemCircleRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemCircleColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCircleBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCircleUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Square(UniversalBaseModel):
    subtype: typing.Literal["square"] = "square"
    ref: DocAnnotationsList200ResponseAnnotationsItemSquareRef
    page: DocAnnotationsList200ResponseAnnotationsItemSquarePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemSquareFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemSquareRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemSquareColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemSquareBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemSquareUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Polygon(UniversalBaseModel):
    subtype: typing.Literal["polygon"] = "polygon"
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonCaption] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemPolygonRef
    page: DocAnnotationsList200ResponseAnnotationsItemPolygonPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemPolygonFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemPolygonRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemPolygonColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolygonBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolygonInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolygonVerticesItem]
    rotation: typing.Optional[float] = None
    cloudy_intensity: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="cloudyIntensity"), pydantic.Field(alias="cloudyIntensity")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Polyline(UniversalBaseModel):
    subtype: typing.Literal["polyline"] = "polyline"
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineCaption] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemPolylineRef
    page: DocAnnotationsList200ResponseAnnotationsItemPolylinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemPolylineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemPolylineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemPolylineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemPolylineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    vertices: typing.List[DocAnnotationsList200ResponseAnnotationsItemPolylineVerticesItem]
    rotation: typing.Optional[float] = None
    line_endings: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemPolylineLineEndings,
        FieldMetadata(alias="lineEndings"),
        pydantic.Field(alias="lineEndings"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Line(UniversalBaseModel):
    subtype: typing.Literal["line"] = "line"
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineIntent] = None
    measure: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineMeasure] = None
    caption: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineCaption] = None
    leader: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineLeader] = None
    ref: DocAnnotationsList200ResponseAnnotationsItemLineRef
    page: DocAnnotationsList200ResponseAnnotationsItemLinePage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemLineFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemLineRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemLineColor
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLineInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    line_points: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineLinePoints,
        FieldMetadata(alias="linePoints"),
        pydantic.Field(alias="linePoints"),
    ]
    line_endings: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLineLineEndings,
        FieldMetadata(alias="lineEndings"),
        pydantic.Field(alias="lineEndings"),
    ]
    rotation: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Link(UniversalBaseModel):
    subtype: typing.Literal["link"] = "link"
    ref: DocAnnotationsList200ResponseAnnotationsItemLinkRef
    page: DocAnnotationsList200ResponseAnnotationsItemLinkPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLinkIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemLinkFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemLinkRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemLinkBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkReplyType],
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
    target: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemLinkTarget] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Ink(UniversalBaseModel):
    subtype: typing.Literal["ink"] = "ink"
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


class DocAnnotationsList200ResponseAnnotationsItem_FreeText(UniversalBaseModel):
    subtype: typing.Literal["free-text"] = "free-text"
    ref: DocAnnotationsList200ResponseAnnotationsItemFreeTextRef
    page: DocAnnotationsList200ResponseAnnotationsItemFreeTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemFreeTextFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemFreeTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextReplyType],
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
    intent: DocAnnotationsList200ResponseAnnotationsItemFreeTextIntent
    font_family: typing_extensions.Annotated[str, FieldMetadata(alias="fontFamily"), pydantic.Field(alias="fontFamily")]
    font_size: typing_extensions.Annotated[float, FieldMetadata(alias="fontSize"), pydantic.Field(alias="fontSize")]
    text_align: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextTextAlign,
        FieldMetadata(alias="textAlign"),
        pydantic.Field(alias="textAlign"),
    ]
    rich_text: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextRichText,
        FieldMetadata(alias="richText"),
        pydantic.Field(alias="richText"),
    ]
    color: DocAnnotationsList200ResponseAnnotationsItemFreeTextColor
    font_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextFontColor],
        FieldMetadata(alias="fontColor"),
        pydantic.Field(alias="fontColor"),
    ] = None
    interior_color: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextInteriorColor],
        FieldMetadata(alias="interiorColor"),
        pydantic.Field(alias="interiorColor"),
    ] = None
    opacity: float
    stroke_width: typing_extensions.Annotated[
        float, FieldMetadata(alias="strokeWidth"), pydantic.Field(alias="strokeWidth")
    ]
    border_style: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFreeTextBorderStyle,
        FieldMetadata(alias="borderStyle"),
        pydantic.Field(alias="borderStyle"),
    ]
    dash_array: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="dashArray"), pydantic.Field(alias="dashArray")
    ] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    callout_line: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="calloutLine"),
        pydantic.Field(alias="calloutLine"),
    ] = None
    line_ending: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextLineEnding],
        FieldMetadata(alias="lineEnding"),
        pydantic.Field(alias="lineEnding"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFreeTextUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Caret(UniversalBaseModel):
    subtype: typing.Literal["caret"] = "caret"
    ref: DocAnnotationsList200ResponseAnnotationsItemCaretRef
    page: DocAnnotationsList200ResponseAnnotationsItemCaretPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCaretIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemCaretFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemCaretRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemCaretBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemCaretColor
    opacity: float
    intent: typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretIntent] = None
    rect_differences: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretRectDifferences],
        FieldMetadata(alias="rectDifferences"),
        pydantic.Field(alias="rectDifferences"),
    ] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemCaretUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Text(UniversalBaseModel):
    subtype: typing.Literal["text"] = "text"
    ref: DocAnnotationsList200ResponseAnnotationsItemTextRef
    page: DocAnnotationsList200ResponseAnnotationsItemTextPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemTextIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemTextFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemTextRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemTextBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemTextInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemTextReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemTextColor
    opacity: float
    icon: DocAnnotationsList200ResponseAnnotationsItemTextIcon
    state: typing.Optional[str] = None
    state_model: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stateModel"), pydantic.Field(alias="stateModel")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Stamp(UniversalBaseModel):
    subtype: typing.Literal["stamp"] = "stamp"
    ref: DocAnnotationsList200ResponseAnnotationsItemStampRef
    page: DocAnnotationsList200ResponseAnnotationsItemStampPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStampIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemStampFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemStampRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemStampBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampReplyType],
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
    name: typing.Optional[str] = None
    rotation: typing.Optional[float] = None
    unrotated_rect: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemStampUnrotatedRect],
        FieldMetadata(alias="unrotatedRect"),
        pydantic.Field(alias="unrotatedRect"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_FileAttachment(UniversalBaseModel):
    subtype: typing.Literal["file-attachment"] = "file-attachment"
    ref: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRef
    page: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemFileAttachmentBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFileAttachmentInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemFileAttachmentReplyType],
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
    color: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentColor
    opacity: float
    icon: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentIcon
    file: DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFile

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class DocAnnotationsList200ResponseAnnotationsItem_Widget(UniversalBaseModel):
    subtype: typing.Literal["widget"] = "widget"
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


class DocAnnotationsList200ResponseAnnotationsItem_Redact(UniversalBaseModel):
    subtype: typing.Literal["redact"] = "redact"
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


class DocAnnotationsList200ResponseAnnotationsItem_Unsupported(UniversalBaseModel):
    subtype: typing.Literal["unsupported"] = "unsupported"
    ref: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRef
    page: DocAnnotationsList200ResponseAnnotationsItemUnsupportedPage
    index: int
    identity_quality: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedIdentityQuality,
        FieldMetadata(alias="identityQuality"),
        pydantic.Field(alias="identityQuality"),
    ]
    nm: typing.Optional[str] = None
    flags: DocAnnotationsList200ResponseAnnotationsItemUnsupportedFlags
    rect: DocAnnotationsList200ResponseAnnotationsItemUnsupportedRect
    contents: typing.Optional[str] = None
    subject: typing.Optional[str] = None
    author: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    modified: typing.Optional[dt.datetime] = None
    blend_mode: typing_extensions.Annotated[
        DocAnnotationsList200ResponseAnnotationsItemUnsupportedBlendMode,
        FieldMetadata(alias="blendMode"),
        pydantic.Field(alias="blendMode"),
    ]
    in_reply_to: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnsupportedInReplyTo],
        FieldMetadata(alias="inReplyTo"),
        pydantic.Field(alias="inReplyTo"),
    ] = None
    reply_type: typing_extensions.Annotated[
        typing.Optional[DocAnnotationsList200ResponseAnnotationsItemUnsupportedReplyType],
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
    raw_subtype_code: typing_extensions.Annotated[
        int, FieldMetadata(alias="rawSubtypeCode"), pydantic.Field(alias="rawSubtypeCode")
    ]
    raw_subtype_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rawSubtypeName"), pydantic.Field(alias="rawSubtypeName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


DocAnnotationsList200ResponseAnnotationsItem = typing_extensions.Annotated[
    typing.Union[
        DocAnnotationsList200ResponseAnnotationsItem_Highlight,
        DocAnnotationsList200ResponseAnnotationsItem_Underline,
        DocAnnotationsList200ResponseAnnotationsItem_Squiggly,
        DocAnnotationsList200ResponseAnnotationsItem_Strikeout,
        DocAnnotationsList200ResponseAnnotationsItem_Circle,
        DocAnnotationsList200ResponseAnnotationsItem_Square,
        DocAnnotationsList200ResponseAnnotationsItem_Polygon,
        DocAnnotationsList200ResponseAnnotationsItem_Polyline,
        DocAnnotationsList200ResponseAnnotationsItem_Line,
        DocAnnotationsList200ResponseAnnotationsItem_Link,
        DocAnnotationsList200ResponseAnnotationsItem_Ink,
        DocAnnotationsList200ResponseAnnotationsItem_FreeText,
        DocAnnotationsList200ResponseAnnotationsItem_Caret,
        DocAnnotationsList200ResponseAnnotationsItem_Text,
        DocAnnotationsList200ResponseAnnotationsItem_Stamp,
        DocAnnotationsList200ResponseAnnotationsItem_FileAttachment,
        DocAnnotationsList200ResponseAnnotationsItem_Widget,
        DocAnnotationsList200ResponseAnnotationsItem_Redact,
        DocAnnotationsList200ResponseAnnotationsItem_Unsupported,
    ],
    pydantic.Field(discriminator="subtype"),
]
