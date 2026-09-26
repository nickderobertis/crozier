



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_jobs_job_id_quotes_request_filter_status import GetJobsJobIdQuotesRequestFilterStatus
    from .get_jobs_job_id_quotes_request_sort_field import GetJobsJobIdQuotesRequestSortField
    from .get_jobs_job_id_quotes_request_sort_order import GetJobsJobIdQuotesRequestSortOrder
    from .get_jobs_request_filter_job_status import GetJobsRequestFilterJobStatus
    from .get_jobs_request_filter_job_type import GetJobsRequestFilterJobType
    from .get_jobs_request_sort_field import GetJobsRequestSortField
    from .get_jobs_request_sort_order import GetJobsRequestSortOrder
    from .post_jobs_job_id_quotes_request_sections_item import PostJobsJobIdQuotesRequestSectionsItem
    from .post_jobs_job_id_quotes_request_sections_item_favourite_section_id import (
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionId,
    )
    from .post_jobs_job_id_quotes_request_sections_item_favourite_section_id_combined import (
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdCombined,
    )
    from .post_jobs_job_id_quotes_request_sections_item_favourite_section_ids import (
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIds,
    )
    from .post_jobs_job_id_quotes_request_sections_item_favourite_section_ids_one_item import (
        PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdsOneItem,
    )
    from .post_jobs_job_id_quotes_request_sections_item_line_items_item import (
        PostJobsJobIdQuotesRequestSectionsItemLineItemsItem,
    )
    from .post_jobs_request_job_type import PostJobsRequestJobType
    from .put_jobs_job_id_quotes_quote_id_request_sections_item import PutJobsJobIdQuotesQuoteIdRequestSectionsItem
    from .put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_id import (
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionId,
    )
    from .put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_id_combined import (
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdCombined,
    )
    from .put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_ids import (
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIds,
    )
    from .put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_ids_one_item import (
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdsOneItem,
    )
    from .put_jobs_job_id_quotes_quote_id_request_sections_item_line_items_item import (
        PutJobsJobIdQuotesQuoteIdRequestSectionsItemLineItemsItem,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_id import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionId,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_id_combined import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdCombined,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_ids import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIds,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_ids_one_item import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdsOneItem,
    )
    from .put_jobs_job_id_quotes_version_version_number_request_sections_item_line_items_item import (
        PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemLineItemsItem,
    )
    from .put_jobs_job_id_request_body import PutJobsJobIdRequestBody
    from .put_jobs_job_id_request_body_customer_id import PutJobsJobIdRequestBodyCustomerId
    from .put_jobs_job_id_request_body_customer_reference import PutJobsJobIdRequestBodyCustomerReference
    from .put_jobs_job_id_request_body_description import PutJobsJobIdRequestBodyDescription
    from .put_jobs_job_id_request_body_site_id import PutJobsJobIdRequestBodySiteId
    from .put_jobs_job_id_request_body_title import PutJobsJobIdRequestBodyTitle
_dynamic_imports: typing.Dict[str, str] = {
    "GetJobsJobIdQuotesRequestFilterStatus": ".get_jobs_job_id_quotes_request_filter_status",
    "GetJobsJobIdQuotesRequestSortField": ".get_jobs_job_id_quotes_request_sort_field",
    "GetJobsJobIdQuotesRequestSortOrder": ".get_jobs_job_id_quotes_request_sort_order",
    "GetJobsRequestFilterJobStatus": ".get_jobs_request_filter_job_status",
    "GetJobsRequestFilterJobType": ".get_jobs_request_filter_job_type",
    "GetJobsRequestSortField": ".get_jobs_request_sort_field",
    "GetJobsRequestSortOrder": ".get_jobs_request_sort_order",
    "PostJobsJobIdQuotesRequestSectionsItem": ".post_jobs_job_id_quotes_request_sections_item",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionId": ".post_jobs_job_id_quotes_request_sections_item_favourite_section_id",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdCombined": ".post_jobs_job_id_quotes_request_sections_item_favourite_section_id_combined",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIds": ".post_jobs_job_id_quotes_request_sections_item_favourite_section_ids",
    "PostJobsJobIdQuotesRequestSectionsItemFavouriteSectionIdsOneItem": ".post_jobs_job_id_quotes_request_sections_item_favourite_section_ids_one_item",
    "PostJobsJobIdQuotesRequestSectionsItemLineItemsItem": ".post_jobs_job_id_quotes_request_sections_item_line_items_item",
    "PostJobsRequestJobType": ".post_jobs_request_job_type",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItem": ".put_jobs_job_id_quotes_quote_id_request_sections_item",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionId": ".put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_id",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdCombined": ".put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_id_combined",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIds": ".put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_ids",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemFavouriteSectionIdsOneItem": ".put_jobs_job_id_quotes_quote_id_request_sections_item_favourite_section_ids_one_item",
    "PutJobsJobIdQuotesQuoteIdRequestSectionsItemLineItemsItem": ".put_jobs_job_id_quotes_quote_id_request_sections_item_line_items_item",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItem": ".put_jobs_job_id_quotes_version_version_number_request_sections_item",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionId": ".put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_id",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdCombined": ".put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_id_combined",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIds": ".put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_ids",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemFavouriteSectionIdsOneItem": ".put_jobs_job_id_quotes_version_version_number_request_sections_item_favourite_section_ids_one_item",
    "PutJobsJobIdQuotesVersionVersionNumberRequestSectionsItemLineItemsItem": ".put_jobs_job_id_quotes_version_version_number_request_sections_item_line_items_item",
    "PutJobsJobIdRequestBody": ".put_jobs_job_id_request_body",
    "PutJobsJobIdRequestBodyCustomerId": ".put_jobs_job_id_request_body_customer_id",
    "PutJobsJobIdRequestBodyCustomerReference": ".put_jobs_job_id_request_body_customer_reference",
    "PutJobsJobIdRequestBodyDescription": ".put_jobs_job_id_request_body_description",
    "PutJobsJobIdRequestBodySiteId": ".put_jobs_job_id_request_body_site_id",
    "PutJobsJobIdRequestBodyTitle": ".put_jobs_job_id_request_body_title",
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
