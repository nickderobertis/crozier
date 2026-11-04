



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_operation import AddOperation
    from .attachment import Attachment
    from .attachment_list import AttachmentList
    from .attachment_permalink_match_list import AttachmentPermalinkMatchList
    from .attachment_permalink_match_result import AttachmentPermalinkMatchResult
    from .attachment_spec import AttachmentSpec
    from .attachment_status import AttachmentStatus
    from .auth_provider import AuthProvider
    from .auth_provider_spec import AuthProviderSpec
    from .auth_provider_spec_auth_type import AuthProviderSpecAuthType
    from .author import Author
    from .backup_file import BackupFile
    from .category import Category
    from .category_spec import CategorySpec
    from .category_status import CategoryStatus
    from .category_tree_node import CategoryTreeNode
    from .comment import Comment
    from .comment_content_request import CommentContentRequest
    from .comment_email_owner import CommentEmailOwner
    from .comment_owner import CommentOwner
    from .comment_spec import CommentSpec
    from .comment_stats import CommentStats
    from .comment_status import CommentStatus
    from .condition import Condition
    from .condition_status import ConditionStatus
    from .config_map import ConfigMap
    from .config_map_ref import ConfigMapRef
    from .content import Content
    from .content_update_param import ContentUpdateParam
    from .content_wrapper import ContentWrapper
    from .contributor import Contributor
    from .copy_operation import CopyOperation
    from .custom_templates import CustomTemplates
    from .dashboard_stats import DashboardStats
    from .detailed_user import DetailedUser
    from .excerpt import Excerpt
    from .extension import Extension
    from .install_from_uri_request import InstallFromUriRequest
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
    from .license import License
    from .listed_auth_provider import ListedAuthProvider
    from .listed_auth_provider_auth_type import ListedAuthProviderAuthType
    from .listed_comment import ListedComment
    from .listed_comment_list import ListedCommentList
    from .listed_post import ListedPost
    from .listed_post_list import ListedPostList
    from .listed_reply import ListedReply
    from .listed_reply_list import ListedReplyList
    from .listed_single_page import ListedSinglePage
    from .listed_single_page_list import ListedSinglePageList
    from .listed_snapshot_dto import ListedSnapshotDto
    from .listed_snapshot_spec import ListedSnapshotSpec
    from .listed_user import ListedUser
    from .menu import Menu
    from .menu_item import MenuItem
    from .menu_item_spec import MenuItemSpec
    from .menu_item_spec_route_ref import MenuItemSpecRouteRef
    from .menu_item_spec_target import MenuItemSpecTarget
    from .menu_item_status import MenuItemStatus
    from .menu_item_tree_node import MenuItemTreeNode
    from .menu_spec import MenuSpec
    from .metadata import Metadata
    from .move_operation import MoveOperation
    from .owner_info import OwnerInfo
    from .page_layout import PageLayout
    from .page_layout_state import PageLayoutState
    from .plugin import Plugin
    from .plugin_author import PluginAuthor
    from .plugin_install_request import PluginInstallRequest
    from .plugin_install_request_source import PluginInstallRequestSource
    from .plugin_list import PluginList
    from .plugin_spec import PluginSpec
    from .plugin_status import PluginStatus
    from .plugin_status_last_probe_state import PluginStatusLastProbeState
    from .plugin_status_phase import PluginStatusPhase
    from .policy_rule import PolicyRule
    from .post import Post
    from .post_request import PostRequest
    from .post_spec import PostSpec
    from .post_spec_visible import PostSpecVisible
    from .post_status import PostStatus
    from .ref import Ref
    from .remove_operation import RemoveOperation
    from .replace_operation import ReplaceOperation
    from .reply import Reply
    from .reply_spec import ReplySpec
    from .reply_status import ReplyStatus
    from .role import Role
    from .setting import Setting
    from .setting_form import SettingForm
    from .setting_ref import SettingRef
    from .setting_spec import SettingSpec
    from .single_page import SinglePage
    from .single_page_request import SinglePageRequest
    from .single_page_spec import SinglePageSpec
    from .single_page_spec_visible import SinglePageSpecVisible
    from .single_page_status import SinglePageStatus
    from .stats import Stats
    from .tag import Tag
    from .tag_list import TagList
    from .tag_spec import TagSpec
    from .tag_status import TagStatus
    from .template_descriptor import TemplateDescriptor
    from .test_operation import TestOperation
    from .theme import Theme
    from .theme_list import ThemeList
    from .theme_spec import ThemeSpec
    from .theme_status import ThemeStatus
    from .theme_status_phase import ThemeStatusPhase
    from .ui_plugin_provider import UiPluginProvider
    from .ui_plugin_provider_descriptor import UiPluginProviderDescriptor
    from .ui_plugin_provider_kind import UiPluginProviderKind
    from .ui_plugin_provider_type import UiPluginProviderType
    from .upgrade_from_uri_request import UpgradeFromUriRequest
    from .user import User
    from .user_endpoint_listed_user_list import UserEndpointListedUserList
    from .user_permission import UserPermission
    from .user_spec import UserSpec
    from .user_status import UserStatus
