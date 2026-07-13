



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .user_get_available_themes_response import UserGetAvailableThemesResponse
    from .user_get_bungie_net_user_by_id_response import UserGetBungieNetUserByIdResponse
    from .user_get_credential_types_for_target_account_response import UserGetCredentialTypesForTargetAccountResponse
    from .user_get_membership_data_by_id_response import UserGetMembershipDataByIdResponse
    from .user_get_membership_data_for_current_user_response import UserGetMembershipDataForCurrentUserResponse
    from .user_get_membership_from_hard_linked_credential_response import (
        UserGetMembershipFromHardLinkedCredentialResponse,
    )
    from .user_get_sanitized_platform_display_names_response import UserGetSanitizedPlatformDisplayNamesResponse
    from .user_search_by_global_name_post_response import UserSearchByGlobalNamePostResponse
    from .user_search_by_global_name_prefix_response import UserSearchByGlobalNamePrefixResponse
_dynamic_imports: typing.Dict[str, str] = {
    "UserGetAvailableThemesResponse": ".user_get_available_themes_response",
    "UserGetBungieNetUserByIdResponse": ".user_get_bungie_net_user_by_id_response",
    "UserGetCredentialTypesForTargetAccountResponse": ".user_get_credential_types_for_target_account_response",
    "UserGetMembershipDataByIdResponse": ".user_get_membership_data_by_id_response",
    "UserGetMembershipDataForCurrentUserResponse": ".user_get_membership_data_for_current_user_response",
    "UserGetMembershipFromHardLinkedCredentialResponse": ".user_get_membership_from_hard_linked_credential_response",
    "UserGetSanitizedPlatformDisplayNamesResponse": ".user_get_sanitized_platform_display_names_response",
    "UserSearchByGlobalNamePostResponse": ".user_search_by_global_name_post_response",
    "UserSearchByGlobalNamePrefixResponse": ".user_search_by_global_name_prefix_response",
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
    "UserGetAvailableThemesResponse",
    "UserGetBungieNetUserByIdResponse",
    "UserGetCredentialTypesForTargetAccountResponse",
    "UserGetMembershipDataByIdResponse",
    "UserGetMembershipDataForCurrentUserResponse",
    "UserGetMembershipFromHardLinkedCredentialResponse",
    "UserGetSanitizedPlatformDisplayNamesResponse",
    "UserSearchByGlobalNamePostResponse",
    "UserSearchByGlobalNamePrefixResponse",
]
