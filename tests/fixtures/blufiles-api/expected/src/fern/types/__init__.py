



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .config import Config
    from .config_disable_registration import ConfigDisableRegistration
    from .config_disable_registration_zero import ConfigDisableRegistrationZero
    from .config_total import ConfigTotal
    from .config_user import ConfigUser
    from .delete_me_tokens_request_id import DeleteMeTokensRequestId
    from .delete_me_tokens_request_id_zero import DeleteMeTokensRequestIdZero
    from .filtered_admin_user import FilteredAdminUser
    from .filtered_admin_user_collections import FilteredAdminUserCollections
    from .filtered_admin_user_files import FilteredAdminUserFiles
    from .filtered_admin_user_folders import FilteredAdminUserFolders
    from .filtered_admin_user_pastes import FilteredAdminUserPastes
    from .filtered_admin_user_shares import FilteredAdminUserShares
    from .filtered_admin_user_storage import FilteredAdminUserStorage
    from .filtered_admin_user_tokens import FilteredAdminUserTokens
    from .filtered_admin_user_type import FilteredAdminUserType
    from .filtered_collection import FilteredCollection
    from .filtered_file import FilteredFile
    from .filtered_file_upload import FilteredFileUpload
    from .filtered_file_upload_status import FilteredFileUploadStatus
    from .filtered_folder import FilteredFolder
    from .filtered_paste import FilteredPaste
    from .filtered_share import FilteredShare
    from .filtered_share_collection import FilteredShareCollection
    from .filtered_share_file import FilteredShareFile
    from .filtered_share_folder import FilteredShareFolder
    from .filtered_share_owner import FilteredShareOwner
    from .filtered_share_paste import FilteredSharePaste
    from .filtered_share_type import FilteredShareType
    from .filtered_token import FilteredToken
    from .filtered_token_type import FilteredTokenType
    from .get_admin_usage_response import GetAdminUsageResponse
    from .get_admin_usage_response_collections import GetAdminUsageResponseCollections
    from .get_admin_usage_response_files import GetAdminUsageResponseFiles
    from .get_admin_usage_response_folders import GetAdminUsageResponseFolders
    from .get_admin_usage_response_pastes import GetAdminUsageResponsePastes
    from .get_admin_usage_response_shares import GetAdminUsageResponseShares
    from .get_admin_usage_response_storage import GetAdminUsageResponseStorage
    from .get_me_response import GetMeResponse
    from .get_me_response_type import GetMeResponseType
    from .get_usage_stats_response import GetUsageStatsResponse
    from .get_usage_stats_response_collections import GetUsageStatsResponseCollections
    from .get_usage_stats_response_files import GetUsageStatsResponseFiles
    from .get_usage_stats_response_folders import GetUsageStatsResponseFolders
    from .get_usage_stats_response_pastes import GetUsageStatsResponsePastes
    from .get_usage_stats_response_shares import GetUsageStatsResponseShares
    from .get_usage_stats_response_storage import GetUsageStatsResponseStorage
    from .get_usage_stats_response_tokens import GetUsageStatsResponseTokens
    from .patch_admin_config_request_disable_registration import PatchAdminConfigRequestDisableRegistration
    from .patch_admin_config_request_disable_registration_one import PatchAdminConfigRequestDisableRegistrationOne
    from .patch_admin_config_request_total import PatchAdminConfigRequestTotal
    from .patch_admin_config_request_user import PatchAdminConfigRequestUser
    from .patch_admin_users_id_request_type import PatchAdminUsersIdRequestType
    from .patch_me_tokens_response import PatchMeTokensResponse
    from .patch_me_tokens_response_type import PatchMeTokensResponseType
    from .post_auth_login_response import PostAuthLoginResponse
    from .post_auth_login_response_user import PostAuthLoginResponseUser
    from .post_auth_register_response import PostAuthRegisterResponse
    from .post_auth_register_response_user import PostAuthRegisterResponseUser
    from .post_me_tokens_response import PostMeTokensResponse
    from .post_me_tokens_response_type import PostMeTokensResponseType
    from .post_search_response import PostSearchResponse
    from .post_share_request_type import PostShareRequestType
