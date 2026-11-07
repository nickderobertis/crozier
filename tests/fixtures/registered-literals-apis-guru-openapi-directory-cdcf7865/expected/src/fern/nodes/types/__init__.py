



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .nodes_addon_read_response import NodesAddonReadResponse
    from .nodes_addon_read_response_attributes import NodesAddonReadResponseAttributes
    from .nodes_addon_read_response_links import NodesAddonReadResponseLinks
    from .nodes_addons_folders_list_response_item import NodesAddonsFoldersListResponseItem
    from .nodes_addons_folders_list_response_item_attributes import NodesAddonsFoldersListResponseItemAttributes
    from .nodes_addons_folders_list_response_item_attributes_categories_item import (
        NodesAddonsFoldersListResponseItemAttributesCategoriesItem,
    )
    from .nodes_addons_list_response_item import NodesAddonsListResponseItem
    from .nodes_addons_list_response_item_attributes import NodesAddonsListResponseItemAttributes
    from .nodes_addons_list_response_item_attributes_categories_item import (
        NodesAddonsListResponseItemAttributesCategoriesItem,
    )
    from .nodes_children_create_request_attributes import NodesChildrenCreateRequestAttributes
    from .nodes_children_create_request_attributes_category import NodesChildrenCreateRequestAttributesCategory
    from .nodes_children_create_request_relationships import NodesChildrenCreateRequestRelationships
    from .nodes_children_list_response_item import NodesChildrenListResponseItem
    from .nodes_children_list_response_item_attributes import NodesChildrenListResponseItemAttributes
    from .nodes_children_list_response_item_attributes_category import NodesChildrenListResponseItemAttributesCategory
    from .nodes_children_list_response_item_links import NodesChildrenListResponseItemLinks
    from .nodes_children_list_response_item_relationships import NodesChildrenListResponseItemRelationships
    from .nodes_citation_list_response import NodesCitationListResponse
    from .nodes_citation_list_response_attributes import NodesCitationListResponseAttributes
    from .nodes_citation_list_response_links import NodesCitationListResponseLinks
    from .nodes_citation_read_response import NodesCitationReadResponse
    from .nodes_citation_read_response_attributes import NodesCitationReadResponseAttributes
    from .nodes_comment_create_request_attributes import NodesCommentCreateRequestAttributes
    from .nodes_comment_create_request_relationships import NodesCommentCreateRequestRelationships
    from .nodes_comments_list_response_item import NodesCommentsListResponseItem
    from .nodes_comments_list_response_item_attributes import NodesCommentsListResponseItemAttributes
    from .nodes_comments_list_response_item_links import NodesCommentsListResponseItemLinks
    from .nodes_comments_list_response_item_relationships import NodesCommentsListResponseItemRelationships
    from .nodes_contributors_create_request_attributes import NodesContributorsCreateRequestAttributes
    from .nodes_contributors_create_request_attributes_permission import (
        NodesContributorsCreateRequestAttributesPermission,
    )
    from .nodes_contributors_create_request_relationships import NodesContributorsCreateRequestRelationships
    from .nodes_contributors_list_response_item import NodesContributorsListResponseItem
    from .nodes_contributors_list_response_item_attributes import NodesContributorsListResponseItemAttributes
    from .nodes_contributors_list_response_item_attributes_permission import (
        NodesContributorsListResponseItemAttributesPermission,
    )
    from .nodes_contributors_list_response_item_links import NodesContributorsListResponseItemLinks
    from .nodes_contributors_list_response_item_relationships import NodesContributorsListResponseItemRelationships
    from .nodes_contributors_partial_update_request_attributes import NodesContributorsPartialUpdateRequestAttributes
    from .nodes_contributors_partial_update_request_attributes_permission import (
        NodesContributorsPartialUpdateRequestAttributesPermission,
    )
    from .nodes_contributors_partial_update_request_relationships import (
        NodesContributorsPartialUpdateRequestRelationships,
    )
    from .nodes_contributors_read_response_item import NodesContributorsReadResponseItem
    from .nodes_contributors_read_response_item_attributes import NodesContributorsReadResponseItemAttributes
    from .nodes_contributors_read_response_item_attributes_permission import (
        NodesContributorsReadResponseItemAttributesPermission,
    )
    from .nodes_contributors_read_response_item_links import NodesContributorsReadResponseItemLinks
    from .nodes_contributors_read_response_item_relationships import NodesContributorsReadResponseItemRelationships
    from .nodes_create_request_attributes import NodesCreateRequestAttributes
    from .nodes_create_request_attributes_category import NodesCreateRequestAttributesCategory
    from .nodes_create_request_relationships import NodesCreateRequestRelationships
    from .nodes_draft_registrations_create_request_attributes import NodesDraftRegistrationsCreateRequestAttributes
    from .nodes_draft_registrations_create_request_attributes_node_license import (
        NodesDraftRegistrationsCreateRequestAttributesNodeLicense,
    )
    from .nodes_draft_registrations_list_response_item import NodesDraftRegistrationsListResponseItem
    from .nodes_draft_registrations_list_response_item_attributes import (
        NodesDraftRegistrationsListResponseItemAttributes,
    )
    from .nodes_draft_registrations_list_response_item_attributes_node_license import (
        NodesDraftRegistrationsListResponseItemAttributesNodeLicense,
    )
    from .nodes_draft_registrations_list_response_item_links import NodesDraftRegistrationsListResponseItemLinks
    from .nodes_draft_registrations_list_response_item_relationships import (
        NodesDraftRegistrationsListResponseItemRelationships,
    )
    from .nodes_draft_registrations_partial_update_request_attributes import (
        NodesDraftRegistrationsPartialUpdateRequestAttributes,
    )
    from .nodes_draft_registrations_partial_update_request_attributes_node_license import (
        NodesDraftRegistrationsPartialUpdateRequestAttributesNodeLicense,
    )
    from .nodes_files_list_response_item import NodesFilesListResponseItem
    from .nodes_files_list_response_item_attributes import NodesFilesListResponseItemAttributes
    from .nodes_files_list_response_item_links import NodesFilesListResponseItemLinks
    from .nodes_files_list_response_item_relationships import NodesFilesListResponseItemRelationships
    from .nodes_files_read_response import NodesFilesReadResponse
    from .nodes_files_read_response_attributes import NodesFilesReadResponseAttributes
    from .nodes_files_read_response_links import NodesFilesReadResponseLinks
    from .nodes_files_read_response_relationships import NodesFilesReadResponseRelationships
    from .nodes_forks_create_request_attributes import NodesForksCreateRequestAttributes
    from .nodes_forks_create_request_attributes_category import NodesForksCreateRequestAttributesCategory
    from .nodes_forks_create_request_relationships import NodesForksCreateRequestRelationships
    from .nodes_forks_list_response_item import NodesForksListResponseItem
    from .nodes_forks_list_response_item_attributes import NodesForksListResponseItemAttributes
    from .nodes_forks_list_response_item_attributes_category import NodesForksListResponseItemAttributesCategory
    from .nodes_forks_list_response_item_links import NodesForksListResponseItemLinks
    from .nodes_forks_list_response_item_relationships import NodesForksListResponseItemRelationships
    from .nodes_identifiers_list_response_item import NodesIdentifiersListResponseItem
    from .nodes_identifiers_list_response_item_attributes import NodesIdentifiersListResponseItemAttributes
    from .nodes_identifiers_list_response_item_attributes_category import (
        NodesIdentifiersListResponseItemAttributesCategory,
    )
    from .nodes_identifiers_list_response_item_links import NodesIdentifiersListResponseItemLinks
    from .nodes_identifiers_list_response_item_relationships import NodesIdentifiersListResponseItemRelationships
    from .nodes_institutions_list_response_item import NodesInstitutionsListResponseItem
    from .nodes_institutions_list_response_item_attributes import NodesInstitutionsListResponseItemAttributes
    from .nodes_institutions_list_response_item_links import NodesInstitutionsListResponseItemLinks
    from .nodes_institutions_list_response_item_relationships import NodesInstitutionsListResponseItemRelationships
    from .nodes_linked_nodes_list_response_item import NodesLinkedNodesListResponseItem
    from .nodes_linked_nodes_list_response_item_attributes import NodesLinkedNodesListResponseItemAttributes
    from .nodes_linked_nodes_list_response_item_attributes_category import (
        NodesLinkedNodesListResponseItemAttributesCategory,
    )
    from .nodes_linked_nodes_list_response_item_links import NodesLinkedNodesListResponseItemLinks
    from .nodes_linked_nodes_list_response_item_relationships import NodesLinkedNodesListResponseItemRelationships
    from .nodes_list_response_item import NodesListResponseItem
    from .nodes_list_response_item_attributes import NodesListResponseItemAttributes
    from .nodes_list_response_item_attributes_category import NodesListResponseItemAttributesCategory
    from .nodes_list_response_item_links import NodesListResponseItemLinks
    from .nodes_list_response_item_relationships import NodesListResponseItemRelationships
    from .nodes_logs_list_response_item import NodesLogsListResponseItem
    from .nodes_logs_list_response_item_attributes import NodesLogsListResponseItemAttributes
    from .nodes_logs_list_response_item_attributes_params import NodesLogsListResponseItemAttributesParams
    from .nodes_logs_list_response_item_links import NodesLogsListResponseItemLinks
    from .nodes_logs_list_response_item_relationships import NodesLogsListResponseItemRelationships
    from .nodes_preprints_list_response_item import NodesPreprintsListResponseItem
    from .nodes_preprints_list_response_item_attributes import NodesPreprintsListResponseItemAttributes
    from .nodes_preprints_list_response_item_links import NodesPreprintsListResponseItemLinks
    from .nodes_preprints_list_response_item_relationships import NodesPreprintsListResponseItemRelationships
    from .nodes_providers_list_response_item import NodesProvidersListResponseItem
    from .nodes_providers_list_response_item_attributes import NodesProvidersListResponseItemAttributes
    from .nodes_providers_list_response_item_links import NodesProvidersListResponseItemLinks
    from .nodes_providers_list_response_item_relationships import NodesProvidersListResponseItemRelationships
    from .nodes_providers_read_response import NodesProvidersReadResponse
    from .nodes_providers_read_response_attributes import NodesProvidersReadResponseAttributes
    from .nodes_providers_read_response_links import NodesProvidersReadResponseLinks
    from .nodes_providers_read_response_relationships import NodesProvidersReadResponseRelationships
    from .nodes_read_response import NodesReadResponse
    from .nodes_read_response_attributes import NodesReadResponseAttributes
    from .nodes_read_response_attributes_category import NodesReadResponseAttributesCategory
    from .nodes_read_response_links import NodesReadResponseLinks
    from .nodes_read_response_relationships import NodesReadResponseRelationships
    from .nodes_registrations_list_response_item import NodesRegistrationsListResponseItem
    from .nodes_registrations_list_response_item_attributes import NodesRegistrationsListResponseItemAttributes
    from .nodes_registrations_list_response_item_attributes_category import (
        NodesRegistrationsListResponseItemAttributesCategory,
    )
    from .nodes_registrations_list_response_item_links import NodesRegistrationsListResponseItemLinks
    from .nodes_registrations_list_response_item_relationships import NodesRegistrationsListResponseItemRelationships
    from .nodes_view_only_links_list_response_item import NodesViewOnlyLinksListResponseItem
    from .nodes_view_only_links_list_response_item_attributes import NodesViewOnlyLinksListResponseItemAttributes
    from .nodes_view_only_links_list_response_item_relationships import NodesViewOnlyLinksListResponseItemRelationships
    from .nodes_view_only_links_read_response import NodesViewOnlyLinksReadResponse
    from .nodes_view_only_links_read_response_attributes import NodesViewOnlyLinksReadResponseAttributes
    from .nodes_view_only_links_read_response_relationships import NodesViewOnlyLinksReadResponseRelationships
    from .nodes_wikis_list_response_item import NodesWikisListResponseItem
    from .nodes_wikis_list_response_item_attributes import NodesWikisListResponseItemAttributes
    from .nodes_wikis_list_response_item_links import NodesWikisListResponseItemLinks
    from .nodes_wikis_list_response_item_relationships import NodesWikisListResponseItemRelationships
