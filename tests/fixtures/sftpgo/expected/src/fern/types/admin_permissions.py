

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdminPermissions(enum.StrEnum):
    """
    Admin permissions:
      * `*` - super admin permissions are granted
      * `add_users` - add new users is allowed
      * `edit_users` - change existing users is allowed
      * `del_users` - remove users is allowed
      * `view_users` - list users is allowed
      * `view_conns` - list active connections is allowed
      * `close_conns` - close active connections is allowed
      * `view_status` - view the server status is allowed
      * `manage_folders` - manage folders is allowed
      * `manage_groups` - manage groups is allowed
      * `quota_scans` - view and start quota scans is allowed
      * `manage_defender` - remove ip from the dynamic blocklist is allowed
      * `view_defender` - list the dynamic blocklist is allowed
      * `view_events` - view and search filesystem and provider events is allowed
      * `disable_mfa` - allow to disable two-factor authentication for users
    """

    ALL = "*"
    ADD_USERS = "add_users"
    EDIT_USERS = "edit_users"
    DEL_USERS = "del_users"
    VIEW_USERS = "view_users"
    VIEW_CONNS = "view_conns"
    CLOSE_CONNS = "close_conns"
    VIEW_STATUS = "view_status"
    MANAGE_FOLDERS = "manage_folders"
    MANAGE_GROUPS = "manage_groups"
    QUOTA_SCANS = "quota_scans"
    MANAGE_DEFENDER = "manage_defender"
    VIEW_DEFENDER = "view_defender"
    VIEW_EVENTS = "view_events"
    DISABLE_MFA = "disable_mfa"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        add_users: typing.Callable[[], T_Result],
        edit_users: typing.Callable[[], T_Result],
        del_users: typing.Callable[[], T_Result],
        view_users: typing.Callable[[], T_Result],
        view_conns: typing.Callable[[], T_Result],
        close_conns: typing.Callable[[], T_Result],
        view_status: typing.Callable[[], T_Result],
        manage_folders: typing.Callable[[], T_Result],
        manage_groups: typing.Callable[[], T_Result],
        quota_scans: typing.Callable[[], T_Result],
        manage_defender: typing.Callable[[], T_Result],
        view_defender: typing.Callable[[], T_Result],
        view_events: typing.Callable[[], T_Result],
        disable_mfa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdminPermissions.ALL:
            return all_()
        if self is AdminPermissions.ADD_USERS:
            return add_users()
        if self is AdminPermissions.EDIT_USERS:
            return edit_users()
        if self is AdminPermissions.DEL_USERS:
            return del_users()
        if self is AdminPermissions.VIEW_USERS:
            return view_users()
        if self is AdminPermissions.VIEW_CONNS:
            return view_conns()
        if self is AdminPermissions.CLOSE_CONNS:
            return close_conns()
        if self is AdminPermissions.VIEW_STATUS:
            return view_status()
        if self is AdminPermissions.MANAGE_FOLDERS:
            return manage_folders()
        if self is AdminPermissions.MANAGE_GROUPS:
            return manage_groups()
        if self is AdminPermissions.QUOTA_SCANS:
            return quota_scans()
        if self is AdminPermissions.MANAGE_DEFENDER:
            return manage_defender()
        if self is AdminPermissions.VIEW_DEFENDER:
            return view_defender()
        if self is AdminPermissions.VIEW_EVENTS:
            return view_events()
        if self is AdminPermissions.DISABLE_MFA:
            return disable_mfa()