_dynamic_imports: typing.Dict[str, str] = {
    "AddOperation": ".add_operation",
    "Attachment": ".attachment",
    "AttachmentList": ".attachment_list",
    "AttachmentPermalinkMatchList": ".attachment_permalink_match_list",
    "AttachmentPermalinkMatchResult": ".attachment_permalink_match_result",
    "AttachmentSpec": ".attachment_spec",
    "AttachmentStatus": ".attachment_status",
    "AuthProvider": ".auth_provider",
    "AuthProviderSpec": ".auth_provider_spec",
    "AuthProviderSpecAuthType": ".auth_provider_spec_auth_type",
    "Author": ".author",
    "BackupFile": ".backup_file",
    "Category": ".category",
    "CategorySpec": ".category_spec",
    "CategoryStatus": ".category_status",
    "CategoryTreeNode": ".category_tree_node",
    "Comment": ".comment",
    "CommentContentRequest": ".comment_content_request",
    "CommentEmailOwner": ".comment_email_owner",
    "CommentOwner": ".comment_owner",
    "CommentSpec": ".comment_spec",
    "CommentStats": ".comment_stats",
    "CommentStatus": ".comment_status",
    "Condition": ".condition",
    "ConditionStatus": ".condition_status",
    "ConfigMap": ".config_map",
    "ConfigMapRef": ".config_map_ref",
    "Content": ".content",
    "ContentUpdateParam": ".content_update_param",
    "ContentWrapper": ".content_wrapper",
    "Contributor": ".contributor",
    "CopyOperation": ".copy_operation",
    "CustomTemplates": ".custom_templates",
    "DashboardStats": ".dashboard_stats",
    "DetailedUser": ".detailed_user",
    "Excerpt": ".excerpt",
    "Extension": ".extension",
    "InstallFromUriRequest": ".install_from_uri_request",
    "JsonPatch": ".json_patch",
    "JsonPatchItem": ".json_patch_item",
    "JsonPatchItem_Add": ".json_patch_item",
    "JsonPatchItem_Copy": ".json_patch_item",
    "JsonPatchItem_Move": ".json_patch_item",
    "JsonPatchItem_Remove": ".json_patch_item",
    "JsonPatchItem_Replace": ".json_patch_item",
    "JsonPatchItem_Test": ".json_patch_item",
    "License": ".license",
    "ListedAuthProvider": ".listed_auth_provider",
    "ListedAuthProviderAuthType": ".listed_auth_provider_auth_type",
    "ListedComment": ".listed_comment",
    "ListedCommentList": ".listed_comment_list",
    "ListedPost": ".listed_post",
    "ListedPostList": ".listed_post_list",
    "ListedReply": ".listed_reply",
    "ListedReplyList": ".listed_reply_list",
    "ListedSinglePage": ".listed_single_page",
    "ListedSinglePageList": ".listed_single_page_list",
    "ListedSnapshotDto": ".listed_snapshot_dto",
    "ListedSnapshotSpec": ".listed_snapshot_spec",
    "ListedUser": ".listed_user",
    "Menu": ".menu",
    "MenuItem": ".menu_item",
    "MenuItemSpec": ".menu_item_spec",
    "MenuItemSpecRouteRef": ".menu_item_spec_route_ref",
    "MenuItemSpecTarget": ".menu_item_spec_target",
    "MenuItemStatus": ".menu_item_status",
    "MenuItemTreeNode": ".menu_item_tree_node",
    "MenuSpec": ".menu_spec",
    "Metadata": ".metadata",
    "MoveOperation": ".move_operation",
    "OwnerInfo": ".owner_info",
    "PageLayout": ".page_layout",
    "PageLayoutState": ".page_layout_state",
    "Plugin": ".plugin",
    "PluginAuthor": ".plugin_author",
    "PluginInstallRequest": ".plugin_install_request",
    "PluginInstallRequestSource": ".plugin_install_request_source",
    "PluginList": ".plugin_list",
    "PluginSpec": ".plugin_spec",
    "PluginStatus": ".plugin_status",
    "PluginStatusLastProbeState": ".plugin_status_last_probe_state",
    "PluginStatusPhase": ".plugin_status_phase",
    "PolicyRule": ".policy_rule",
    "Post": ".post",
    "PostRequest": ".post_request",
    "PostSpec": ".post_spec",
    "PostSpecVisible": ".post_spec_visible",
    "PostStatus": ".post_status",
    "Ref": ".ref",
    "RemoveOperation": ".remove_operation",
    "ReplaceOperation": ".replace_operation",
    "Reply": ".reply",
    "ReplySpec": ".reply_spec",
    "ReplyStatus": ".reply_status",
    "Role": ".role",
    "Setting": ".setting",
    "SettingForm": ".setting_form",
    "SettingRef": ".setting_ref",
    "SettingSpec": ".setting_spec",
    "SinglePage": ".single_page",
    "SinglePageRequest": ".single_page_request",
    "SinglePageSpec": ".single_page_spec",
    "SinglePageSpecVisible": ".single_page_spec_visible",
    "SinglePageStatus": ".single_page_status",
    "Stats": ".stats",
    "Tag": ".tag",
    "TagList": ".tag_list",
    "TagSpec": ".tag_spec",
    "TagStatus": ".tag_status",
    "TemplateDescriptor": ".template_descriptor",
    "TestOperation": ".test_operation",
    "Theme": ".theme",
    "ThemeList": ".theme_list",
    "ThemeSpec": ".theme_spec",
    "ThemeStatus": ".theme_status",
    "ThemeStatusPhase": ".theme_status_phase",
    "UiPluginProvider": ".ui_plugin_provider",
    "UiPluginProviderDescriptor": ".ui_plugin_provider_descriptor",
    "UiPluginProviderKind": ".ui_plugin_provider_kind",
    "UiPluginProviderType": ".ui_plugin_provider_type",
    "UpgradeFromUriRequest": ".upgrade_from_uri_request",
    "User": ".user",
    "UserEndpointListedUserList": ".user_endpoint_listed_user_list",
    "UserPermission": ".user_permission",
    "UserSpec": ".user_spec",
    "UserStatus": ".user_status",
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
    "Attachment",
    "AttachmentList",
    "AttachmentPermalinkMatchList",
    "AttachmentPermalinkMatchResult",
    "AttachmentSpec",
    "AttachmentStatus",
    "AuthProvider",
    "AuthProviderSpec",
    "AuthProviderSpecAuthType",
    "Author",
    "BackupFile",
    "Category",
    "CategorySpec",
    "CategoryStatus",
    "CategoryTreeNode",
    "Comment",
    "CommentContentRequest",
    "CommentEmailOwner",
    "CommentOwner",
    "CommentSpec",
    "CommentStats",
    "CommentStatus",
    "Condition",
    "ConditionStatus",
    "ConfigMap",
    "ConfigMapRef",
    "Content",
    "ContentUpdateParam",
    "ContentWrapper",
    "Contributor",
    "CopyOperation",
    "CustomTemplates",
    "DashboardStats",
    "DetailedUser",
    "Excerpt",
    "Extension",
    "InstallFromUriRequest",
    "JsonPatch",
    "JsonPatchItem",
    "JsonPatchItem_Add",
    "JsonPatchItem_Copy",
    "JsonPatchItem_Move",
    "JsonPatchItem_Remove",
    "JsonPatchItem_Replace",
    "JsonPatchItem_Test",
    "License",
    "ListedAuthProvider",
    "ListedAuthProviderAuthType",
    "ListedComment",
    "ListedCommentList",
    "ListedPost",
    "ListedPostList",
    "ListedReply",
    "ListedReplyList",
    "ListedSinglePage",
    "ListedSinglePageList",
    "ListedSnapshotDto",
    "ListedSnapshotSpec",
    "ListedUser",
    "Menu",
    "MenuItem",
    "MenuItemSpec",
    "MenuItemSpecRouteRef",
    "MenuItemSpecTarget",
    "MenuItemStatus",
    "MenuItemTreeNode",
    "MenuSpec",
    "Metadata",
    "MoveOperation",
    "OwnerInfo",
    "PageLayout",
    "PageLayoutState",
    "Plugin",
    "PluginAuthor",
    "PluginInstallRequest",
    "PluginInstallRequestSource",
    "PluginList",
    "PluginSpec",
    "PluginStatus",
    "PluginStatusLastProbeState",
    "PluginStatusPhase",
    "PolicyRule",
    "Post",
    "PostRequest",
    "PostSpec",
    "PostSpecVisible",
    "PostStatus",
    "Ref",
    "RemoveOperation",
    "ReplaceOperation",
    "Reply",
    "ReplySpec",
    "ReplyStatus",
    "Role",
    "Setting",
    "SettingForm",
    "SettingRef",
    "SettingSpec",
    "SinglePage",
    "SinglePageRequest",
    "SinglePageSpec",
    "SinglePageSpecVisible",
    "SinglePageStatus",
    "Stats",
    "Tag",
    "TagList",
    "TagSpec",
    "TagStatus",
    "TemplateDescriptor",
    "TestOperation",
    "Theme",
    "ThemeList",
    "ThemeSpec",
    "ThemeStatus",
    "ThemeStatusPhase",
    "UiPluginProvider",
    "UiPluginProviderDescriptor",
    "UiPluginProviderKind",
    "UiPluginProviderType",
    "UpgradeFromUriRequest",
    "User",
    "UserEndpointListedUserList",
    "UserPermission",
    "UserSpec",
    "UserStatus",
]