_dynamic_imports: typing.Dict[str, str] = {
    "NodesAddonReadResponse": ".nodes_addon_read_response",
    "NodesAddonReadResponseAttributes": ".nodes_addon_read_response_attributes",
    "NodesAddonReadResponseLinks": ".nodes_addon_read_response_links",
    "NodesAddonsFoldersListResponseItem": ".nodes_addons_folders_list_response_item",
    "NodesAddonsFoldersListResponseItemAttributes": ".nodes_addons_folders_list_response_item_attributes",
    "NodesAddonsFoldersListResponseItemAttributesCategoriesItem": ".nodes_addons_folders_list_response_item_attributes_categories_item",
    "NodesAddonsListResponseItem": ".nodes_addons_list_response_item",
    "NodesAddonsListResponseItemAttributes": ".nodes_addons_list_response_item_attributes",
    "NodesAddonsListResponseItemAttributesCategoriesItem": ".nodes_addons_list_response_item_attributes_categories_item",
    "NodesChildrenCreateRequestAttributes": ".nodes_children_create_request_attributes",
    "NodesChildrenCreateRequestAttributesCategory": ".nodes_children_create_request_attributes_category",
    "NodesChildrenCreateRequestRelationships": ".nodes_children_create_request_relationships",
    "NodesChildrenListResponseItem": ".nodes_children_list_response_item",
    "NodesChildrenListResponseItemAttributes": ".nodes_children_list_response_item_attributes",
    "NodesChildrenListResponseItemAttributesCategory": ".nodes_children_list_response_item_attributes_category",
    "NodesChildrenListResponseItemLinks": ".nodes_children_list_response_item_links",
    "NodesChildrenListResponseItemRelationships": ".nodes_children_list_response_item_relationships",
    "NodesCitationListResponse": ".nodes_citation_list_response",
    "NodesCitationListResponseAttributes": ".nodes_citation_list_response_attributes",
    "NodesCitationListResponseLinks": ".nodes_citation_list_response_links",
    "NodesCitationReadResponse": ".nodes_citation_read_response",
    "NodesCitationReadResponseAttributes": ".nodes_citation_read_response_attributes",
    "NodesCommentCreateRequestAttributes": ".nodes_comment_create_request_attributes",
    "NodesCommentCreateRequestRelationships": ".nodes_comment_create_request_relationships",
    "NodesCommentsListResponseItem": ".nodes_comments_list_response_item",
    "NodesCommentsListResponseItemAttributes": ".nodes_comments_list_response_item_attributes",
    "NodesCommentsListResponseItemLinks": ".nodes_comments_list_response_item_links",
    "NodesCommentsListResponseItemRelationships": ".nodes_comments_list_response_item_relationships",
    "NodesContributorsCreateRequestAttributes": ".nodes_contributors_create_request_attributes",
    "NodesContributorsCreateRequestAttributesPermission": ".nodes_contributors_create_request_attributes_permission",
    "NodesContributorsCreateRequestRelationships": ".nodes_contributors_create_request_relationships",
    "NodesContributorsListResponseItem": ".nodes_contributors_list_response_item",
    "NodesContributorsListResponseItemAttributes": ".nodes_contributors_list_response_item_attributes",
    "NodesContributorsListResponseItemAttributesPermission": ".nodes_contributors_list_response_item_attributes_permission",
    "NodesContributorsListResponseItemLinks": ".nodes_contributors_list_response_item_links",
    "NodesContributorsListResponseItemRelationships": ".nodes_contributors_list_response_item_relationships",
    "NodesContributorsPartialUpdateRequestAttributes": ".nodes_contributors_partial_update_request_attributes",
    "NodesContributorsPartialUpdateRequestAttributesPermission": ".nodes_contributors_partial_update_request_attributes_permission",
    "NodesContributorsPartialUpdateRequestRelationships": ".nodes_contributors_partial_update_request_relationships",
    "NodesContributorsReadResponseItem": ".nodes_contributors_read_response_item",
    "NodesContributorsReadResponseItemAttributes": ".nodes_contributors_read_response_item_attributes",
    "NodesContributorsReadResponseItemAttributesPermission": ".nodes_contributors_read_response_item_attributes_permission",
    "NodesContributorsReadResponseItemLinks": ".nodes_contributors_read_response_item_links",
    "NodesContributorsReadResponseItemRelationships": ".nodes_contributors_read_response_item_relationships",
    "NodesCreateRequestAttributes": ".nodes_create_request_attributes",
    "NodesCreateRequestAttributesCategory": ".nodes_create_request_attributes_category",
    "NodesCreateRequestRelationships": ".nodes_create_request_relationships",
    "NodesDraftRegistrationsCreateRequestAttributes": ".nodes_draft_registrations_create_request_attributes",
    "NodesDraftRegistrationsCreateRequestAttributesNodeLicense": ".nodes_draft_registrations_create_request_attributes_node_license",
    "NodesDraftRegistrationsListResponseItem": ".nodes_draft_registrations_list_response_item",
    "NodesDraftRegistrationsListResponseItemAttributes": ".nodes_draft_registrations_list_response_item_attributes",
    "NodesDraftRegistrationsListResponseItemAttributesNodeLicense": ".nodes_draft_registrations_list_response_item_attributes_node_license",
    "NodesDraftRegistrationsListResponseItemLinks": ".nodes_draft_registrations_list_response_item_links",
    "NodesDraftRegistrationsListResponseItemRelationships": ".nodes_draft_registrations_list_response_item_relationships",
    "NodesDraftRegistrationsPartialUpdateRequestAttributes": ".nodes_draft_registrations_partial_update_request_attributes",
    "NodesDraftRegistrationsPartialUpdateRequestAttributesNodeLicense": ".nodes_draft_registrations_partial_update_request_attributes_node_license",
    "NodesFilesListResponseItem": ".nodes_files_list_response_item",
    "NodesFilesListResponseItemAttributes": ".nodes_files_list_response_item_attributes",
    "NodesFilesListResponseItemLinks": ".nodes_files_list_response_item_links",
    "NodesFilesListResponseItemRelationships": ".nodes_files_list_response_item_relationships",
    "NodesFilesReadResponse": ".nodes_files_read_response",
    "NodesFilesReadResponseAttributes": ".nodes_files_read_response_attributes",
    "NodesFilesReadResponseLinks": ".nodes_files_read_response_links",
    "NodesFilesReadResponseRelationships": ".nodes_files_read_response_relationships",
    "NodesForksCreateRequestAttributes": ".nodes_forks_create_request_attributes",
    "NodesForksCreateRequestAttributesCategory": ".nodes_forks_create_request_attributes_category",
    "NodesForksCreateRequestRelationships": ".nodes_forks_create_request_relationships",
    "NodesForksListResponseItem": ".nodes_forks_list_response_item",
    "NodesForksListResponseItemAttributes": ".nodes_forks_list_response_item_attributes",
    "NodesForksListResponseItemAttributesCategory": ".nodes_forks_list_response_item_attributes_category",
    "NodesForksListResponseItemLinks": ".nodes_forks_list_response_item_links",
    "NodesForksListResponseItemRelationships": ".nodes_forks_list_response_item_relationships",
    "NodesIdentifiersListResponseItem": ".nodes_identifiers_list_response_item",
    "NodesIdentifiersListResponseItemAttributes": ".nodes_identifiers_list_response_item_attributes",
    "NodesIdentifiersListResponseItemAttributesCategory": ".nodes_identifiers_list_response_item_attributes_category",
    "NodesIdentifiersListResponseItemLinks": ".nodes_identifiers_list_response_item_links",
    "NodesIdentifiersListResponseItemRelationships": ".nodes_identifiers_list_response_item_relationships",
    "NodesInstitutionsListResponseItem": ".nodes_institutions_list_response_item",
    "NodesInstitutionsListResponseItemAttributes": ".nodes_institutions_list_response_item_attributes",
    "NodesInstitutionsListResponseItemLinks": ".nodes_institutions_list_response_item_links",
    "NodesInstitutionsListResponseItemRelationships": ".nodes_institutions_list_response_item_relationships",
    "NodesLinkedNodesListResponseItem": ".nodes_linked_nodes_list_response_item",
    "NodesLinkedNodesListResponseItemAttributes": ".nodes_linked_nodes_list_response_item_attributes",
    "NodesLinkedNodesListResponseItemAttributesCategory": ".nodes_linked_nodes_list_response_item_attributes_category",
    "NodesLinkedNodesListResponseItemLinks": ".nodes_linked_nodes_list_response_item_links",
    "NodesLinkedNodesListResponseItemRelationships": ".nodes_linked_nodes_list_response_item_relationships",
    "NodesListResponseItem": ".nodes_list_response_item",
    "NodesListResponseItemAttributes": ".nodes_list_response_item_attributes",
    "NodesListResponseItemAttributesCategory": ".nodes_list_response_item_attributes_category",
    "NodesListResponseItemLinks": ".nodes_list_response_item_links",
    "NodesListResponseItemRelationships": ".nodes_list_response_item_relationships",
    "NodesLogsListResponseItem": ".nodes_logs_list_response_item",
    "NodesLogsListResponseItemAttributes": ".nodes_logs_list_response_item_attributes",
    "NodesLogsListResponseItemAttributesParams": ".nodes_logs_list_response_item_attributes_params",
    "NodesLogsListResponseItemLinks": ".nodes_logs_list_response_item_links",
    "NodesLogsListResponseItemRelationships": ".nodes_logs_list_response_item_relationships",
    "NodesPreprintsListResponseItem": ".nodes_preprints_list_response_item",
    "NodesPreprintsListResponseItemAttributes": ".nodes_preprints_list_response_item_attributes",
    "NodesPreprintsListResponseItemLinks": ".nodes_preprints_list_response_item_links",
    "NodesPreprintsListResponseItemRelationships": ".nodes_preprints_list_response_item_relationships",
    "NodesProvidersListResponseItem": ".nodes_providers_list_response_item",
    "NodesProvidersListResponseItemAttributes": ".nodes_providers_list_response_item_attributes",
    "NodesProvidersListResponseItemLinks": ".nodes_providers_list_response_item_links",
    "NodesProvidersListResponseItemRelationships": ".nodes_providers_list_response_item_relationships",
    "NodesProvidersReadResponse": ".nodes_providers_read_response",
    "NodesProvidersReadResponseAttributes": ".nodes_providers_read_response_attributes",
    "NodesProvidersReadResponseLinks": ".nodes_providers_read_response_links",
    "NodesProvidersReadResponseRelationships": ".nodes_providers_read_response_relationships",
    "NodesReadResponse": ".nodes_read_response",
    "NodesReadResponseAttributes": ".nodes_read_response_attributes",
    "NodesReadResponseAttributesCategory": ".nodes_read_response_attributes_category",
    "NodesReadResponseLinks": ".nodes_read_response_links",
    "NodesReadResponseRelationships": ".nodes_read_response_relationships",
    "NodesRegistrationsListResponseItem": ".nodes_registrations_list_response_item",
    "NodesRegistrationsListResponseItemAttributes": ".nodes_registrations_list_response_item_attributes",
    "NodesRegistrationsListResponseItemAttributesCategory": ".nodes_registrations_list_response_item_attributes_category",
    "NodesRegistrationsListResponseItemLinks": ".nodes_registrations_list_response_item_links",
    "NodesRegistrationsListResponseItemRelationships": ".nodes_registrations_list_response_item_relationships",
    "NodesViewOnlyLinksListResponseItem": ".nodes_view_only_links_list_response_item",
    "NodesViewOnlyLinksListResponseItemAttributes": ".nodes_view_only_links_list_response_item_attributes",
    "NodesViewOnlyLinksListResponseItemRelationships": ".nodes_view_only_links_list_response_item_relationships",
    "NodesViewOnlyLinksReadResponse": ".nodes_view_only_links_read_response",
    "NodesViewOnlyLinksReadResponseAttributes": ".nodes_view_only_links_read_response_attributes",
    "NodesViewOnlyLinksReadResponseRelationships": ".nodes_view_only_links_read_response_relationships",
    "NodesWikisListResponseItem": ".nodes_wikis_list_response_item",
    "NodesWikisListResponseItemAttributes": ".nodes_wikis_list_response_item_attributes",
    "NodesWikisListResponseItemLinks": ".nodes_wikis_list_response_item_links",
    "NodesWikisListResponseItemRelationships": ".nodes_wikis_list_response_item_relationships",
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
    "NodesAddonReadResponse",
    "NodesAddonReadResponseAttributes",
    "NodesAddonReadResponseLinks",
    "NodesAddonsFoldersListResponseItem",
    "NodesAddonsFoldersListResponseItemAttributes",
    "NodesAddonsFoldersListResponseItemAttributesCategoriesItem",
    "NodesAddonsListResponseItem",
    "NodesAddonsListResponseItemAttributes",
    "NodesAddonsListResponseItemAttributesCategoriesItem",
    "NodesChildrenCreateRequestAttributes",
    "NodesChildrenCreateRequestAttributesCategory",
    "NodesChildrenCreateRequestRelationships",
    "NodesChildrenListResponseItem",
    "NodesChildrenListResponseItemAttributes",
    "NodesChildrenListResponseItemAttributesCategory",
    "NodesChildrenListResponseItemLinks",
    "NodesChildrenListResponseItemRelationships",
    "NodesCitationListResponse",
    "NodesCitationListResponseAttributes",
    "NodesCitationListResponseLinks",
    "NodesCitationReadResponse",
    "NodesCitationReadResponseAttributes",
    "NodesCommentCreateRequestAttributes",
    "NodesCommentCreateRequestRelationships",
    "NodesCommentsListResponseItem",
    "NodesCommentsListResponseItemAttributes",
    "NodesCommentsListResponseItemLinks",
    "NodesCommentsListResponseItemRelationships",
    "NodesContributorsCreateRequestAttributes",
    "NodesContributorsCreateRequestAttributesPermission",
    "NodesContributorsCreateRequestRelationships",
    "NodesContributorsListResponseItem",
    "NodesContributorsListResponseItemAttributes",
    "NodesContributorsListResponseItemAttributesPermission",
    "NodesContributorsListResponseItemLinks",
    "NodesContributorsListResponseItemRelationships",
    "NodesContributorsPartialUpdateRequestAttributes",
    "NodesContributorsPartialUpdateRequestAttributesPermission",
    "NodesContributorsPartialUpdateRequestRelationships",
    "NodesContributorsReadResponseItem",
    "NodesContributorsReadResponseItemAttributes",
    "NodesContributorsReadResponseItemAttributesPermission",
    "NodesContributorsReadResponseItemLinks",
    "NodesContributorsReadResponseItemRelationships",
    "NodesCreateRequestAttributes",
    "NodesCreateRequestAttributesCategory",
    "NodesCreateRequestRelationships",
    "NodesDraftRegistrationsCreateRequestAttributes",
    "NodesDraftRegistrationsCreateRequestAttributesNodeLicense",
    "NodesDraftRegistrationsListResponseItem",
    "NodesDraftRegistrationsListResponseItemAttributes",
    "NodesDraftRegistrationsListResponseItemAttributesNodeLicense",
    "NodesDraftRegistrationsListResponseItemLinks",
    "NodesDraftRegistrationsListResponseItemRelationships",
    "NodesDraftRegistrationsPartialUpdateRequestAttributes",
    "NodesDraftRegistrationsPartialUpdateRequestAttributesNodeLicense",
    "NodesFilesListResponseItem",
    "NodesFilesListResponseItemAttributes",
    "NodesFilesListResponseItemLinks",
    "NodesFilesListResponseItemRelationships",
    "NodesFilesReadResponse",
    "NodesFilesReadResponseAttributes",
    "NodesFilesReadResponseLinks",
    "NodesFilesReadResponseRelationships",
    "NodesForksCreateRequestAttributes",
    "NodesForksCreateRequestAttributesCategory",
    "NodesForksCreateRequestRelationships",
    "NodesForksListResponseItem",
    "NodesForksListResponseItemAttributes",
    "NodesForksListResponseItemAttributesCategory",
    "NodesForksListResponseItemLinks",
    "NodesForksListResponseItemRelationships",
    "NodesIdentifiersListResponseItem",
    "NodesIdentifiersListResponseItemAttributes",
    "NodesIdentifiersListResponseItemAttributesCategory",
    "NodesIdentifiersListResponseItemLinks",
    "NodesIdentifiersListResponseItemRelationships",
    "NodesInstitutionsListResponseItem",
    "NodesInstitutionsListResponseItemAttributes",
    "NodesInstitutionsListResponseItemLinks",
    "NodesInstitutionsListResponseItemRelationships",
    "NodesLinkedNodesListResponseItem",
    "NodesLinkedNodesListResponseItemAttributes",
    "NodesLinkedNodesListResponseItemAttributesCategory",
    "NodesLinkedNodesListResponseItemLinks",
    "NodesLinkedNodesListResponseItemRelationships",
    "NodesListResponseItem",
    "NodesListResponseItemAttributes",
    "NodesListResponseItemAttributesCategory",
    "NodesListResponseItemLinks",
    "NodesListResponseItemRelationships",
    "NodesLogsListResponseItem",
    "NodesLogsListResponseItemAttributes",
    "NodesLogsListResponseItemAttributesParams",
    "NodesLogsListResponseItemLinks",
    "NodesLogsListResponseItemRelationships",
    "NodesPreprintsListResponseItem",
    "NodesPreprintsListResponseItemAttributes",
    "NodesPreprintsListResponseItemLinks",
    "NodesPreprintsListResponseItemRelationships",
    "NodesProvidersListResponseItem",
    "NodesProvidersListResponseItemAttributes",
    "NodesProvidersListResponseItemLinks",
    "NodesProvidersListResponseItemRelationships",
    "NodesProvidersReadResponse",
    "NodesProvidersReadResponseAttributes",
    "NodesProvidersReadResponseLinks",
    "NodesProvidersReadResponseRelationships",
    "NodesReadResponse",
    "NodesReadResponseAttributes",
    "NodesReadResponseAttributesCategory",
    "NodesReadResponseLinks",
    "NodesReadResponseRelationships",
    "NodesRegistrationsListResponseItem",
    "NodesRegistrationsListResponseItemAttributes",
    "NodesRegistrationsListResponseItemAttributesCategory",
    "NodesRegistrationsListResponseItemLinks",
    "NodesRegistrationsListResponseItemRelationships",
    "NodesViewOnlyLinksListResponseItem",
    "NodesViewOnlyLinksListResponseItemAttributes",
    "NodesViewOnlyLinksListResponseItemRelationships",
    "NodesViewOnlyLinksReadResponse",
    "NodesViewOnlyLinksReadResponseAttributes",
    "NodesViewOnlyLinksReadResponseRelationships",
    "NodesWikisListResponseItem",
    "NodesWikisListResponseItemAttributes",
    "NodesWikisListResponseItemLinks",
    "NodesWikisListResponseItemRelationships",
]
