



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_operation import AddOperation
    from .annotation_setting import AnnotationSetting
    from .annotation_setting_spec import AnnotationSettingSpec
    from .attachment import Attachment
    from .attachment_list import AttachmentList
    from .attachment_permalink_match_list import AttachmentPermalinkMatchList
    from .attachment_permalink_match_result import AttachmentPermalinkMatchResult
    from .attachment_spec import AttachmentSpec
    from .attachment_status import AttachmentStatus
    from .category import Category
    from .category_spec import CategorySpec
    from .category_status import CategoryStatus
    from .condition import Condition
    from .condition_status import ConditionStatus
    from .contributor import Contributor
    from .copy_operation import CopyOperation
    from .device import Device
    from .device_spec import DeviceSpec
    from .device_status import DeviceStatus
    from .excerpt import Excerpt
    from .group_kind import GroupKind
    from .json_patch import JsonPatch
    from .json_patch_item import (
        JsonPatchItem,
        JsonPatchItem_Add,
        JsonPatchItem_Copy,
        JsonPatchItem_Move,
        JsonPatchItem_Remove,
        JsonPatchItem_Replace,
        JsonPatchItem_Test,
    )
    from .listed_post import ListedPost
    from .listed_post_list import ListedPostList
    from .metadata import Metadata
    from .move_operation import MoveOperation
    from .notification import Notification
    from .notification_list import NotificationList
    from .notification_spec import NotificationSpec
    from .notifier_info import NotifierInfo
    from .password_request import PasswordRequest
    from .pat_spec import PatSpec
    from .personal_access_token import PersonalAccessToken
    from .post import Post
    from .post_spec import PostSpec
    from .post_spec_visible import PostSpecVisible
    from .post_status import PostStatus
    from .reason_type_info import ReasonTypeInfo
    from .reason_type_notifier_matrix import ReasonTypeNotifierMatrix
    from .reason_type_notifier_request import ReasonTypeNotifierRequest
    from .ref import Ref
    from .remove_operation import RemoveOperation
    from .replace_operation import ReplaceOperation
    from .snap_shot_spec import SnapShotSpec
    from .snapshot import Snapshot
    from .stats import Stats
    from .tag import Tag
    from .tag_spec import TagSpec
    from .tag_status import TagStatus
    from .test_operation import TestOperation
    from .totp_auth_link_response import TotpAuthLinkResponse
    from .two_factor_auth_settings import TwoFactorAuthSettings
    from .uc_user_vo import UcUserVo
    from .user_connection import UserConnection
    from .user_connection_spec import UserConnectionSpec
    from .user_device import UserDevice
_dynamic_imports: typing.Dict[str, str] = {
    "AddOperation": ".add_operation",
    "AnnotationSetting": ".annotation_setting",
    "AnnotationSettingSpec": ".annotation_setting_spec",
    "Attachment": ".attachment",
    "AttachmentList": ".attachment_list",
    "AttachmentPermalinkMatchList": ".attachment_permalink_match_list",
    "AttachmentPermalinkMatchResult": ".attachment_permalink_match_result",
    "AttachmentSpec": ".attachment_spec",
    "AttachmentStatus": ".attachment_status",
    "Category": ".category",
    "CategorySpec": ".category_spec",
    "CategoryStatus": ".category_status",
    "Condition": ".condition",
    "ConditionStatus": ".condition_status",
    "Contributor": ".contributor",
    "CopyOperation": ".copy_operation",
    "Device": ".device",
    "DeviceSpec": ".device_spec",
    "DeviceStatus": ".device_status",
    "Excerpt": ".excerpt",
    "GroupKind": ".group_kind",
    "JsonPatch": ".json_patch",
    "JsonPatchItem": ".json_patch_item",
    "JsonPatchItem_Add": ".json_patch_item",
    "JsonPatchItem_Copy": ".json_patch_item",
    "JsonPatchItem_Move": ".json_patch_item",
    "JsonPatchItem_Remove": ".json_patch_item",
    "JsonPatchItem_Replace": ".json_patch_item",
    "JsonPatchItem_Test": ".json_patch_item",
    "ListedPost": ".listed_post",
    "ListedPostList": ".listed_post_list",
    "Metadata": ".metadata",
    "MoveOperation": ".move_operation",
    "Notification": ".notification",
    "NotificationList": ".notification_list",
    "NotificationSpec": ".notification_spec",
    "NotifierInfo": ".notifier_info",
    "PasswordRequest": ".password_request",
    "PatSpec": ".pat_spec",
    "PersonalAccessToken": ".personal_access_token",
    "Post": ".post",
    "PostSpec": ".post_spec",
    "PostSpecVisible": ".post_spec_visible",
    "PostStatus": ".post_status",
    "ReasonTypeInfo": ".reason_type_info",
    "ReasonTypeNotifierMatrix": ".reason_type_notifier_matrix",
    "ReasonTypeNotifierRequest": ".reason_type_notifier_request",
    "Ref": ".ref",
    "RemoveOperation": ".remove_operation",
    "ReplaceOperation": ".replace_operation",
    "SnapShotSpec": ".snap_shot_spec",
    "Snapshot": ".snapshot",
    "Stats": ".stats",
    "Tag": ".tag",
    "TagSpec": ".tag_spec",
    "TagStatus": ".tag_status",
    "TestOperation": ".test_operation",
    "TotpAuthLinkResponse": ".totp_auth_link_response",
    "TwoFactorAuthSettings": ".two_factor_auth_settings",
    "UcUserVo": ".uc_user_vo",
    "UserConnection": ".user_connection",
    "UserConnectionSpec": ".user_connection_spec",
    "UserDevice": ".user_device",
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
    "AddOperation",
    "AnnotationSetting",
    "AnnotationSettingSpec",
    "Attachment",
    "AttachmentList",
    "AttachmentPermalinkMatchList",
    "AttachmentPermalinkMatchResult",
    "AttachmentSpec",
    "AttachmentStatus",
    "Category",
    "CategorySpec",
    "CategoryStatus",
    "Condition",
    "ConditionStatus",
    "Contributor",
    "CopyOperation",
    "Device",
    "DeviceSpec",
    "DeviceStatus",
    "Excerpt",
    "GroupKind",
    "JsonPatch",
    "JsonPatchItem",
    "JsonPatchItem_Add",
    "JsonPatchItem_Copy",
    "JsonPatchItem_Move",
    "JsonPatchItem_Remove",
    "JsonPatchItem_Replace",
    "JsonPatchItem_Test",
    "ListedPost",
    "ListedPostList",
    "Metadata",
    "MoveOperation",
    "Notification",
    "NotificationList",
    "NotificationSpec",
    "NotifierInfo",
    "PasswordRequest",
    "PatSpec",
    "PersonalAccessToken",
    "Post",
    "PostSpec",
    "PostSpecVisible",
    "PostStatus",
    "ReasonTypeInfo",
    "ReasonTypeNotifierMatrix",
    "ReasonTypeNotifierRequest",
    "Ref",
    "RemoveOperation",
    "ReplaceOperation",
    "SnapShotSpec",
    "Snapshot",
    "Stats",
    "Tag",
    "TagSpec",
    "TagStatus",
    "TestOperation",
    "TotpAuthLinkResponse",
    "TwoFactorAuthSettings",
    "UcUserVo",
    "UserConnection",
    "UserConnectionSpec",
    "UserDevice",
]
