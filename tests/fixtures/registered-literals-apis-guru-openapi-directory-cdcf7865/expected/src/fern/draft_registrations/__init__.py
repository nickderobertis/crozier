



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DraftRegistrationContributorsCreateRequestAttributes,
        DraftRegistrationContributorsCreateRequestAttributesPermission,
        DraftRegistrationContributorsCreateRequestRelationships,
        DraftRegistrationsCreateRequestAttributes,
        DraftRegistrationsCreateRequestAttributesNodeLicense,
        DraftRegistrationsCreateResponse,
        DraftRegistrationsCreateResponseAttributes,
        DraftRegistrationsCreateResponseAttributesNodeLicense,
        DraftRegistrationsCreateResponseLinks,
        DraftRegistrationsCreateResponseRelationships,
        DraftRegistrationsReadResponse,
        DraftRegistrationsReadResponseAttributes,
        DraftRegistrationsReadResponseAttributesNodeLicense,
        DraftRegistrationsReadResponseLinks,
        DraftRegistrationsReadResponseRelationships,
        GetDraftRegistrationsDraftIdInstitutionsResponse,
        GetDraftRegistrationsDraftIdInstitutionsResponseAttributes,
        GetDraftRegistrationsDraftIdInstitutionsResponseLinks,
        GetDraftRegistrationsDraftIdInstitutionsResponseRelationships,
        GetDraftRegistrationsDraftIdResponse,
        GetDraftRegistrationsDraftIdResponseAttributes,
        GetDraftRegistrationsDraftIdResponseAttributesNodeLicense,
        GetDraftRegistrationsDraftIdResponseLinks,
        GetDraftRegistrationsDraftIdResponseRelationships,
        NodesDraftRegistrationsReadResponse,
        NodesDraftRegistrationsReadResponseAttributes,
        NodesDraftRegistrationsReadResponseAttributesNodeLicense,
        NodesDraftRegistrationsReadResponseLinks,
        NodesDraftRegistrationsReadResponseRelationships,
        NodesDraftRegistrationsSubjectsResponse,
        NodesDraftRegistrationsSubjectsResponseAttributes,
        NodesDraftRegistrationsSubjectsResponseEmbeds,
        NodesDraftRegistrationsSubjectsResponseEmbedsParent,
        NodesDraftRegistrationsSubjectsResponseEmbedsParentData,
        NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes,
        NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships,
        NodesDraftRegistrationsSubjectsResponseLinks,
        NodesDraftRegistrationsSubjectsResponseRelationships,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DraftRegistrationContributorsCreateRequestAttributes": ".types",
    "DraftRegistrationContributorsCreateRequestAttributesPermission": ".types",
    "DraftRegistrationContributorsCreateRequestRelationships": ".types",
    "DraftRegistrationsCreateRequestAttributes": ".types",
    "DraftRegistrationsCreateRequestAttributesNodeLicense": ".types",
    "DraftRegistrationsCreateResponse": ".types",
    "DraftRegistrationsCreateResponseAttributes": ".types",
    "DraftRegistrationsCreateResponseAttributesNodeLicense": ".types",
    "DraftRegistrationsCreateResponseLinks": ".types",
    "DraftRegistrationsCreateResponseRelationships": ".types",
    "DraftRegistrationsReadResponse": ".types",
    "DraftRegistrationsReadResponseAttributes": ".types",
    "DraftRegistrationsReadResponseAttributesNodeLicense": ".types",
    "DraftRegistrationsReadResponseLinks": ".types",
    "DraftRegistrationsReadResponseRelationships": ".types",
    "GetDraftRegistrationsDraftIdInstitutionsResponse": ".types",
    "GetDraftRegistrationsDraftIdInstitutionsResponseAttributes": ".types",
    "GetDraftRegistrationsDraftIdInstitutionsResponseLinks": ".types",
    "GetDraftRegistrationsDraftIdInstitutionsResponseRelationships": ".types",
    "GetDraftRegistrationsDraftIdResponse": ".types",
    "GetDraftRegistrationsDraftIdResponseAttributes": ".types",
    "GetDraftRegistrationsDraftIdResponseAttributesNodeLicense": ".types",
    "GetDraftRegistrationsDraftIdResponseLinks": ".types",
    "GetDraftRegistrationsDraftIdResponseRelationships": ".types",
    "NodesDraftRegistrationsReadResponse": ".types",
    "NodesDraftRegistrationsReadResponseAttributes": ".types",
    "NodesDraftRegistrationsReadResponseAttributesNodeLicense": ".types",
    "NodesDraftRegistrationsReadResponseLinks": ".types",
    "NodesDraftRegistrationsReadResponseRelationships": ".types",
    "NodesDraftRegistrationsSubjectsResponse": ".types",
    "NodesDraftRegistrationsSubjectsResponseAttributes": ".types",
    "NodesDraftRegistrationsSubjectsResponseEmbeds": ".types",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParent": ".types",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentData": ".types",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataAttributes": ".types",
    "NodesDraftRegistrationsSubjectsResponseEmbedsParentDataRelationships": ".types",
    "NodesDraftRegistrationsSubjectsResponseLinks": ".types",
    "NodesDraftRegistrationsSubjectsResponseRelationships": ".types",
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
