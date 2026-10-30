



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .block_object_request import (
        BlockObjectRequest,
        BlockObjectRequest_BulletedListItem,
        BlockObjectRequest_Paragraph,
    )
    from .bulleted_list_item_block_request import BulletedListItemBlockRequest
    from .bulleted_list_item_block_request_bulleted_list_item import BulletedListItemBlockRequestBulletedListItem
    from .conflict_error_body import ConflictErrorBody
    from .create_a_comment_request_parent import CreateACommentRequestParent
    from .create_a_comment_request_rich_text_item import CreateACommentRequestRichTextItem
    from .create_a_comment_request_rich_text_item_text import CreateACommentRequestRichTextItemText
    from .data_source_id_parent_request import DataSourceIdParentRequest
    from .data_source_id_parent_request_type import DataSourceIdParentRequestType
    from .forbidden_error_body import ForbiddenErrorBody
    from .get_self_response import GetSelfResponse
    from .get_self_response_bot import GetSelfResponseBot
    from .get_self_response_bot_owner import GetSelfResponseBotOwner
    from .get_self_response_bot_owner_user import GetSelfResponseBotOwnerUser
    from .get_self_response_bot_owner_user_person import GetSelfResponseBotOwnerUserPerson
    from .move_page_parent_request import MovePageParentRequest
    from .move_page_parent_request_database_id import MovePageParentRequestDatabaseId
    from .move_page_parent_request_database_id_type import MovePageParentRequestDatabaseIdType
    from .move_page_parent_request_page_id import MovePageParentRequestPageId
    from .move_page_parent_request_page_id_type import MovePageParentRequestPageIdType
    from .move_page_parent_request_type import MovePageParentRequestType
    from .move_page_parent_request_type_type import MovePageParentRequestTypeType
    from .not_found_error_body import NotFoundErrorBody
    from .page_id_parent_request import PageIdParentRequest
    from .paragraph_block_request import ParagraphBlockRequest
    from .paragraph_block_request_paragraph import ParagraphBlockRequestParagraph
    from .parent_request import ParentRequest
    from .parent_request_type import ParentRequestType
    from .parent_request_type_type import ParentRequestTypeType
    from .patch_page_request_cover import PatchPageRequestCover
    from .patch_page_request_cover_external import PatchPageRequestCoverExternal
    from .patch_page_request_cover_type import PatchPageRequestCoverType
    from .patch_page_request_icon import PatchPageRequestIcon
    from .post_search_request_filter import PostSearchRequestFilter
    from .post_search_request_filter_value import PostSearchRequestFilterValue
    from .post_search_request_sort import PostSearchRequestSort
    from .rich_text_request import RichTextRequest
    from .rich_text_request_text import RichTextRequestText
    from .rich_text_request_text_link import RichTextRequestTextLink
    from .rich_text_request_type import RichTextRequestType
    from .sort_object import SortObject
    from .sort_object_direction import SortObjectDirection
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .update_a_block_request_type import UpdateABlockRequestType
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BlockObjectRequest": ".block_object_request",
    "BlockObjectRequest_BulletedListItem": ".block_object_request",
    "BlockObjectRequest_Paragraph": ".block_object_request",
    "BulletedListItemBlockRequest": ".bulleted_list_item_block_request",
    "BulletedListItemBlockRequestBulletedListItem": ".bulleted_list_item_block_request_bulleted_list_item",
    "ConflictErrorBody": ".conflict_error_body",
    "CreateACommentRequestParent": ".create_a_comment_request_parent",
    "CreateACommentRequestRichTextItem": ".create_a_comment_request_rich_text_item",
    "CreateACommentRequestRichTextItemText": ".create_a_comment_request_rich_text_item_text",
    "DataSourceIdParentRequest": ".data_source_id_parent_request",
    "DataSourceIdParentRequestType": ".data_source_id_parent_request_type",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "GetSelfResponse": ".get_self_response",
    "GetSelfResponseBot": ".get_self_response_bot",
    "GetSelfResponseBotOwner": ".get_self_response_bot_owner",
    "GetSelfResponseBotOwnerUser": ".get_self_response_bot_owner_user",
    "GetSelfResponseBotOwnerUserPerson": ".get_self_response_bot_owner_user_person",
    "MovePageParentRequest": ".move_page_parent_request",
    "MovePageParentRequestDatabaseId": ".move_page_parent_request_database_id",
    "MovePageParentRequestDatabaseIdType": ".move_page_parent_request_database_id_type",
    "MovePageParentRequestPageId": ".move_page_parent_request_page_id",
    "MovePageParentRequestPageIdType": ".move_page_parent_request_page_id_type",
    "MovePageParentRequestType": ".move_page_parent_request_type",
    "MovePageParentRequestTypeType": ".move_page_parent_request_type_type",
    "NotFoundErrorBody": ".not_found_error_body",
    "PageIdParentRequest": ".page_id_parent_request",
    "ParagraphBlockRequest": ".paragraph_block_request",
    "ParagraphBlockRequestParagraph": ".paragraph_block_request_paragraph",
    "ParentRequest": ".parent_request",
    "ParentRequestType": ".parent_request_type",
    "ParentRequestTypeType": ".parent_request_type_type",
    "PatchPageRequestCover": ".patch_page_request_cover",
    "PatchPageRequestCoverExternal": ".patch_page_request_cover_external",
    "PatchPageRequestCoverType": ".patch_page_request_cover_type",
    "PatchPageRequestIcon": ".patch_page_request_icon",
    "PostSearchRequestFilter": ".post_search_request_filter",
    "PostSearchRequestFilterValue": ".post_search_request_filter_value",
    "PostSearchRequestSort": ".post_search_request_sort",
    "RichTextRequest": ".rich_text_request",
    "RichTextRequestText": ".rich_text_request_text",
    "RichTextRequestTextLink": ".rich_text_request_text_link",
    "RichTextRequestType": ".rich_text_request_type",
    "SortObject": ".sort_object",
    "SortObjectDirection": ".sort_object_direction",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "UpdateABlockRequestType": ".update_a_block_request_type",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "BadRequestErrorBody",
    "BlockObjectRequest",
    "BlockObjectRequest_BulletedListItem",
    "BlockObjectRequest_Paragraph",
    "BulletedListItemBlockRequest",
    "BulletedListItemBlockRequestBulletedListItem",
    "ConflictErrorBody",
    "CreateACommentRequestParent",
    "CreateACommentRequestRichTextItem",
    "CreateACommentRequestRichTextItemText",
    "DataSourceIdParentRequest",
    "DataSourceIdParentRequestType",
    "ForbiddenErrorBody",
    "GetSelfResponse",
    "GetSelfResponseBot",
    "GetSelfResponseBotOwner",
    "GetSelfResponseBotOwnerUser",
    "GetSelfResponseBotOwnerUserPerson",
    "MovePageParentRequest",
    "MovePageParentRequestDatabaseId",
    "MovePageParentRequestDatabaseIdType",
    "MovePageParentRequestPageId",
    "MovePageParentRequestPageIdType",
    "MovePageParentRequestType",
    "MovePageParentRequestTypeType",
    "NotFoundErrorBody",
    "PageIdParentRequest",
    "ParagraphBlockRequest",
    "ParagraphBlockRequestParagraph",
    "ParentRequest",
    "ParentRequestType",
    "ParentRequestTypeType",
    "PatchPageRequestCover",
    "PatchPageRequestCoverExternal",
    "PatchPageRequestCoverType",
    "PatchPageRequestIcon",
    "PostSearchRequestFilter",
    "PostSearchRequestFilterValue",
    "PostSearchRequestSort",
    "RichTextRequest",
    "RichTextRequestText",
    "RichTextRequestTextLink",
    "RichTextRequestType",
    "SortObject",
    "SortObjectDirection",
    "TooManyRequestsErrorBody",
    "UpdateABlockRequestType",
]
