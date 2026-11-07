



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .draft_registration_contributors_create_request_attributes import (
        DraftRegistrationContributorsCreateRequestAttributes,
    )
    from .draft_registration_contributors_create_request_attributes_permission import (
        DraftRegistrationContributorsCreateRequestAttributesPermission,
    )
    from .draft_registration_contributors_create_request_relationships import (
        DraftRegistrationContributorsCreateRequestRelationships,
    )
    from .draft_registrations_create_request_attributes import DraftRegistrationsCreateRequestAttributes
    from .draft_registrations_create_request_attributes_node_license import (
        DraftRegistrationsCreateRequestAttributesNodeLicense,
    )
    from .draft_registrations_create_response import DraftRegistrationsCreateResponse
    from .draft_registrations_create_response_attributes import DraftRegistrationsCreateResponseAttributes
    from .draft_registrations_create_response_attributes_node_license import (
        DraftRegistrationsCreateResponseAttributesNodeLicense,
    )
    from .draft_registrations_create_response_links import DraftRegistrationsCreateResponseLinks
    from .draft_registrations_create_response_relationships import DraftRegistrationsCreateResponseRelationships
    from .draft_registrations_read_response import DraftRegistrationsReadResponse
    from .draft_registrations_read_response_attributes import DraftRegistrationsReadResponseAttributes
    from .draft_registrations_read_response_attributes_node_license import (
        DraftRegistrationsReadResponseAttributesNodeLicense,
    )
    from .draft_registrations_read_response_links import DraftRegistrationsReadResponseLinks
    from .draft_registrations_read_response_relationships import DraftRegistrationsReadResponseRelationships
    from .get_draft_registrations_draft_id_institutions_response import GetDraftRegistrationsDraftIdInstitutionsResponse
    from .get_draft_registrations_draft_id_institutions_response_attributes import (
        GetDraftRegistrationsDraftIdInstitutionsResponseAttributes,
    )
    from .get_draft_registrations_draft_id_institutions_response_links import (
        GetDraftRegistrationsDraftIdInstitutionsResponseLinks,
    )
    from .get_draft_registrations_draft_id_institutions_response_relationships import (
        GetDraftRegistrationsDraftIdInstitutionsResponseRelationships,
    )
    from .get_draft_registrations_draft_id_response import GetDraftRegistrationsDraftIdResponse
    from .get_draft_registrations_draft_id_response_attributes import GetDraftRegistrationsDraftIdResponseAttributes
    from .get_draft_registrations_draft_id_response_attributes_node_license import (
        GetDraftRegistrationsDraftIdResponseAttributesNodeLicense,
    )
    from .get_draft_registrations_draft_id_response_links import GetDraftRegistrationsDraftIdResponseLinks
    from .get_draft_registrations_draft_id_response_relationships import (
        GetDraftRegistrationsDraftIdResponseRelationships,
    )
    from .nodes_draft_registrations_read_response import NodesDraftRegistrationsReadResponse
    from .nodes_draft_registrations_read_response_attributes import NodesDraftRegistrationsReadResponseAttributes
    from .nodes_draft_registrations_read_response_attributes_node_license import (
        NodesDraftRegistrationsReadResponseAttributesNodeLicense,
    )
    from .nodes_draft_registrations_read_response_links import NodesDraftRegistrationsReadResponseLinks
    from .nodes_draft_registrations_read_response_relationships import NodesDraftRegistrationsReadResponseRelationships
    from .nodes_draft_registrations_subjects_response import NodesDraftRegistrationsSubjectsResponse
    from .nodes_draft_registrations_subjects_response_attributes import (
        NodesDraftRegistrationsSubjectsResponseAttributes,
    )
    from .nodes_draft_registrations_subjects_response_embeds import NodesDraftRegistrationsSubjectsResponseEmbeds
    from .nodes_draft_registrations_subjects_response_embeds_parent import (
        NodesDraftRegistrationsSubjectsResponseEmbedsParent,
    )
    from .nodes_draft_registrations_subjects_response_embeds_parent_data import (
        NodesDraftRegistrationsSubjectsResponseEmbedsParentData,
    )
    from .nodes_draft_registrations_subjects_response_embeds_parent_data_attributes import (
        NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes,
    )
    from .nodes_draft_registrations_subjects_response_embeds_parent_data_relationships import (
        NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships,
    )
    from .nodes_draft_registrations_subjects_response_links import NodesDraftRegistrationsSubjectsResponseLinks
    from .nodes_draft_registrations_subjects_response_relationships import (
        NodesDraftRegistrationsSubjectsResponseRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DraftRegistrationContributorsCreateRequestAttributes": ".draft_registration_contributors_create_request_attributes",
    "DraftRegistrationContributorsCreateRequestAttributesPermission": ".draft_registration_contributors_create_request_attributes_permission",
    "DraftRegistrationContributorsCreateRequestRelationships": ".draft_registration_contributors_create_request_relationships",
    "DraftRegistrationsCreateRequestAttributes": ".draft_registrations_create_request_attributes",
    "DraftRegistrationsCreateRequestAttributesNodeLicense": ".draft_registrations_create_request_attributes_node_license",
    "DraftRegistrationsCreateResponse": ".draft_registrations_create_response",
    "DraftRegistrationsCreateResponseAttributes": ".draft_registrations_create_response_attributes",
    "DraftRegistrationsCreateResponseAttributesNodeLicense": ".draft_registrations_create_response_attributes_node_license",
    "DraftRegistrationsCreateResponseLinks": ".draft_registrations_create_response_links",
    "DraftRegistrationsCreateResponseRelationships": ".draft_registrations_create_response_relationships",
    "DraftRegistrationsReadResponse": ".draft_registrations_read_response",
    "DraftRegistrationsReadResponseAttributes": ".draft_registrations_read_response_attributes",
    "DraftRegistrationsReadResponseAttributesNodeLicense": ".draft_registrations_read_response_attributes_node_license",
    "DraftRegistrationsReadResponseLinks": ".draft_registrations_read_response_links",
    "DraftRegistrationsReadResponseRelationships": ".draft_registrations_read_response_relationships",
    "GetDraftRegistrationsDraftIdInstitutionsResponse": ".get_draft_registrations_draft_id_institutions_response",
    "GetDraftRegistrationsDraftIdInstitutionsResponseAttributes": ".get_draft_registrations_draft_id_institutions_response_attributes",
    "GetDraftRegistrationsDraftIdInstitutionsResponseLinks": ".get_draft_registrations_draft_id_institutions_response_links",
    "GetDraftRegistrationsDraftIdInstitutionsResponseRelationships": ".get_draft_registrations_draft_id_institutions_response_relationships",
    "GetDraftRegistrationsDraftIdResponse": ".get_draft_registrations_draft_id_response",
    "GetDraftRegistrationsDraftIdResponseAttributes": ".get_draft_registrations_draft_id_response_attributes",
    "GetDraftRegistrationsDraftIdResponseAttributesNodeLicense": ".get_draft_registrations_draft_id_response_attributes_node_license",
    "GetDraftRegistrationsDraftIdResponseLinks": ".get_draft_registrations_draft_id_response_links",
    "GetDraftRegistrationsDraftIdResponseRelationships": ".get_draft_registrations_draft_id_response_relationships",
    "NodesDraftRegistrationsReadResponse": ".nodes_draft_registrations_read_response",
    "NodesDraftRegistrationsReadResponseAttributes": ".nodes_draft_registrations_read_response_attributes",
    "NodesDraftRegistrationsReadResponseAttributesNodeLicense": ".nodes_draft_registrations_read_response_attributes_node_license",
    "NodesDraftRegistrationsReadResponseLinks": ".nodes_draft_registrations_read_response_links",
    "NodesDraftRegistrationsReadResponseRelationships": ".nodes_draft_registrations_read_response_relationships",
    "NodesDraftRegistrationsSubjectsResponse": ".nodes_draft_registrations_subjects_response",
    "NodesDraftRegistrationsSubjectsResponseAttributes": ".nodes_draft_registrations_subjects_response_attributes",
    "NodesDraftRegistrationsSubjectsResponseEmbeds": ".nodes_draft_registrations_subjects_response_embeds",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParent": ".nodes_draft_registrations_subjects_response_embeds_parent",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentData": ".nodes_draft_registrations_subjects_response_embeds_parent_data",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes": ".nodes_draft_registrations_subjects_response_embeds_parent_data_attributes",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships": ".nodes_draft_registrations_subjects_response_embeds_parent_data_relationships",
    "NodesDraftRegistrationsSubjectsResponseLinks": ".nodes_draft_registrations_subjects_response_links",
    "NodesDraftRegistrationsSubjectsResponseRelationships": ".nodes_draft_registrations_subjects_response_relationships",
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
    "DraftRegistrationContributorsCreateRequestAttributes",
    "DraftRegistrationContributorsCreateRequestAttributesPermission",
    "DraftRegistrationContributorsCreateRequestRelationships",
    "DraftRegistrationsCreateRequestAttributes",
    "DraftRegistrationsCreateRequestAttributesNodeLicense",
    "DraftRegistrationsCreateResponse",
    "DraftRegistrationsCreateResponseAttributes",
    "DraftRegistrationsCreateResponseAttributesNodeLicense",
    "DraftRegistrationsCreateResponseLinks",
    "DraftRegistrationsCreateResponseRelationships",
    "DraftRegistrationsReadResponse",
    "DraftRegistrationsReadResponseAttributes",
    "DraftRegistrationsReadResponseAttributesNodeLicense",
    "DraftRegistrationsReadResponseLinks",
    "DraftRegistrationsReadResponseRelationships",
    "GetDraftRegistrationsDraftIdInstitutionsResponse",
    "GetDraftRegistrationsDraftIdInstitutionsResponseAttributes",
    "GetDraftRegistrationsDraftIdInstitutionsResponseLinks",
    "GetDraftRegistrationsDraftIdInstitutionsResponseRelationships",
    "GetDraftRegistrationsDraftIdResponse",
    "GetDraftRegistrationsDraftIdResponseAttributes",
    "GetDraftRegistrationsDraftIdResponseAttributesNodeLicense",
    "GetDraftRegistrationsDraftIdResponseLinks",
    "GetDraftRegistrationsDraftIdResponseRelationships",
    "NodesDraftRegistrationsReadResponse",
    "NodesDraftRegistrationsReadResponseAttributes",
    "NodesDraftRegistrationsReadResponseAttributesNodeLicense",
    "NodesDraftRegistrationsReadResponseLinks",
    "NodesDraftRegistrationsReadResponseRelationships",
    "NodesDraftRegistrationsSubjectsResponse",
    "NodesDraftRegistrationsSubjectsResponseAttributes",
    "NodesDraftRegistrationsSubjectsResponseEmbeds",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParent",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentData",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships",
    "NodesDraftRegistrationsSubjectsResponseLinks",
    "NodesDraftRegistrationsSubjectsResponseRelationships",
]