_dynamic_imports: typing.Dict[str, str] = {
    "Config": ".config",
    "ConfigDisableRegistration": ".config_disable_registration",
    "ConfigDisableRegistrationZero": ".config_disable_registration_zero",
    "ConfigTotal": ".config_total",
    "ConfigUser": ".config_user",
    "DeleteMeTokensRequestId": ".delete_me_tokens_request_id",
    "DeleteMeTokensRequestIdZero": ".delete_me_tokens_request_id_zero",
    "FilteredAdminUser": ".filtered_admin_user",
    "FilteredAdminUserCollections": ".filtered_admin_user_collections",
    "FilteredAdminUserFiles": ".filtered_admin_user_files",
    "FilteredAdminUserFolders": ".filtered_admin_user_folders",
    "FilteredAdminUserPastes": ".filtered_admin_user_pastes",
    "FilteredAdminUserShares": ".filtered_admin_user_shares",
    "FilteredAdminUserStorage": ".filtered_admin_user_storage",
    "FilteredAdminUserTokens": ".filtered_admin_user_tokens",
    "FilteredAdminUserType": ".filtered_admin_user_type",
    "FilteredCollection": ".filtered_collection",
    "FilteredFile": ".filtered_file",
    "FilteredFileUpload": ".filtered_file_upload",
    "FilteredFileUploadStatus": ".filtered_file_upload_status",
    "FilteredFolder": ".filtered_folder",
    "FilteredPaste": ".filtered_paste",
    "FilteredShare": ".filtered_share",
    "FilteredShareCollection": ".filtered_share_collection",
    "FilteredShareFile": ".filtered_share_file",
    "FilteredShareFolder": ".filtered_share_folder",
    "FilteredShareOwner": ".filtered_share_owner",
    "FilteredSharePaste": ".filtered_share_paste",
    "FilteredShareType": ".filtered_share_type",
    "FilteredToken": ".filtered_token",
    "FilteredTokenType": ".filtered_token_type",
    "GetAdminUsageResponse": ".get_admin_usage_response",
    "GetAdminUsageResponseCollections": ".get_admin_usage_response_collections",
    "GetAdminUsageResponseFiles": ".get_admin_usage_response_files",
    "GetAdminUsageResponseFolders": ".get_admin_usage_response_folders",
    "GetAdminUsageResponsePastes": ".get_admin_usage_response_pastes",
    "GetAdminUsageResponseShares": ".get_admin_usage_response_shares",
    "GetAdminUsageResponseStorage": ".get_admin_usage_response_storage",
    "GetMeResponse": ".get_me_response",
    "GetMeResponseType": ".get_me_response_type",
    "GetUsageStatsResponse": ".get_usage_stats_response",
    "GetUsageStatsResponseCollections": ".get_usage_stats_response_collections",
    "GetUsageStatsResponseFiles": ".get_usage_stats_response_files",
    "GetUsageStatsResponseFolders": ".get_usage_stats_response_folders",
    "GetUsageStatsResponsePastes": ".get_usage_stats_response_pastes",
    "GetUsageStatsResponseShares": ".get_usage_stats_response_shares",
    "GetUsageStatsResponseStorage": ".get_usage_stats_response_storage",
    "GetUsageStatsResponseTokens": ".get_usage_stats_response_tokens",
    "PatchAdminConfigRequestDisableRegistration": ".patch_admin_config_request_disable_registration",
    "PatchAdminConfigRequestDisableRegistrationOne": ".patch_admin_config_request_disable_registration_one",
    "PatchAdminConfigRequestTotal": ".patch_admin_config_request_total",
    "PatchAdminConfigRequestUser": ".patch_admin_config_request_user",
    "PatchAdminUsersIdRequestType": ".patch_admin_users_id_request_type",
    "PatchMeTokensResponse": ".patch_me_tokens_response",
    "PatchMeTokensResponseType": ".patch_me_tokens_response_type",
    "PostAuthLoginResponse": ".post_auth_login_response",
    "PostAuthLoginResponseUser": ".post_auth_login_response_user",
    "PostAuthRegisterResponse": ".post_auth_register_response",
    "PostAuthRegisterResponseUser": ".post_auth_register_response_user",
    "PostMeTokensResponse": ".post_me_tokens_response",
    "PostMeTokensResponseType": ".post_me_tokens_response_type",
    "PostSearchResponse": ".post_search_response",
    "PostShareRequestType": ".post_share_request_type",
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
    "Config",
    "ConfigDisableRegistration",
    "ConfigDisableRegistrationZero",
    "ConfigTotal",
    "ConfigUser",
    "DeleteMeTokensRequestId",
    "DeleteMeTokensRequestIdZero",
    "FilteredAdminUser",
    "FilteredAdminUserCollections",
    "FilteredAdminUserFiles",
    "FilteredAdminUserFolders",
    "FilteredAdminUserPastes",
    "FilteredAdminUserShares",
    "FilteredAdminUserStorage",
    "FilteredAdminUserTokens",
    "FilteredAdminUserType",
    "FilteredCollection",
    "FilteredFile",
    "FilteredFileUpload",
    "FilteredFileUploadStatus",
    "FilteredFolder",
    "FilteredPaste",
    "FilteredShare",
    "FilteredShareCollection",
    "FilteredShareFile",
    "FilteredShareFolder",
    "FilteredShareOwner",
    "FilteredSharePaste",
    "FilteredShareType",
    "FilteredToken",
    "FilteredTokenType",
    "GetAdminUsageResponse",
    "GetAdminUsageResponseCollections",
    "GetAdminUsageResponseFiles",
    "GetAdminUsageResponseFolders",
    "GetAdminUsageResponsePastes",
    "GetAdminUsageResponseShares",
    "GetAdminUsageResponseStorage",
    "GetMeResponse",
    "GetMeResponseType",
    "GetUsageStatsResponse",
    "GetUsageStatsResponseCollections",
    "GetUsageStatsResponseFiles",
    "GetUsageStatsResponseFolders",
    "GetUsageStatsResponsePastes",
    "GetUsageStatsResponseShares",
    "GetUsageStatsResponseStorage",
    "GetUsageStatsResponseTokens",
    "PatchAdminConfigRequestDisableRegistration",
    "PatchAdminConfigRequestDisableRegistrationOne",
    "PatchAdminConfigRequestTotal",
    "PatchAdminConfigRequestUser",
    "PatchAdminUsersIdRequestType",
    "PatchMeTokensResponse",
    "PatchMeTokensResponseType",
    "PostAuthLoginResponse",
    "PostAuthLoginResponseUser",
    "PostAuthRegisterResponse",
    "PostAuthRegisterResponseUser",
    "PostMeTokensResponse",
    "PostMeTokensResponseType",
    "PostSearchResponse",
    "PostShareRequestType",
]
