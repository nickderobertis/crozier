



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .registrations_children_list_response_item import RegistrationsChildrenListResponseItem
    from .registrations_children_list_response_item_attributes import RegistrationsChildrenListResponseItemAttributes
    from .registrations_children_list_response_item_attributes_category import (
        RegistrationsChildrenListResponseItemAttributesCategory,
    )
    from .registrations_children_list_response_item_links import RegistrationsChildrenListResponseItemLinks
    from .registrations_children_list_response_item_relationships import (
        RegistrationsChildrenListResponseItemRelationships,
    )
    from .registrations_citation_read_response import RegistrationsCitationReadResponse
    from .registrations_citation_read_response_attributes import RegistrationsCitationReadResponseAttributes
    from .registrations_citation_read_response_links import RegistrationsCitationReadResponseLinks
    from .registrations_citations_list_response_item import RegistrationsCitationsListResponseItem
    from .registrations_citations_list_response_item_attributes import RegistrationsCitationsListResponseItemAttributes
    from .registrations_comments_list_response_item import RegistrationsCommentsListResponseItem
    from .registrations_comments_list_response_item_attributes import RegistrationsCommentsListResponseItemAttributes
    from .registrations_comments_list_response_item_links import RegistrationsCommentsListResponseItemLinks
    from .registrations_comments_list_response_item_relationships import (
        RegistrationsCommentsListResponseItemRelationships,
    )
    from .registrations_contributors_list_response_item import RegistrationsContributorsListResponseItem
    from .registrations_contributors_list_response_item_attributes import (
        RegistrationsContributorsListResponseItemAttributes,
    )
    from .registrations_contributors_list_response_item_attributes_permission import (
        RegistrationsContributorsListResponseItemAttributesPermission,
    )
    from .registrations_contributors_list_response_item_links import RegistrationsContributorsListResponseItemLinks
    from .registrations_contributors_list_response_item_relationships import (
        RegistrationsContributorsListResponseItemRelationships,
    )
    from .registrations_contributors_read_response_item import RegistrationsContributorsReadResponseItem
    from .registrations_contributors_read_response_item_attributes import (
        RegistrationsContributorsReadResponseItemAttributes,
    )
    from .registrations_contributors_read_response_item_attributes_permission import (
        RegistrationsContributorsReadResponseItemAttributesPermission,
    )
    from .registrations_contributors_read_response_item_links import RegistrationsContributorsReadResponseItemLinks
    from .registrations_contributors_read_response_item_relationships import (
        RegistrationsContributorsReadResponseItemRelationships,
    )
    from .registrations_files_list_response_item import RegistrationsFilesListResponseItem
    from .registrations_files_list_response_item_attributes import RegistrationsFilesListResponseItemAttributes
    from .registrations_files_list_response_item_links import RegistrationsFilesListResponseItemLinks
    from .registrations_files_list_response_item_relationships import RegistrationsFilesListResponseItemRelationships
    from .registrations_files_read_response import RegistrationsFilesReadResponse
    from .registrations_files_read_response_attributes import RegistrationsFilesReadResponseAttributes
    from .registrations_files_read_response_links import RegistrationsFilesReadResponseLinks
    from .registrations_files_read_response_relationships import RegistrationsFilesReadResponseRelationships
    from .registrations_forks_list_response_item import RegistrationsForksListResponseItem
    from .registrations_forks_list_response_item_attributes import RegistrationsForksListResponseItemAttributes
    from .registrations_forks_list_response_item_attributes_category import (
        RegistrationsForksListResponseItemAttributesCategory,
    )
    from .registrations_forks_list_response_item_links import RegistrationsForksListResponseItemLinks
    from .registrations_forks_list_response_item_relationships import RegistrationsForksListResponseItemRelationships
    from .registrations_identifiers_list_response_item import RegistrationsIdentifiersListResponseItem
    from .registrations_identifiers_list_response_item_attributes import (
        RegistrationsIdentifiersListResponseItemAttributes,
    )
    from .registrations_identifiers_list_response_item_attributes_category import (
        RegistrationsIdentifiersListResponseItemAttributesCategory,
    )
    from .registrations_identifiers_list_response_item_links import RegistrationsIdentifiersListResponseItemLinks
    from .registrations_identifiers_list_response_item_relationships import (
        RegistrationsIdentifiersListResponseItemRelationships,
    )
    from .registrations_institutions_list_response_item import RegistrationsInstitutionsListResponseItem
    from .registrations_institutions_list_response_item_attributes import (
        RegistrationsInstitutionsListResponseItemAttributes,
    )
    from .registrations_institutions_list_response_item_links import RegistrationsInstitutionsListResponseItemLinks
    from .registrations_institutions_list_response_item_relationships import (
        RegistrationsInstitutionsListResponseItemRelationships,
    )
    from .registrations_linked_nodes_list_response_item import RegistrationsLinkedNodesListResponseItem
    from .registrations_linked_nodes_list_response_item_attributes import (
        RegistrationsLinkedNodesListResponseItemAttributes,
    )
    from .registrations_linked_nodes_list_response_item_attributes_category import (
        RegistrationsLinkedNodesListResponseItemAttributesCategory,
    )
    from .registrations_linked_nodes_list_response_item_links import RegistrationsLinkedNodesListResponseItemLinks
    from .registrations_linked_nodes_list_response_item_relationships import (
        RegistrationsLinkedNodesListResponseItemRelationships,
    )
    from .registrations_list_response_item import RegistrationsListResponseItem
    from .registrations_list_response_item_attributes import RegistrationsListResponseItemAttributes
    from .registrations_list_response_item_attributes_category import RegistrationsListResponseItemAttributesCategory
    from .registrations_list_response_item_links import RegistrationsListResponseItemLinks
    from .registrations_list_response_item_relationships import RegistrationsListResponseItemRelationships
    from .registrations_logs_list_response_item import RegistrationsLogsListResponseItem
    from .registrations_logs_list_response_item_attributes import RegistrationsLogsListResponseItemAttributes
    from .registrations_logs_list_response_item_attributes_params import (
        RegistrationsLogsListResponseItemAttributesParams,
    )
    from .registrations_logs_list_response_item_links import RegistrationsLogsListResponseItemLinks
    from .registrations_logs_list_response_item_relationships import RegistrationsLogsListResponseItemRelationships
    from .registrations_providers_list_response_item import RegistrationsProvidersListResponseItem
    from .registrations_providers_list_response_item_attributes import RegistrationsProvidersListResponseItemAttributes
    from .registrations_providers_list_response_item_links import RegistrationsProvidersListResponseItemLinks
    from .registrations_providers_list_response_item_relationships import (
        RegistrationsProvidersListResponseItemRelationships,
    )
    from .registrations_read_response import RegistrationsReadResponse
    from .registrations_read_response_attributes import RegistrationsReadResponseAttributes
    from .registrations_read_response_attributes_category import RegistrationsReadResponseAttributesCategory
    from .registrations_read_response_links import RegistrationsReadResponseLinks
    from .registrations_read_response_relationships import RegistrationsReadResponseRelationships
    from .registrations_view_only_links_list_response_item import RegistrationsViewOnlyLinksListResponseItem
    from .registrations_view_only_links_list_response_item_attributes import (
        RegistrationsViewOnlyLinksListResponseItemAttributes,
    )
    from .registrations_view_only_links_list_response_item_relationships import (
        RegistrationsViewOnlyLinksListResponseItemRelationships,
    )
    from .registrations_view_only_links_read_response import RegistrationsViewOnlyLinksReadResponse
    from .registrations_view_only_links_read_response_attributes import RegistrationsViewOnlyLinksReadResponseAttributes
    from .registrations_view_only_links_read_response_relationships import (
        RegistrationsViewOnlyLinksReadResponseRelationships,
    )
    from .registrations_wikis_list_response_item import RegistrationsWikisListResponseItem
    from .registrations_wikis_list_response_item_attributes import RegistrationsWikisListResponseItemAttributes
    from .registrations_wikis_list_response_item_links import RegistrationsWikisListResponseItemLinks
    from .registrations_wikis_list_response_item_relationships import RegistrationsWikisListResponseItemRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "RegistrationsChildrenListResponseItem": ".registrations_children_list_response_item",
    "RegistrationsChildrenListResponseItemAttributes": ".registrations_children_list_response_item_attributes",
    "RegistrationsChildrenListResponseItemAttributesCategory": ".registrations_children_list_response_item_attributes_category",
    "RegistrationsChildrenListResponseItemLinks": ".registrations_children_list_response_item_links",
    "RegistrationsChildrenListResponseItemRelationships": ".registrations_children_list_response_item_relationships",
    "RegistrationsCitationReadResponse": ".registrations_citation_read_response",
    "RegistrationsCitationReadResponseAttributes": ".registrations_citation_read_response_attributes",
    "RegistrationsCitationReadResponseLinks": ".registrations_citation_read_response_links",
    "RegistrationsCitationsListResponseItem": ".registrations_citations_list_response_item",
    "RegistrationsCitationsListResponseItemAttributes": ".registrations_citations_list_response_item_attributes",
    "RegistrationsCommentsListResponseItem": ".registrations_comments_list_response_item",
    "RegistrationsCommentsListResponseItemAttributes": ".registrations_comments_list_response_item_attributes",
    "RegistrationsCommentsListResponseItemLinks": ".registrations_comments_list_response_item_links",
    "RegistrationsCommentsListResponseItemRelationships": ".registrations_comments_list_response_item_relationships",
    "RegistrationsContributorsListResponseItem": ".registrations_contributors_list_response_item",
    "RegistrationsContributorsListResponseItemAttributes": ".registrations_contributors_list_response_item_attributes",
    "RegistrationsContributorsListResponseItemAttributesPermission": ".registrations_contributors_list_response_item_attributes_permission",
    "RegistrationsContributorsListResponseItemLinks": ".registrations_contributors_list_response_item_links",
    "RegistrationsContributorsListResponseItemRelationships": ".registrations_contributors_list_response_item_relationships",
    "RegistrationsContributorsReadResponseItem": ".registrations_contributors_read_response_item",
    "RegistrationsContributorsReadResponseItemAttributes": ".registrations_contributors_read_response_item_attributes",
    "RegistrationsContributorsReadResponseItemAttributesPermission": ".registrations_contributors_read_response_item_attributes_permission",
    "RegistrationsContributorsReadResponseItemLinks": ".registrations_contributors_read_response_item_links",
    "RegistrationsContributorsReadResponseItemRelationships": ".registrations_contributors_read_response_item_relationships",
    "RegistrationsFilesListResponseItem": ".registrations_files_list_response_item",
    "RegistrationsFilesListResponseItemAttributes": ".registrations_files_list_response_item_attributes",
    "RegistrationsFilesListResponseItemLinks": ".registrations_files_list_response_item_links",
    "RegistrationsFilesListResponseItemRelationships": ".registrations_files_list_response_item_relationships",
    "RegistrationsFilesReadResponse": ".registrations_files_read_response",
    "RegistrationsFilesReadResponseAttributes": ".registrations_files_read_response_attributes",
    "RegistrationsFilesReadResponseLinks": ".registrations_files_read_response_links",
    "RegistrationsFilesReadResponseRelationships": ".registrations_files_read_response_relationships",
    "RegistrationsForksListResponseItem": ".registrations_forks_list_response_item",
    "RegistrationsForksListResponseItemAttributes": ".registrations_forks_list_response_item_attributes",
    "RegistrationsForksListResponseItemAttributesCategory": ".registrations_forks_list_response_item_attributes_category",
    "RegistrationsForksListResponseItemLinks": ".registrations_forks_list_response_item_links",
    "RegistrationsForksListResponseItemRelationships": ".registrations_forks_list_response_item_relationships",
    "RegistrationsIdentifiersListResponseItem": ".registrations_identifiers_list_response_item",
    "RegistrationsIdentifiersListResponseItemAttributes": ".registrations_identifiers_list_response_item_attributes",
    "RegistrationsIdentifiersListResponseItemAttributesCategory": ".registrations_identifiers_list_response_item_attributes_category",
    "RegistrationsIdentifiersListResponseItemLinks": ".registrations_identifiers_list_response_item_links",
    "RegistrationsIdentifiersListResponseItemRelationships": ".registrations_identifiers_list_response_item_relationships",
    "RegistrationsInstitutionsListResponseItem": ".registrations_institutions_list_response_item",
    "RegistrationsInstitutionsListResponseItemAttributes": ".registrations_institutions_list_response_item_attributes",
    "RegistrationsInstitutionsListResponseItemLinks": ".registrations_institutions_list_response_item_links",
    "RegistrationsInstitutionsListResponseItemRelationships": ".registrations_institutions_list_response_item_relationships",
    "RegistrationsLinkedNodesListResponseItem": ".registrations_linked_nodes_list_response_item",
    "RegistrationsLinkedNodesListResponseItemAttributes": ".registrations_linked_nodes_list_response_item_attributes",
    "RegistrationsLinkedNodesListResponseItemAttributesCategory": ".registrations_linked_nodes_list_response_item_attributes_category",
    "RegistrationsLinkedNodesListResponseItemLinks": ".registrations_linked_nodes_list_response_item_links",
    "RegistrationsLinkedNodesListResponseItemRelationships": ".registrations_linked_nodes_list_response_item_relationships",
    "RegistrationsListResponseItem": ".registrations_list_response_item",
    "RegistrationsListResponseItemAttributes": ".registrations_list_response_item_attributes",
    "RegistrationsListResponseItemAttributesCategory": ".registrations_list_response_item_attributes_category",
    "RegistrationsListResponseItemLinks": ".registrations_list_response_item_links",
    "RegistrationsListResponseItemRelationships": ".registrations_list_response_item_relationships",
    "RegistrationsLogsListResponseItem": ".registrations_logs_list_response_item",
    "RegistrationsLogsListResponseItemAttributes": ".registrations_logs_list_response_item_attributes",
    "RegistrationsLogsListResponseItemAttributesParams": ".registrations_logs_list_response_item_attributes_params",
    "RegistrationsLogsListResponseItemLinks": ".registrations_logs_list_response_item_links",
    "RegistrationsLogsListResponseItemRelationships": ".registrations_logs_list_response_item_relationships",
    "RegistrationsProvidersListResponseItem": ".registrations_providers_list_response_item",
    "RegistrationsProvidersListResponseItemAttributes": ".registrations_providers_list_response_item_attributes",
    "RegistrationsProvidersListResponseItemLinks": ".registrations_providers_list_response_item_links",
    "RegistrationsProvidersListResponseItemRelationships": ".registrations_providers_list_response_item_relationships",
    "RegistrationsReadResponse": ".registrations_read_response",
    "RegistrationsReadResponseAttributes": ".registrations_read_response_attributes",
    "RegistrationsReadResponseAttributesCategory": ".registrations_read_response_attributes_category",
    "RegistrationsReadResponseLinks": ".registrations_read_response_links",
    "RegistrationsReadResponseRelationships": ".registrations_read_response_relationships",
    "RegistrationsViewOnlyLinksListResponseItem": ".registrations_view_only_links_list_response_item",
    "RegistrationsViewOnlyLinksListResponseItemAttributes": ".registrations_view_only_links_list_response_item_attributes",
    "RegistrationsViewOnlyLinksListResponseItemRelationships": ".registrations_view_only_links_list_response_item_relationships",
    "RegistrationsViewOnlyLinksReadResponse": ".registrations_view_only_links_read_response",
    "RegistrationsViewOnlyLinksReadResponseAttributes": ".registrations_view_only_links_read_response_attributes",
    "RegistrationsViewOnlyLinksReadResponseRelationships": ".registrations_view_only_links_read_response_relationships",
    "RegistrationsWikisListResponseItem": ".registrations_wikis_list_response_item",
    "RegistrationsWikisListResponseItemAttributes": ".registrations_wikis_list_response_item_attributes",
    "RegistrationsWikisListResponseItemLinks": ".registrations_wikis_list_response_item_links",
    "RegistrationsWikisListResponseItemRelationships": ".registrations_wikis_list_response_item_relationships",
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
    "RegistrationsChildrenListResponseItem",
    "RegistrationsChildrenListResponseItemAttributes",
    "RegistrationsChildrenListResponseItemAttributesCategory",
    "RegistrationsChildrenListResponseItemLinks",
    "RegistrationsChildrenListResponseItemRelationships",
    "RegistrationsCitationReadResponse",
    "RegistrationsCitationReadResponseAttributes",
    "RegistrationsCitationReadResponseLinks",
    "RegistrationsCitationsListResponseItem",
    "RegistrationsCitationsListResponseItemAttributes",
    "RegistrationsCommentsListResponseItem",
    "RegistrationsCommentsListResponseItemAttributes",
    "RegistrationsCommentsListResponseItemLinks",
    "RegistrationsCommentsListResponseItemRelationships",
    "RegistrationsContributorsListResponseItem",
    "RegistrationsContributorsListResponseItemAttributes",
    "RegistrationsContributorsListResponseItemAttributesPermission",
    "RegistrationsContributorsListResponseItemLinks",
    "RegistrationsContributorsListResponseItemRelationships",
    "RegistrationsContributorsReadResponseItem",
    "RegistrationsContributorsReadResponseItemAttributes",
    "RegistrationsContributorsReadResponseItemAttributesPermission",
    "RegistrationsContributorsReadResponseItemLinks",
    "RegistrationsContributorsReadResponseItemRelationships",
    "RegistrationsFilesListResponseItem",
    "RegistrationsFilesListResponseItemAttributes",
    "RegistrationsFilesListResponseItemLinks",
    "RegistrationsFilesListResponseItemRelationships",
    "RegistrationsFilesReadResponse",
    "RegistrationsFilesReadResponseAttributes",
    "RegistrationsFilesReadResponseLinks",
    "RegistrationsFilesReadResponseRelationships",
    "RegistrationsForksListResponseItem",
    "RegistrationsForksListResponseItemAttributes",
    "RegistrationsForksListResponseItemAttributesCategory",
    "RegistrationsForksListResponseItemLinks",
    "RegistrationsForksListResponseItemRelationships",
    "RegistrationsIdentifiersListResponseItem",
    "RegistrationsIdentifiersListResponseItemAttributes",
    "RegistrationsIdentifiersListResponseItemAttributesCategory",
    "RegistrationsIdentifiersListResponseItemLinks",
    "RegistrationsIdentifiersListResponseItemRelationships",
    "RegistrationsInstitutionsListResponseItem",
    "RegistrationsInstitutionsListResponseItemAttributes",
    "RegistrationsInstitutionsListResponseItemLinks",
    "RegistrationsInstitutionsListResponseItemRelationships",
    "RegistrationsLinkedNodesListResponseItem",
    "RegistrationsLinkedNodesListResponseItemAttributes",
    "RegistrationsLinkedNodesListResponseItemAttributesCategory",
    "RegistrationsLinkedNodesListResponseItemLinks",
    "RegistrationsLinkedNodesListResponseItemRelationships",
    "RegistrationsListResponseItem",
    "RegistrationsListResponseItemAttributes",
    "RegistrationsListResponseItemAttributesCategory",
    "RegistrationsListResponseItemLinks",
    "RegistrationsListResponseItemRelationships",
    "RegistrationsLogsListResponseItem",
    "RegistrationsLogsListResponseItemAttributes",
    "RegistrationsLogsListResponseItemAttributesParams",
    "RegistrationsLogsListResponseItemLinks",
    "RegistrationsLogsListResponseItemRelationships",
    "RegistrationsProvidersListResponseItem",
    "RegistrationsProvidersListResponseItemAttributes",
    "RegistrationsProvidersListResponseItemLinks",
    "RegistrationsProvidersListResponseItemRelationships",
    "RegistrationsReadResponse",
    "RegistrationsReadResponseAttributes",
    "RegistrationsReadResponseAttributesCategory",
    "RegistrationsReadResponseLinks",
    "RegistrationsReadResponseRelationships",
    "RegistrationsViewOnlyLinksListResponseItem",
    "RegistrationsViewOnlyLinksListResponseItemAttributes",
    "RegistrationsViewOnlyLinksListResponseItemRelationships",
    "RegistrationsViewOnlyLinksReadResponse",
    "RegistrationsViewOnlyLinksReadResponseAttributes",
    "RegistrationsViewOnlyLinksReadResponseRelationships",
    "RegistrationsWikisListResponseItem",
    "RegistrationsWikisListResponseItemAttributes",
    "RegistrationsWikisListResponseItemLinks",
    "RegistrationsWikisListResponseItemRelationships",
]
