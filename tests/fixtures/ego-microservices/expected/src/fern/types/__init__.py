



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .avatar_is_not_exist import AvatarIsNotExist
    from .deleted_avatar_response import DeletedAvatarResponse
    from .deleted_post_response import DeletedPostResponse
    from .deleted_user_response import DeletedUserResponse
    from .empty import Empty
    from .error_result_invalid_avatar_type import ErrorResultInvalidAvatarType
    from .error_result_subscribe_is_already_exists import ErrorResultSubscribeIsAlreadyExists
    from .error_result_subscribe_is_not_exists import ErrorResultSubscribeIsNotExists
    from .error_result_subscribe_on_yourself import ErrorResultSubscribeOnYourself
    from .error_result_union_invalid_gender_invalid_birthday_date import (
        ErrorResultUnionInvalidGenderInvalidBirthdayDate,
    )
    from .error_result_union_invalid_gender_invalid_birthday_date_data import (
        ErrorResultUnionInvalidGenderInvalidBirthdayDateData,
    )
    from .error_result_user_data_is_not_correct import ErrorResultUserDataIsNotCorrect
    from .error_result_user_id_is_already_exist import ErrorResultUserIdIsAlreadyExist
    from .error_result_user_is_deleted import ErrorResultUserIsDeleted
    from .error_result_user_is_not_exist import ErrorResultUserIsNotExist
    from .error_result_user_is_not_exists import ErrorResultUserIsNotExists
    from .error_result_user_is_not_post_creator import ErrorResultUserIsNotPostCreator
    from .error_result_username_is_already_exist import ErrorResultUsernameIsAlreadyExist
    from .full_text_posts_search_posts_full_text_search_get_request_limit import (
        FullTextPostsSearchPostsFullTextSearchGetRequestLimit,
    )
    from .full_text_posts_search_posts_full_text_search_get_request_offset import (
        FullTextPostsSearchPostsFullTextSearchGetRequestOffset,
    )
    from .gender_value import GenderValue
    from .get_posts_order import GetPostsOrder
    from .get_subscribers_subscription_get_subscribers_get_request_limit import (
        GetSubscribersSubscriptionGetSubscribersGetRequestLimit,
    )
    from .get_subscribers_subscription_get_subscribers_get_request_offset import (
        GetSubscribersSubscriptionGetSubscribersGetRequestOffset,
    )
    from .get_subscriptions_order import GetSubscriptionsOrder
    from .get_subscriptions_subscription_get_subscriptions_get_request_limit import (
        GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit,
    )
    from .get_subscriptions_subscription_get_subscriptions_get_request_offset import (
        GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset,
    )
    from .get_user_posts_posts_user_posts_get_request_limit import GetUserPostsPostsUserPostsGetRequestLimit
    from .get_user_posts_posts_user_posts_get_request_offset import GetUserPostsPostsUserPostsGetRequestOffset
    from .http_validation_error import HttpValidationError
    from .invalid_avatar_type import InvalidAvatarType
    from .invalid_birthday_date import InvalidBirthdayDate
    from .invalid_gender import InvalidGender
    from .post_dto import PostDto
    from .post_response import PostResponse
    from .posts_response import PostsResponse
    from .posts_response_limit import PostsResponseLimit
    from .posts_response_offset import PostsResponseOffset
    from .refresh_token_response import RefreshTokenResponse
    from .set_avatar_response import SetAvatarResponse
    from .subscribe_is_already_exists import SubscribeIsAlreadyExists
    from .subscribe_is_not_exists import SubscribeIsNotExists
    from .subscribe_on_yourself import SubscribeOnYourself
    from .subscribe_response import SubscribeResponse
    from .subscribers_response import SubscribersResponse
    from .subscribers_response_limit import SubscribersResponseLimit
    from .subscribers_response_offset import SubscribersResponseOffset
    from .subscription_dto import SubscriptionDto
    from .subscriptions_response import SubscriptionsResponse
    from .subscriptions_response_limit import SubscriptionsResponseLimit
    from .subscriptions_response_offset import SubscriptionsResponseOffset
    from .tokens_response import TokensResponse
    from .unsubscribe_response import UnsubscribeResponse
    from .update_login_user_response import UpdateLoginUserResponse
    from .user_data_is_not_correct import UserDataIsNotCorrect
    from .user_data_response import UserDataResponse
    from .user_id_is_already_exist import UserIdIsAlreadyExist
    from .user_is_deleted import UserIsDeleted
    from .user_is_not_exist import UserIsNotExist
    from .user_is_not_exists import UserIsNotExists
    from .user_is_not_post_creator import UserIsNotPostCreator
    from .username_is_already_exist import UsernameIsAlreadyExist
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .verify_status import VerifyStatus
_dynamic_imports: typing.Dict[str, str] = {
    "AvatarIsNotExist": ".avatar_is_not_exist",
    "DeletedAvatarResponse": ".deleted_avatar_response",
    "DeletedPostResponse": ".deleted_post_response",
    "DeletedUserResponse": ".deleted_user_response",
    "Empty": ".empty",
    "ErrorResultInvalidAvatarType": ".error_result_invalid_avatar_type",
    "ErrorResultSubscribeIsAlreadyExists": ".error_result_subscribe_is_already_exists",
    "ErrorResultSubscribeIsNotExists": ".error_result_subscribe_is_not_exists",
    "ErrorResultSubscribeOnYourself": ".error_result_subscribe_on_yourself",
    "ErrorResultUnionInvalidGenderInvalidBirthdayDate": ".error_result_union_invalid_gender_invalid_birthday_date",
    "ErrorResultUnionInvalidGenderInvalidBirthdayDateData": ".error_result_union_invalid_gender_invalid_birthday_date_data",
    "ErrorResultUserDataIsNotCorrect": ".error_result_user_data_is_not_correct",
    "ErrorResultUserIdIsAlreadyExist": ".error_result_user_id_is_already_exist",
    "ErrorResultUserIsDeleted": ".error_result_user_is_deleted",
    "ErrorResultUserIsNotExist": ".error_result_user_is_not_exist",
    "ErrorResultUserIsNotExists": ".error_result_user_is_not_exists",
    "ErrorResultUserIsNotPostCreator": ".error_result_user_is_not_post_creator",
    "ErrorResultUsernameIsAlreadyExist": ".error_result_username_is_already_exist",
    "FullTextPostsSearchPostsFullTextSearchGetRequestLimit": ".full_text_posts_search_posts_full_text_search_get_request_limit",
    "FullTextPostsSearchPostsFullTextSearchGetRequestOffset": ".full_text_posts_search_posts_full_text_search_get_request_offset",
    "GenderValue": ".gender_value",
    "GetPostsOrder": ".get_posts_order",
    "GetSubscribersSubscriptionGetSubscribersGetRequestLimit": ".get_subscribers_subscription_get_subscribers_get_request_limit",
    "GetSubscribersSubscriptionGetSubscribersGetRequestOffset": ".get_subscribers_subscription_get_subscribers_get_request_offset",
    "GetSubscriptionsOrder": ".get_subscriptions_order",
    "GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit": ".get_subscriptions_subscription_get_subscriptions_get_request_limit",
    "GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset": ".get_subscriptions_subscription_get_subscriptions_get_request_offset",
    "GetUserPostsPostsUserPostsGetRequestLimit": ".get_user_posts_posts_user_posts_get_request_limit",
    "GetUserPostsPostsUserPostsGetRequestOffset": ".get_user_posts_posts_user_posts_get_request_offset",
    "HttpValidationError": ".http_validation_error",
    "InvalidAvatarType": ".invalid_avatar_type",
    "InvalidBirthdayDate": ".invalid_birthday_date",
    "InvalidGender": ".invalid_gender",
    "PostDto": ".post_dto",
    "PostResponse": ".post_response",
    "PostsResponse": ".posts_response",
    "PostsResponseLimit": ".posts_response_limit",
    "PostsResponseOffset": ".posts_response_offset",
    "RefreshTokenResponse": ".refresh_token_response",
    "SetAvatarResponse": ".set_avatar_response",
    "SubscribeIsAlreadyExists": ".subscribe_is_already_exists",
    "SubscribeIsNotExists": ".subscribe_is_not_exists",
    "SubscribeOnYourself": ".subscribe_on_yourself",
    "SubscribeResponse": ".subscribe_response",
    "SubscribersResponse": ".subscribers_response",
    "SubscribersResponseLimit": ".subscribers_response_limit",
    "SubscribersResponseOffset": ".subscribers_response_offset",
    "SubscriptionDto": ".subscription_dto",
    "SubscriptionsResponse": ".subscriptions_response",
    "SubscriptionsResponseLimit": ".subscriptions_response_limit",
    "SubscriptionsResponseOffset": ".subscriptions_response_offset",
    "TokensResponse": ".tokens_response",
    "UnsubscribeResponse": ".unsubscribe_response",
    "UpdateLoginUserResponse": ".update_login_user_response",
    "UserDataIsNotCorrect": ".user_data_is_not_correct",
    "UserDataResponse": ".user_data_response",
    "UserIdIsAlreadyExist": ".user_id_is_already_exist",
    "UserIsDeleted": ".user_is_deleted",
    "UserIsNotExist": ".user_is_not_exist",
    "UserIsNotExists": ".user_is_not_exists",
    "UserIsNotPostCreator": ".user_is_not_post_creator",
    "UsernameIsAlreadyExist": ".username_is_already_exist",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "VerifyStatus": ".verify_status",
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
    "AvatarIsNotExist",
    "DeletedAvatarResponse",
    "DeletedPostResponse",
    "DeletedUserResponse",
    "Empty",
    "ErrorResultInvalidAvatarType",
    "ErrorResultSubscribeIsAlreadyExists",
    "ErrorResultSubscribeIsNotExists",
    "ErrorResultSubscribeOnYourself",
    "ErrorResultUnionInvalidGenderInvalidBirthdayDate",
    "ErrorResultUnionInvalidGenderInvalidBirthdayDateData",
    "ErrorResultUserDataIsNotCorrect",
    "ErrorResultUserIdIsAlreadyExist",
    "ErrorResultUserIsDeleted",
    "ErrorResultUserIsNotExist",
    "ErrorResultUserIsNotExists",
    "ErrorResultUserIsNotPostCreator",
    "ErrorResultUsernameIsAlreadyExist",
    "FullTextPostsSearchPostsFullTextSearchGetRequestLimit",
    "FullTextPostsSearchPostsFullTextSearchGetRequestOffset",
    "GenderValue",
    "GetPostsOrder",
    "GetSubscribersSubscriptionGetSubscribersGetRequestLimit",
    "GetSubscribersSubscriptionGetSubscribersGetRequestOffset",
    "GetSubscriptionsOrder",
    "GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit",
    "GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset",
    "GetUserPostsPostsUserPostsGetRequestLimit",
    "GetUserPostsPostsUserPostsGetRequestOffset",
    "HttpValidationError",
    "InvalidAvatarType",
    "InvalidBirthdayDate",
    "InvalidGender",
    "PostDto",
    "PostResponse",
    "PostsResponse",
    "PostsResponseLimit",
    "PostsResponseOffset",
    "RefreshTokenResponse",
    "SetAvatarResponse",
    "SubscribeIsAlreadyExists",
    "SubscribeIsNotExists",
    "SubscribeOnYourself",
    "SubscribeResponse",
    "SubscribersResponse",
    "SubscribersResponseLimit",
    "SubscribersResponseOffset",
    "SubscriptionDto",
    "SubscriptionsResponse",
    "SubscriptionsResponseLimit",
    "SubscriptionsResponseOffset",
    "TokensResponse",
    "UnsubscribeResponse",
    "UpdateLoginUserResponse",
    "UserDataIsNotCorrect",
    "UserDataResponse",
    "UserIdIsAlreadyExist",
    "UserIsDeleted",
    "UserIsNotExist",
    "UserIsNotExists",
    "UserIsNotPostCreator",
    "UsernameIsAlreadyExist",
    "ValidationError",
    "ValidationErrorLocItem",
    "VerifyStatus",
]
