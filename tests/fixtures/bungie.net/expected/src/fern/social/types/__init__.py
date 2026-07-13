



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .social_accept_friend_request_response import SocialAcceptFriendRequestResponse
    from .social_decline_friend_request_response import SocialDeclineFriendRequestResponse
    from .social_get_friend_list_response import SocialGetFriendListResponse
    from .social_get_friend_request_list_response import SocialGetFriendRequestListResponse
    from .social_get_platform_friend_list_response import SocialGetPlatformFriendListResponse
    from .social_issue_friend_request_response import SocialIssueFriendRequestResponse
    from .social_remove_friend_request_response import SocialRemoveFriendRequestResponse
    from .social_remove_friend_response import SocialRemoveFriendResponse
_dynamic_imports: typing.Dict[str, str] = {
    "SocialAcceptFriendRequestResponse": ".social_accept_friend_request_response",
    "SocialDeclineFriendRequestResponse": ".social_decline_friend_request_response",
    "SocialGetFriendListResponse": ".social_get_friend_list_response",
    "SocialGetFriendRequestListResponse": ".social_get_friend_request_list_response",
    "SocialGetPlatformFriendListResponse": ".social_get_platform_friend_list_response",
    "SocialIssueFriendRequestResponse": ".social_issue_friend_request_response",
    "SocialRemoveFriendRequestResponse": ".social_remove_friend_request_response",
    "SocialRemoveFriendResponse": ".social_remove_friend_response",
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
    "SocialAcceptFriendRequestResponse",
    "SocialDeclineFriendRequestResponse",
    "SocialGetFriendListResponse",
    "SocialGetFriendRequestListResponse",
    "SocialGetPlatformFriendListResponse",
    "SocialIssueFriendRequestResponse",
    "SocialRemoveFriendRequestResponse",
    "SocialRemoveFriendResponse",
]
