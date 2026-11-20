



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        NotebooksGetResponse,
        NotebooksGetResponseNotebooksItem,
        PagePostResponse,
        PagePostResponseData,
        PagePostResponseDataAnnotations,
        PagePostResponseDataAnnotationsAnnotationsItem,
        PagePostResponseDataAnnotationsAnnotationsItemBlock,
        PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType,
        PagePostResponseDataAnnotationsAnnotationsItemBold,
        PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemCode,
        PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemCustom,
        PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemHighlighting,
        PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemImage,
        PagePostResponseDataAnnotationsAnnotationsItemImageAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemInline,
        PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemItalics,
        PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemLink,
        PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemMetadata,
        PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemReference,
        PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes,
        PagePostResponseDataAnnotationsAnnotationsItemStrikethrough,
        PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes,
        PagePostResponseDataAnnotationsAnnotationsItem_Block,
        PagePostResponseDataAnnotationsAnnotationsItem_Bold,
        PagePostResponseDataAnnotationsAnnotationsItem_Code,
        PagePostResponseDataAnnotationsAnnotationsItem_Custom,
        PagePostResponseDataAnnotationsAnnotationsItem_Highlighting,
        PagePostResponseDataAnnotationsAnnotationsItem_Image,
        PagePostResponseDataAnnotationsAnnotationsItem_Inline,
        PagePostResponseDataAnnotationsAnnotationsItem_Italics,
        PagePostResponseDataAnnotationsAnnotationsItem_Link,
        PagePostResponseDataAnnotationsAnnotationsItem_Metadata,
        PagePostResponseDataAnnotationsAnnotationsItem_Reference,
        PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough,
        PagePostResponseDataOne,
        PagePostResponseDataTwo,
        QueryPostResponse,
        QueryPostResponseDataItem,
        QueryPostResponseDataItemResults,
        QueryPostResponseDataItemResultsOne,
        QueryPostResponseDataItemResultsTwo,
        QueryPostResponseDataItemResultsZeroItemValue,
        QueryRequestConditionsItem,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "NotebooksGetResponse": ".types",
    "NotebooksGetResponseNotebooksItem": ".types",
    "PagePostResponse": ".types",
    "PagePostResponseData": ".types",
    "PagePostResponseDataAnnotations": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemBlock": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemBold": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemCode": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemCustom": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlighting": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemImage": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemImageAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemInline": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemItalics": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemLink": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadata": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemReference": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethrough": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Block": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Bold": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Code": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Custom": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Highlighting": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Image": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Inline": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Italics": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Link": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Metadata": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Reference": ".types",
    "PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough": ".types",
    "PagePostResponseDataOne": ".types",
    "PagePostResponseDataTwo": ".types",
    "QueryPostResponse": ".types",
    "QueryPostResponseDataItem": ".types",
    "QueryPostResponseDataItemResults": ".types",
    "QueryPostResponseDataItemResultsOne": ".types",
    "QueryPostResponseDataItemResultsTwo": ".types",
    "QueryPostResponseDataItemResultsZeroItemValue": ".types",
    "QueryRequestConditionsItem": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "NotebooksGetResponse",
    "NotebooksGetResponseNotebooksItem",
    "PagePostResponse",
    "PagePostResponseData",
    "PagePostResponseDataAnnotations",
    "PagePostResponseDataAnnotationsAnnotationsItem",
    "PagePostResponseDataAnnotationsAnnotationsItemBlock",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType",
    "PagePostResponseDataAnnotationsAnnotationsItemBold",
    "PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemCode",
    "PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemCustom",
    "PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlighting",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemImage",
    "PagePostResponseDataAnnotationsAnnotationsItemImageAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemInline",
    "PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemItalics",
    "PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemLink",
    "PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadata",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemReference",
    "PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethrough",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes",
    "PagePostResponseDataAnnotationsAnnotationsItem_Block",
    "PagePostResponseDataAnnotationsAnnotationsItem_Bold",
    "PagePostResponseDataAnnotationsAnnotationsItem_Code",
    "PagePostResponseDataAnnotationsAnnotationsItem_Custom",
    "PagePostResponseDataAnnotationsAnnotationsItem_Highlighting",
    "PagePostResponseDataAnnotationsAnnotationsItem_Image",
    "PagePostResponseDataAnnotationsAnnotationsItem_Inline",
    "PagePostResponseDataAnnotationsAnnotationsItem_Italics",
    "PagePostResponseDataAnnotationsAnnotationsItem_Link",
    "PagePostResponseDataAnnotationsAnnotationsItem_Metadata",
    "PagePostResponseDataAnnotationsAnnotationsItem_Reference",
    "PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough",
    "PagePostResponseDataOne",
    "PagePostResponseDataTwo",
    "QueryPostResponse",
    "QueryPostResponseDataItem",
    "QueryPostResponseDataItemResults",
    "QueryPostResponseDataItemResultsOne",
    "QueryPostResponseDataItemResultsTwo",
    "QueryPostResponseDataItemResultsZeroItemValue",
    "QueryRequestConditionsItem",
    "__version__",
]
