



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .notebooks_get_response import NotebooksGetResponse
    from .notebooks_get_response_notebooks_item import NotebooksGetResponseNotebooksItem
    from .page_post_response import PagePostResponse
    from .page_post_response_data import PagePostResponseData
    from .page_post_response_data_annotations import PagePostResponseDataAnnotations
    from .page_post_response_data_annotations_annotations_item import (
        PagePostResponseDataAnnotationsAnnotationsItem,
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
    )
    from .page_post_response_data_annotations_annotations_item_block import (
        PagePostResponseDataAnnotationsAnnotationsItemBlock,
    )
    from .page_post_response_data_annotations_annotations_item_block_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_block_attributes_view_type import (
        PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType,
    )
    from .page_post_response_data_annotations_annotations_item_bold import (
        PagePostResponseDataAnnotationsAnnotationsItemBold,
    )
    from .page_post_response_data_annotations_annotations_item_bold_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_code import (
        PagePostResponseDataAnnotationsAnnotationsItemCode,
    )
    from .page_post_response_data_annotations_annotations_item_code_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_custom import (
        PagePostResponseDataAnnotationsAnnotationsItemCustom,
    )
    from .page_post_response_data_annotations_annotations_item_custom_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_highlighting import (
        PagePostResponseDataAnnotationsAnnotationsItemHighlighting,
    )
    from .page_post_response_data_annotations_annotations_item_highlighting_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_image import (
        PagePostResponseDataAnnotationsAnnotationsItemImage,
    )
    from .page_post_response_data_annotations_annotations_item_image_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemImageAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_inline import (
        PagePostResponseDataAnnotationsAnnotationsItemInline,
    )
    from .page_post_response_data_annotations_annotations_item_inline_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_italics import (
        PagePostResponseDataAnnotationsAnnotationsItemItalics,
    )
    from .page_post_response_data_annotations_annotations_item_italics_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_link import (
        PagePostResponseDataAnnotationsAnnotationsItemLink,
    )
    from .page_post_response_data_annotations_annotations_item_link_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_metadata import (
        PagePostResponseDataAnnotationsAnnotationsItemMetadata,
    )
    from .page_post_response_data_annotations_annotations_item_metadata_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_reference import (
        PagePostResponseDataAnnotationsAnnotationsItemReference,
    )
    from .page_post_response_data_annotations_annotations_item_reference_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes,
    )
    from .page_post_response_data_annotations_annotations_item_strikethrough import (
        PagePostResponseDataAnnotationsAnnotationsItemStrikethrough,
    )
    from .page_post_response_data_annotations_annotations_item_strikethrough_attributes import (
        PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes,
    )
    from .page_post_response_data_one import PagePostResponseDataOne
    from .page_post_response_data_two import PagePostResponseDataTwo
    from .query_post_response import QueryPostResponse
    from .query_post_response_data_item import QueryPostResponseDataItem
    from .query_post_response_data_item_results import QueryPostResponseDataItemResults
    from .query_post_response_data_item_results_one import QueryPostResponseDataItemResultsOne
    from .query_post_response_data_item_results_two import QueryPostResponseDataItemResultsTwo
    from .query_post_response_data_item_results_zero_item_value import QueryPostResponseDataItemResultsZeroItemValue
    from .query_request_conditions_item import QueryRequestConditionsItem
_dynamic_imports: typing.Dict[str, str] = {
    "NotebooksGetResponse": ".notebooks_get_response",
    "NotebooksGetResponseNotebooksItem": ".notebooks_get_response_notebooks_item",
    "PagePostResponse": ".page_post_response",
    "PagePostResponseData": ".page_post_response_data",
    "PagePostResponseDataAnnotations": ".page_post_response_data_annotations",
    "PagePostResponseDataAnnotationsAnnotationsItem": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItemBlock": ".page_post_response_data_annotations_annotations_item_block",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributes": ".page_post_response_data_annotations_annotations_item_block_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemBlockAttributesViewType": ".page_post_response_data_annotations_annotations_item_block_attributes_view_type",
    "PagePostResponseDataAnnotationsAnnotationsItemBold": ".page_post_response_data_annotations_annotations_item_bold",
    "PagePostResponseDataAnnotationsAnnotationsItemBoldAttributes": ".page_post_response_data_annotations_annotations_item_bold_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemCode": ".page_post_response_data_annotations_annotations_item_code",
    "PagePostResponseDataAnnotationsAnnotationsItemCodeAttributes": ".page_post_response_data_annotations_annotations_item_code_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemCustom": ".page_post_response_data_annotations_annotations_item_custom",
    "PagePostResponseDataAnnotationsAnnotationsItemCustomAttributes": ".page_post_response_data_annotations_annotations_item_custom_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlighting": ".page_post_response_data_annotations_annotations_item_highlighting",
    "PagePostResponseDataAnnotationsAnnotationsItemHighlightingAttributes": ".page_post_response_data_annotations_annotations_item_highlighting_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemImage": ".page_post_response_data_annotations_annotations_item_image",
    "PagePostResponseDataAnnotationsAnnotationsItemImageAttributes": ".page_post_response_data_annotations_annotations_item_image_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemInline": ".page_post_response_data_annotations_annotations_item_inline",
    "PagePostResponseDataAnnotationsAnnotationsItemInlineAttributes": ".page_post_response_data_annotations_annotations_item_inline_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemItalics": ".page_post_response_data_annotations_annotations_item_italics",
    "PagePostResponseDataAnnotationsAnnotationsItemItalicsAttributes": ".page_post_response_data_annotations_annotations_item_italics_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemLink": ".page_post_response_data_annotations_annotations_item_link",
    "PagePostResponseDataAnnotationsAnnotationsItemLinkAttributes": ".page_post_response_data_annotations_annotations_item_link_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadata": ".page_post_response_data_annotations_annotations_item_metadata",
    "PagePostResponseDataAnnotationsAnnotationsItemMetadataAttributes": ".page_post_response_data_annotations_annotations_item_metadata_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemReference": ".page_post_response_data_annotations_annotations_item_reference",
    "PagePostResponseDataAnnotationsAnnotationsItemReferenceAttributes": ".page_post_response_data_annotations_annotations_item_reference_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethrough": ".page_post_response_data_annotations_annotations_item_strikethrough",
    "PagePostResponseDataAnnotationsAnnotationsItemStrikethroughAttributes": ".page_post_response_data_annotations_annotations_item_strikethrough_attributes",
    "PagePostResponseDataAnnotationsAnnotationsItem_Block": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Bold": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Code": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Custom": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Highlighting": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Image": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Inline": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Italics": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Link": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Metadata": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Reference": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataAnnotationsAnnotationsItem_Strikethrough": ".page_post_response_data_annotations_annotations_item",
    "PagePostResponseDataOne": ".page_post_response_data_one",
    "PagePostResponseDataTwo": ".page_post_response_data_two",
    "QueryPostResponse": ".query_post_response",
    "QueryPostResponseDataItem": ".query_post_response_data_item",
    "QueryPostResponseDataItemResults": ".query_post_response_data_item_results",
    "QueryPostResponseDataItemResultsOne": ".query_post_response_data_item_results_one",
    "QueryPostResponseDataItemResultsTwo": ".query_post_response_data_item_results_two",
    "QueryPostResponseDataItemResultsZeroItemValue": ".query_post_response_data_item_results_zero_item_value",
    "QueryRequestConditionsItem": ".query_request_conditions_item",
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
]
