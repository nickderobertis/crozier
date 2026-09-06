

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DumpDataScopes(enum.StrEnum):
    USERS = "users"
    FOLDERS = "folders"
    GROUPS = "groups"
    ADMINS = "admins"
    API_KEYS = "api_keys"
    SHARES = "shares"
    ACTIONS = "actions"
    RULES = "rules"
    ROLES = "roles"
    IP_LISTS = "ip_lists"
    CONFIGS = "configs"

    def visit(
        self,
        users: typing.Callable[[], T_Result],
        folders: typing.Callable[[], T_Result],
        groups: typing.Callable[[], T_Result],
        admins: typing.Callable[[], T_Result],
        api_keys: typing.Callable[[], T_Result],
        shares: typing.Callable[[], T_Result],
        actions: typing.Callable[[], T_Result],
        rules: typing.Callable[[], T_Result],
        roles: typing.Callable[[], T_Result],
        ip_lists: typing.Callable[[], T_Result],
        configs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DumpDataScopes.USERS:
            return users()
        if self is DumpDataScopes.FOLDERS:
            return folders()
        if self is DumpDataScopes.GROUPS:
            return groups()
        if self is DumpDataScopes.ADMINS:
            return admins()
        if self is DumpDataScopes.API_KEYS:
            return api_keys()
        if self is DumpDataScopes.SHARES:
            return shares()
        if self is DumpDataScopes.ACTIONS:
            return actions()
        if self is DumpDataScopes.RULES:
            return rules()
        if self is DumpDataScopes.ROLES:
            return roles()
        if self is DumpDataScopes.IP_LISTS:
            return ip_lists()
        if self is DumpDataScopes.CONFIGS:
            return configs()
