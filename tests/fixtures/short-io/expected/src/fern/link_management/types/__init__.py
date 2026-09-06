



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_links_delete_bulk_response import DeleteLinksDeleteBulkResponse
    from .delete_links_link_id_response import DeleteLinksLinkIdResponse
    from .delete_links_permissions_domain_id_link_id_user_id_response import (
        DeleteLinksPermissionsDomainIdLinkIdUserIdResponse,
    )
    from .get_links_permissions_domain_id_link_id_response_item import GetLinksPermissionsDomainIdLinkIdResponseItem
    from .post_links_archive_bulk_response import PostLinksArchiveBulkResponse
    from .post_links_archive_response import PostLinksArchiveResponse
    from .post_links_bulk_request_links_item import PostLinksBulkRequestLinksItem
    from .post_links_bulk_request_links_item_created_at import PostLinksBulkRequestLinksItemCreatedAt
    from .post_links_bulk_request_links_item_expires_at import PostLinksBulkRequestLinksItemExpiresAt
    from .post_links_bulk_request_links_item_split_urlv2item import PostLinksBulkRequestLinksItemSplitUrlv2Item
    from .post_links_bulk_request_links_item_ttl import PostLinksBulkRequestLinksItemTtl
    from .post_links_duplicate_link_id_response import PostLinksDuplicateLinkIdResponse
    from .post_links_duplicate_link_id_response_expires_at import PostLinksDuplicateLinkIdResponseExpiresAt
    from .post_links_duplicate_link_id_response_redirect_type import PostLinksDuplicateLinkIdResponseRedirectType
    from .post_links_duplicate_link_id_response_source import PostLinksDuplicateLinkIdResponseSource
    from .post_links_duplicate_link_id_response_split_urlv2item import PostLinksDuplicateLinkIdResponseSplitUrlv2Item
    from .post_links_duplicate_link_id_response_ttl import PostLinksDuplicateLinkIdResponseTtl
    from .post_links_duplicate_link_id_response_user import PostLinksDuplicateLinkIdResponseUser
    from .post_links_examples_response import PostLinksExamplesResponse
    from .post_links_examples_response_links_item import PostLinksExamplesResponseLinksItem
    from .post_links_examples_response_links_item_expires_at import PostLinksExamplesResponseLinksItemExpiresAt
    from .post_links_examples_response_links_item_redirect_type import PostLinksExamplesResponseLinksItemRedirectType
    from .post_links_examples_response_links_item_source import PostLinksExamplesResponseLinksItemSource
    from .post_links_examples_response_links_item_split_urlv2item import (
        PostLinksExamplesResponseLinksItemSplitUrlv2Item,
    )
    from .post_links_examples_response_links_item_ttl import PostLinksExamplesResponseLinksItemTtl
    from .post_links_examples_response_links_item_user import PostLinksExamplesResponseLinksItemUser
    from .post_links_link_id_request_created_at import PostLinksLinkIdRequestCreatedAt
    from .post_links_link_id_request_expires_at import PostLinksLinkIdRequestExpiresAt
    from .post_links_link_id_request_split_urlv2item import PostLinksLinkIdRequestSplitUrlv2Item
    from .post_links_link_id_request_ttl import PostLinksLinkIdRequestTtl
    from .post_links_link_id_response import PostLinksLinkIdResponse
    from .post_links_link_id_response_expires_at import PostLinksLinkIdResponseExpiresAt
    from .post_links_link_id_response_redirect_type import PostLinksLinkIdResponseRedirectType
    from .post_links_link_id_response_source import PostLinksLinkIdResponseSource
    from .post_links_link_id_response_split_urlv2item import PostLinksLinkIdResponseSplitUrlv2Item
    from .post_links_link_id_response_ttl import PostLinksLinkIdResponseTtl
    from .post_links_link_id_response_user import PostLinksLinkIdResponseUser
    from .post_links_permissions_domain_id_link_id_user_id_response import (
        PostLinksPermissionsDomainIdLinkIdUserIdResponse,
    )
    from .post_links_public_request_created_at import PostLinksPublicRequestCreatedAt
    from .post_links_public_request_expires_at import PostLinksPublicRequestExpiresAt
    from .post_links_public_request_split_urlv2item import PostLinksPublicRequestSplitUrlv2Item
    from .post_links_public_request_ttl import PostLinksPublicRequestTtl
    from .post_links_public_response import PostLinksPublicResponse
    from .post_links_public_response_expires_at import PostLinksPublicResponseExpiresAt
    from .post_links_public_response_redirect_type import PostLinksPublicResponseRedirectType
    from .post_links_public_response_source import PostLinksPublicResponseSource
    from .post_links_public_response_split_urlv2item import PostLinksPublicResponseSplitUrlv2Item
    from .post_links_public_response_ttl import PostLinksPublicResponseTtl
    from .post_links_public_response_user import PostLinksPublicResponseUser
    from .post_links_qr_bulk_request_type import PostLinksQrBulkRequestType
    from .post_links_qr_link_id_string_request_type import PostLinksQrLinkIdStringRequestType
    from .post_links_request_created_at import PostLinksRequestCreatedAt
    from .post_links_request_expires_at import PostLinksRequestExpiresAt
    from .post_links_request_split_urlv2item import PostLinksRequestSplitUrlv2Item
    from .post_links_request_ttl import PostLinksRequestTtl
    from .post_links_response import PostLinksResponse
    from .post_links_response_expires_at import PostLinksResponseExpiresAt
    from .post_links_response_redirect_type import PostLinksResponseRedirectType
    from .post_links_response_source import PostLinksResponseSource
    from .post_links_response_split_urlv2item import PostLinksResponseSplitUrlv2Item
    from .post_links_response_ttl import PostLinksResponseTtl
    from .post_links_response_user import PostLinksResponseUser
    from .post_links_unarchive_bulk_response import PostLinksUnarchiveBulkResponse
    from .post_links_unarchive_response import PostLinksUnarchiveResponse
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteLinksDeleteBulkResponse": ".delete_links_delete_bulk_response",
    "DeleteLinksLinkIdResponse": ".delete_links_link_id_response",
    "DeleteLinksPermissionsDomainIdLinkIdUserIdResponse": ".delete_links_permissions_domain_id_link_id_user_id_response",
    "GetLinksPermissionsDomainIdLinkIdResponseItem": ".get_links_permissions_domain_id_link_id_response_item",
    "PostLinksArchiveBulkResponse": ".post_links_archive_bulk_response",
    "PostLinksArchiveResponse": ".post_links_archive_response",
    "PostLinksBulkRequestLinksItem": ".post_links_bulk_request_links_item",
    "PostLinksBulkRequestLinksItemCreatedAt": ".post_links_bulk_request_links_item_created_at",
    "PostLinksBulkRequestLinksItemExpiresAt": ".post_links_bulk_request_links_item_expires_at",
    "PostLinksBulkRequestLinksItemSplitUrlv2Item": ".post_links_bulk_request_links_item_split_urlv2item",
    "PostLinksBulkRequestLinksItemTtl": ".post_links_bulk_request_links_item_ttl",
    "PostLinksDuplicateLinkIdResponse": ".post_links_duplicate_link_id_response",
    "PostLinksDuplicateLinkIdResponseExpiresAt": ".post_links_duplicate_link_id_response_expires_at",
    "PostLinksDuplicateLinkIdResponseRedirectType": ".post_links_duplicate_link_id_response_redirect_type",
    "PostLinksDuplicateLinkIdResponseSource": ".post_links_duplicate_link_id_response_source",
    "PostLinksDuplicateLinkIdResponseSplitUrlv2Item": ".post_links_duplicate_link_id_response_split_urlv2item",
    "PostLinksDuplicateLinkIdResponseTtl": ".post_links_duplicate_link_id_response_ttl",
    "PostLinksDuplicateLinkIdResponseUser": ".post_links_duplicate_link_id_response_user",
    "PostLinksExamplesResponse": ".post_links_examples_response",
    "PostLinksExamplesResponseLinksItem": ".post_links_examples_response_links_item",
    "PostLinksExamplesResponseLinksItemExpiresAt": ".post_links_examples_response_links_item_expires_at",
    "PostLinksExamplesResponseLinksItemRedirectType": ".post_links_examples_response_links_item_redirect_type",
    "PostLinksExamplesResponseLinksItemSource": ".post_links_examples_response_links_item_source",
    "PostLinksExamplesResponseLinksItemSplitUrlv2Item": ".post_links_examples_response_links_item_split_urlv2item",
    "PostLinksExamplesResponseLinksItemTtl": ".post_links_examples_response_links_item_ttl",
    "PostLinksExamplesResponseLinksItemUser": ".post_links_examples_response_links_item_user",
    "PostLinksLinkIdRequestCreatedAt": ".post_links_link_id_request_created_at",
    "PostLinksLinkIdRequestExpiresAt": ".post_links_link_id_request_expires_at",
    "PostLinksLinkIdRequestSplitUrlv2Item": ".post_links_link_id_request_split_urlv2item",
    "PostLinksLinkIdRequestTtl": ".post_links_link_id_request_ttl",
    "PostLinksLinkIdResponse": ".post_links_link_id_response",
    "PostLinksLinkIdResponseExpiresAt": ".post_links_link_id_response_expires_at",
    "PostLinksLinkIdResponseRedirectType": ".post_links_link_id_response_redirect_type",
    "PostLinksLinkIdResponseSource": ".post_links_link_id_response_source",
    "PostLinksLinkIdResponseSplitUrlv2Item": ".post_links_link_id_response_split_urlv2item",
    "PostLinksLinkIdResponseTtl": ".post_links_link_id_response_ttl",
    "PostLinksLinkIdResponseUser": ".post_links_link_id_response_user",
    "PostLinksPermissionsDomainIdLinkIdUserIdResponse": ".post_links_permissions_domain_id_link_id_user_id_response",
    "PostLinksPublicRequestCreatedAt": ".post_links_public_request_created_at",
    "PostLinksPublicRequestExpiresAt": ".post_links_public_request_expires_at",
    "PostLinksPublicRequestSplitUrlv2Item": ".post_links_public_request_split_urlv2item",
    "PostLinksPublicRequestTtl": ".post_links_public_request_ttl",
    "PostLinksPublicResponse": ".post_links_public_response",
    "PostLinksPublicResponseExpiresAt": ".post_links_public_response_expires_at",
    "PostLinksPublicResponseRedirectType": ".post_links_public_response_redirect_type",
    "PostLinksPublicResponseSource": ".post_links_public_response_source",
    "PostLinksPublicResponseSplitUrlv2Item": ".post_links_public_response_split_urlv2item",
    "PostLinksPublicResponseTtl": ".post_links_public_response_ttl",
    "PostLinksPublicResponseUser": ".post_links_public_response_user",
    "PostLinksQrBulkRequestType": ".post_links_qr_bulk_request_type",
    "PostLinksQrLinkIdStringRequestType": ".post_links_qr_link_id_string_request_type",
    "PostLinksRequestCreatedAt": ".post_links_request_created_at",
    "PostLinksRequestExpiresAt": ".post_links_request_expires_at",
    "PostLinksRequestSplitUrlv2Item": ".post_links_request_split_urlv2item",
    "PostLinksRequestTtl": ".post_links_request_ttl",
    "PostLinksResponse": ".post_links_response",
    "PostLinksResponseExpiresAt": ".post_links_response_expires_at",
    "PostLinksResponseRedirectType": ".post_links_response_redirect_type",
    "PostLinksResponseSource": ".post_links_response_source",
    "PostLinksResponseSplitUrlv2Item": ".post_links_response_split_urlv2item",
    "PostLinksResponseTtl": ".post_links_response_ttl",
    "PostLinksResponseUser": ".post_links_response_user",
    "PostLinksUnarchiveBulkResponse": ".post_links_unarchive_bulk_response",
    "PostLinksUnarchiveResponse": ".post_links_unarchive_response",
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
    "DeleteLinksDeleteBulkResponse",
    "DeleteLinksLinkIdResponse",
    "DeleteLinksPermissionsDomainIdLinkIdUserIdResponse",
    "GetLinksPermissionsDomainIdLinkIdResponseItem",
    "PostLinksArchiveBulkResponse",
    "PostLinksArchiveResponse",
    "PostLinksBulkRequestLinksItem",
    "PostLinksBulkRequestLinksItemCreatedAt",
    "PostLinksBulkRequestLinksItemExpiresAt",
    "PostLinksBulkRequestLinksItemSplitUrlv2Item",
    "PostLinksBulkRequestLinksItemTtl",
    "PostLinksDuplicateLinkIdResponse",
    "PostLinksDuplicateLinkIdResponseExpiresAt",
    "PostLinksDuplicateLinkIdResponseRedirectType",
    "PostLinksDuplicateLinkIdResponseSource",
    "PostLinksDuplicateLinkIdResponseSplitUrlv2Item",
    "PostLinksDuplicateLinkIdResponseTtl",
    "PostLinksDuplicateLinkIdResponseUser",
    "PostLinksExamplesResponse",
    "PostLinksExamplesResponseLinksItem",
    "PostLinksExamplesResponseLinksItemExpiresAt",
    "PostLinksExamplesResponseLinksItemRedirectType",
    "PostLinksExamplesResponseLinksItemSource",
    "PostLinksExamplesResponseLinksItemSplitUrlv2Item",
    "PostLinksExamplesResponseLinksItemTtl",
    "PostLinksExamplesResponseLinksItemUser",
    "PostLinksLinkIdRequestCreatedAt",
    "PostLinksLinkIdRequestExpiresAt",
    "PostLinksLinkIdRequestSplitUrlv2Item",
    "PostLinksLinkIdRequestTtl",
    "PostLinksLinkIdResponse",
    "PostLinksLinkIdResponseExpiresAt",
    "PostLinksLinkIdResponseRedirectType",
    "PostLinksLinkIdResponseSource",
    "PostLinksLinkIdResponseSplitUrlv2Item",
    "PostLinksLinkIdResponseTtl",
    "PostLinksLinkIdResponseUser",
    "PostLinksPermissionsDomainIdLinkIdUserIdResponse",
    "PostLinksPublicRequestCreatedAt",
    "PostLinksPublicRequestExpiresAt",
    "PostLinksPublicRequestSplitUrlv2Item",
    "PostLinksPublicRequestTtl",
    "PostLinksPublicResponse",
    "PostLinksPublicResponseExpiresAt",
    "PostLinksPublicResponseRedirectType",
    "PostLinksPublicResponseSource",
    "PostLinksPublicResponseSplitUrlv2Item",
    "PostLinksPublicResponseTtl",
    "PostLinksPublicResponseUser",
    "PostLinksQrBulkRequestType",
    "PostLinksQrLinkIdStringRequestType",
    "PostLinksRequestCreatedAt",
    "PostLinksRequestExpiresAt",
    "PostLinksRequestSplitUrlv2Item",
    "PostLinksRequestTtl",
    "PostLinksResponse",
    "PostLinksResponseExpiresAt",
    "PostLinksResponseRedirectType",
    "PostLinksResponseSource",
    "PostLinksResponseSplitUrlv2Item",
    "PostLinksResponseTtl",
    "PostLinksResponseUser",
    "PostLinksUnarchiveBulkResponse",
    "PostLinksUnarchiveResponse",
]
