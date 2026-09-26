



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetJobsJobIdQuotesRequestFilterStatus,
        GetJobsJobIdQuotesRequestSortField,
        GetJobsJobIdQuotesRequestSortOrder,
        GetJobsRequestFilterJobStatus,
        GetJobsRequestFilterJobType,
        GetJobsRequestSortField,
        GetJobsRequestSortOrder,
        PostJobsJobIdQuotesRequestSectionsItem,
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionId,
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdCombined,
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIds,
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdsOneItem,
        PostJobsJobIdQuotesRequestSectionsItemLineItemsItem,
        PostJobsRequestJobType,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItem,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionId,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdCombined,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIds,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdsOneItem,
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemLineItemsItem,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionId,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdCombined,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIds,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdsOneItem,
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemLineItemsItem,
        PutJobsJobIdRequestBody,
        PutJobsJobIdRequestBodyCustomerId,
        PutJobsJobIdRequestBodyCustomerReference,
        PutJobsJobIdRequestBodyDescription,
        PutJobsJobIdRequestBodySiteId,
        PutJobsJobIdRequestBodyTitle,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetJobsJobIdQuotesRequestFilterStatus": ".types",
    "GetJobsJobIdQuotesRequestSortField": ".types",
    "GetJobsJobIdQuotesRequestSortOrder": ".types",
    "GetJobsRequestFilterJobStatus": ".types",
    "GetJobsRequestFilterJobType": ".types",
    "GetJobsRequestSortField": ".types",
    "GetJobsRequestSortOrder": ".types",
    "PostJobsJobIdQuotesRequestSectionsItem": ".types",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionId": ".types",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdCombined": ".types",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIds": ".types",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdsOneItem": ".types",
    "PostJobsJobIdQuotesRequestSectionsItemLineItemsItem": ".types",
    "PostJobsRequestJobType": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItem": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionId": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdCombined": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIds": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdsOneItem": ".types",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemLineItemsItem": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionId": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdCombined": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIds": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdsOneItem": ".types",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemLineItemsItem": ".types",
    "PutJobsJobIdRequestBody": ".types",
    "PutJobsJobIdRequestBodyCustomerId": ".types",
    "PutJobsJobIdRequestBodyCustomerReference": ".types",
    "PutJobsJobIdRequestBodyDescription": ".types",
    "PutJobsJobIdRequestBodySiteId": ".types",
    "PutJobsJobIdRequestBodyTitle": ".types",
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
    "GetJobsJobIdQuotesRequestFilterStatus",
    "GetJobsJobIdQuotesRequestSortField",
    "GetJobsJobIdQuotesRequestSortOrder",
    "GetJobsRequestFilterJobStatus",
    "GetJobsRequestFilterJobType",
    "GetJobsRequestSortField",
    "GetJobsRequestSortOrder",
    "PostJobsJobIdQuotesRequestSectionsItem",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionId",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdCombined",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIds",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdsOneItem",
    "PostJobsJobIdQuotesRequestSectionsItemLineItemsItem",
    "PostJobsRequestJobType",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItem",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionId",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdCombined",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIds",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdsOneItem",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemLineItemsItem",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionId",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdCombined",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIds",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdsOneItem",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemLineItemsItem",
    "PutJobsJobIdRequestBody",
    "PutJobsJobIdRequestBodyCustomerId",
    "PutJobsJobIdRequestBodyCustomerReference",
    "PutJobsJobIdRequestBodyDescription",
    "PutJobsJobIdRequestBodySiteId",
    "PutJobsJobIdRequestBodyTitle",
]
