



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .basic_legacy_val import BasicLegacyVal
    from .basic_legacy_val_author import BasicLegacyValAuthor
    from .basic_legacy_val_links import BasicLegacyValLinks
    from .basic_legacy_val_privacy import BasicLegacyValPrivacy
    from .basic_legacy_val_type import BasicLegacyValType
    from .branch import Branch
    from .branch_links import BranchLinks
    from .conflict_error_body import ConflictErrorBody
    from .extended_legacy_val import ExtendedLegacyVal
    from .extended_legacy_val_author import ExtendedLegacyValAuthor
    from .extended_legacy_val_links import ExtendedLegacyValLinks
    from .extended_legacy_val_privacy import ExtendedLegacyValPrivacy
    from .extended_legacy_val_type import ExtendedLegacyValType
    from .file_revision_metadata_v1 import FileRevisionMetadataV1
    from .file_revision_metadata_v1links import FileRevisionMetadataV1Links
    from .file_revision_metadata_v1type import FileRevisionMetadataV1Type
    from .file_revision_metadata_v2 import FileRevisionMetadataV2
    from .file_revision_metadata_v2links import FileRevisionMetadataV2Links
    from .file_revision_metadata_v2type import FileRevisionMetadataV2Type
    from .forbidden_error_body import ForbiddenErrorBody
    from .internal_server_error_body import InternalServerErrorBody
    from .membership import Membership
    from .membership_role import MembershipRole
    from .membership_user import MembershipUser
    from .not_found_error_body import NotFoundErrorBody
    from .org import Org
    from .pagination_links import PaginationLinks
    from .project import Project
    from .project_author import ProjectAuthor
    from .project_author_type import ProjectAuthorType
    from .project_author_type_one import ProjectAuthorTypeOne
    from .project_author_type_zero import ProjectAuthorTypeZero
    from .project_links import ProjectLinks
    from .project_privacy import ProjectPrivacy
    from .result_set import ResultSet
    from .result_set_last_insert_rowid import ResultSetLastInsertRowid
    from .t_environment_variable import TEnvironmentVariable
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .user import User
    from .user_links import UserLinks
    from .user_type import UserType
    from .val import Val
    from .val_author import ValAuthor
    from .val_author_type import ValAuthorType
    from .val_author_type_one import ValAuthorTypeOne
    from .val_author_type_zero import ValAuthorTypeZero
    from .val_links import ValLinks
    from .val_privacy import ValPrivacy
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "BasicLegacyVal": ".basic_legacy_val",
    "BasicLegacyValAuthor": ".basic_legacy_val_author",
    "BasicLegacyValLinks": ".basic_legacy_val_links",
    "BasicLegacyValPrivacy": ".basic_legacy_val_privacy",
    "BasicLegacyValType": ".basic_legacy_val_type",
    "Branch": ".branch",
    "BranchLinks": ".branch_links",
    "ConflictErrorBody": ".conflict_error_body",
    "ExtendedLegacyVal": ".extended_legacy_val",
    "ExtendedLegacyValAuthor": ".extended_legacy_val_author",
    "ExtendedLegacyValLinks": ".extended_legacy_val_links",
    "ExtendedLegacyValPrivacy": ".extended_legacy_val_privacy",
    "ExtendedLegacyValType": ".extended_legacy_val_type",
    "FileRevisionMetadataV1": ".file_revision_metadata_v1",
    "FileRevisionMetadataV1Links": ".file_revision_metadata_v1links",
    "FileRevisionMetadataV1Type": ".file_revision_metadata_v1type",
    "FileRevisionMetadataV2": ".file_revision_metadata_v2",
    "FileRevisionMetadataV2Links": ".file_revision_metadata_v2links",
    "FileRevisionMetadataV2Type": ".file_revision_metadata_v2type",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "InternalServerErrorBody": ".internal_server_error_body",
    "Membership": ".membership",
    "MembershipRole": ".membership_role",
    "MembershipUser": ".membership_user",
    "NotFoundErrorBody": ".not_found_error_body",
    "Org": ".org",
    "PaginationLinks": ".pagination_links",
    "Project": ".project",
    "ProjectAuthor": ".project_author",
    "ProjectAuthorType": ".project_author_type",
    "ProjectAuthorTypeOne": ".project_author_type_one",
    "ProjectAuthorTypeZero": ".project_author_type_zero",
    "ProjectLinks": ".project_links",
    "ProjectPrivacy": ".project_privacy",
    "ResultSet": ".result_set",
    "ResultSetLastInsertRowid": ".result_set_last_insert_rowid",
    "TEnvironmentVariable": ".t_environment_variable",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "User": ".user",
    "UserLinks": ".user_links",
    "UserType": ".user_type",
    "Val": ".val",
    "ValAuthor": ".val_author",
    "ValAuthorType": ".val_author_type",
    "ValAuthorTypeOne": ".val_author_type_one",
    "ValAuthorTypeZero": ".val_author_type_zero",
    "ValLinks": ".val_links",
    "ValPrivacy": ".val_privacy",
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
    "BasicLegacyVal",
    "BasicLegacyValAuthor",
    "BasicLegacyValLinks",
    "BasicLegacyValPrivacy",
    "BasicLegacyValType",
    "Branch",
    "BranchLinks",
    "ConflictErrorBody",
    "ExtendedLegacyVal",
    "ExtendedLegacyValAuthor",
    "ExtendedLegacyValLinks",
    "ExtendedLegacyValPrivacy",
    "ExtendedLegacyValType",
    "FileRevisionMetadataV1",
    "FileRevisionMetadataV1Links",
    "FileRevisionMetadataV1Type",
    "FileRevisionMetadataV2",
    "FileRevisionMetadataV2Links",
    "FileRevisionMetadataV2Type",
    "ForbiddenErrorBody",
    "InternalServerErrorBody",
    "Membership",
    "MembershipRole",
    "MembershipUser",
    "NotFoundErrorBody",
    "Org",
    "PaginationLinks",
    "Project",
    "ProjectAuthor",
    "ProjectAuthorType",
    "ProjectAuthorTypeOne",
    "ProjectAuthorTypeZero",
    "ProjectLinks",
    "ProjectPrivacy",
    "ResultSet",
    "ResultSetLastInsertRowid",
    "TEnvironmentVariable",
    "UnauthorizedErrorBody",
    "User",
    "UserLinks",
    "UserType",
    "Val",
    "ValAuthor",
    "ValAuthorType",
    "ValAuthorTypeOne",
    "ValAuthorTypeZero",
    "ValLinks",
    "ValPrivacy",
]
