

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ADMIN_GROUPS = "AdminGroups"
    """
    Administer Group/Clan Forums, Wall, and Members for groups and clans that the 
    user is a founder or an administrator.
    """

    ADVANCED_WRITE_ACTIONS = "AdvancedWriteActions"
    """
    Can perform actions that will result in a prompt to the user via the Destiny app.
    """

    BNET_WRITE = "BnetWrite"
    """
    Create new groups, clans, and forum posts, along with other actions that are reserved for Bungie.net
    elevated scope: not meant to be used by third party applications.
    """

    DESTINY_UNLOCK_VALUE_QUERY = "DestinyUnlockValueQuery"
    """
    Allows an app to query sensitive information like unlock flags and values not available through normal methods.
    """

    EDIT_USER_DATA = "EditUserData"
    """
    Edit user data such as preferred language, status, motto, avatar selection and theme.
    """

    MOVE_EQUIP_DESTINY_ITEMS = "MoveEquipDestinyItems"
    """
    Move or equip Destiny items
    """

    PARTNER_OFFER_GRANT = "PartnerOfferGrant"
    """
    Can use the partner offer api to claim rewards defined for a partner
    """

    READ_AND_APPLY_TOKENS = "ReadAndApplyTokens"
    """
    Read offer history and claim and apply tokens for the user.
    """

    READ_BASIC_USER_PROFILE = "ReadBasicUserProfile"
    """
    Read basic user profile information such as the user's handle, avatar icon, etc.
    """

    READ_DESTINY_INVENTORY_AND_VAULT = "ReadDestinyInventoryAndVault"
    """
    Read Destiny 1 Inventory and Vault contents.
    For Destiny 2, this scope is needed to read anything regarded as private. This is the only scope a
    Destiny 2 app needs for read operations against Destiny 2 data such as inventory, vault, currency,
    vendors, milestones, progression, etc.
    """

    READ_DESTINY_VENDORS_AND_ADVISORS = "ReadDestinyVendorsAndAdvisors"
    """
    Access vendor and advisor data specific to a user. OBSOLETE. This scope is only used on the Destiny 1 API.
    """

    READ_GROUPS = "ReadGroups"
    """
    Read Group/Clan Forums, Wall, and Members for groups and clans that the 
    user has joined.
    """

    READ_USER_DATA = "ReadUserData"
    """
    Read user data such as who they are web notifications, 
    clan/group memberships, recent activity, muted users.
    """

    USER_PII_READ = "UserPiiRead"
    """
    Allows an app to query sensitive user PII, most notably email information.
    """

    WRITE_GROUPS = "WriteGroups"
    """
    Write Group/Clan Forums, Wall, and Members for groups and clans that the 
    user has joined.
    """

    def visit(
        self,
        admin_groups: typing.Callable[[], T_Result],
        advanced_write_actions: typing.Callable[[], T_Result],
        bnet_write: typing.Callable[[], T_Result],
        destiny_unlock_value_query: typing.Callable[[], T_Result],
        edit_user_data: typing.Callable[[], T_Result],
        move_equip_destiny_items: typing.Callable[[], T_Result],
        partner_offer_grant: typing.Callable[[], T_Result],
        read_and_apply_tokens: typing.Callable[[], T_Result],
        read_basic_user_profile: typing.Callable[[], T_Result],
        read_destiny_inventory_and_vault: typing.Callable[[], T_Result],
        read_destiny_vendors_and_advisors: typing.Callable[[], T_Result],
        read_groups: typing.Callable[[], T_Result],
        read_user_data: typing.Callable[[], T_Result],
        user_pii_read: typing.Callable[[], T_Result],
        write_groups: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ADMIN_GROUPS:
            return admin_groups()
        if self is OauthScope.ADVANCED_WRITE_ACTIONS:
            return advanced_write_actions()
        if self is OauthScope.BNET_WRITE:
            return bnet_write()
        if self is OauthScope.DESTINY_UNLOCK_VALUE_QUERY:
            return destiny_unlock_value_query()
        if self is OauthScope.EDIT_USER_DATA:
            return edit_user_data()
        if self is OauthScope.MOVE_EQUIP_DESTINY_ITEMS:
            return move_equip_destiny_items()
        if self is OauthScope.PARTNER_OFFER_GRANT:
            return partner_offer_grant()
        if self is OauthScope.READ_AND_APPLY_TOKENS:
            return read_and_apply_tokens()
        if self is OauthScope.READ_BASIC_USER_PROFILE:
            return read_basic_user_profile()
        if self is OauthScope.READ_DESTINY_INVENTORY_AND_VAULT:
            return read_destiny_inventory_and_vault()
        if self is OauthScope.READ_DESTINY_VENDORS_AND_ADVISORS:
            return read_destiny_vendors_and_advisors()
        if self is OauthScope.READ_GROUPS:
            return read_groups()
        if self is OauthScope.READ_USER_DATA:
            return read_user_data()
        if self is OauthScope.USER_PII_READ:
            return user_pii_read()
        if self is OauthScope.WRITE_GROUPS:
            return write_groups()
