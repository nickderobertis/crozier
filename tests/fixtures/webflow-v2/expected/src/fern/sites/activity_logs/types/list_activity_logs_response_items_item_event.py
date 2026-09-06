

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListActivityLogsResponseItemsItemEvent(enum.StrEnum):
    STYLES_MODIFIED = "styles_modified"
    SITE_PUBLISHED = "site_published"
    IX2MODIFIED_ON_PAGE = "ix2_modified_on_page"
    PAGE_DOM_MODIFIED = "page_dom_modified"
    CMS_ITEM = "cms_item"
    BACKUP_CREATED = "backup_created"
    PAGE_CUSTOM_CODE_MODIFIED = "page_custom_code_modified"
    SYMBOLS_MODIFIED = "symbols_modified"
    VARIABLE_MODIFIED = "variable_modified"
    VARIABLES_MODIFIED = "variables_modified"
    CMS_COLLECTION = "cms_collection"
    PAGE_SETTINGS_MODIFIED = "page_settings_modified"
    PAGE_SETTINGS_CUSTOM_CODE_MODIFIED = "page_settings_custom_code_modified"
    IX2MODIFIED_ON_COMPONENT = "ix2_modified_on_component"
    IX2MODIFIED_ON_CLASS = "ix2_modified_on_class"
    SITE_CUSTOM_CODE_MODIFIED = "site_custom_code_modified"
    PAGE_DUPLICATED = "page_duplicated"
    SECONDARY_LOCALE_PAGE_CONTENT_MODIFIED = "secondary_locale_page_content_modified"
    PAGE_RENAMED = "page_renamed"
    PAGE_CREATED = "page_created"
    PAGE_DELETED = "page_deleted"
    SITE_UNPUBLISHED = "site_unpublished"
    BACKUP_RESTORED = "backup_restored"
    LOCALE_ADDED = "locale_added"
    BRANCH_CREATED = "branch_created"
    LOCALE_DISPLAY_NAME_UPDATED = "locale_display_name_updated"
    LOCALE_SUBDIRECTORY_UPDATED = "locale_subdirectory_updated"
    BRANCH_MERGED = "branch_merged"
    LOCALE_TAG_UPDATED = "locale_tag_updated"
    BRANCH_DELETED = "branch_deleted"
    LOCALE_ENABLED = "locale_enabled"
    LOCALE_REMOVED = "locale_removed"
    LOCALE_DISABLED = "locale_disabled"
    LIBRARY_SHARED = "library_shared"
    LIBRARY_UNSHARED = "library_unshared"
    LIBRARY_INSTALLED = "library_installed"
    LIBRARY_UNINSTALLED = "library_uninstalled"
    LIBRARY_UPDATE_SHARED = "library_update_shared"
    LIBRARY_UPDATE_ACCEPTED = "library_update_accepted"
    BRANCH_REVIEW_CREATED = "branch_review_created"
    BRANCH_REVIEW_APPROVED = "branch_review_approved"
    BRANCH_REVIEW_CANCELED = "branch_review_canceled"

    def visit(
        self,
        styles_modified: typing.Callable[[], T_Result],
        site_published: typing.Callable[[], T_Result],
        ix2modified_on_page: typing.Callable[[], T_Result],
        page_dom_modified: typing.Callable[[], T_Result],
        cms_item: typing.Callable[[], T_Result],
        backup_created: typing.Callable[[], T_Result],
        page_custom_code_modified: typing.Callable[[], T_Result],
        symbols_modified: typing.Callable[[], T_Result],
        variable_modified: typing.Callable[[], T_Result],
        variables_modified: typing.Callable[[], T_Result],
        cms_collection: typing.Callable[[], T_Result],
        page_settings_modified: typing.Callable[[], T_Result],
        page_settings_custom_code_modified: typing.Callable[[], T_Result],
        ix2modified_on_component: typing.Callable[[], T_Result],
        ix2modified_on_class: typing.Callable[[], T_Result],
        site_custom_code_modified: typing.Callable[[], T_Result],
        page_duplicated: typing.Callable[[], T_Result],
        secondary_locale_page_content_modified: typing.Callable[[], T_Result],
        page_renamed: typing.Callable[[], T_Result],
        page_created: typing.Callable[[], T_Result],
        page_deleted: typing.Callable[[], T_Result],
        site_unpublished: typing.Callable[[], T_Result],
        backup_restored: typing.Callable[[], T_Result],
        locale_added: typing.Callable[[], T_Result],
        branch_created: typing.Callable[[], T_Result],
        locale_display_name_updated: typing.Callable[[], T_Result],
        locale_subdirectory_updated: typing.Callable[[], T_Result],
        branch_merged: typing.Callable[[], T_Result],
        locale_tag_updated: typing.Callable[[], T_Result],
        branch_deleted: typing.Callable[[], T_Result],
        locale_enabled: typing.Callable[[], T_Result],
        locale_removed: typing.Callable[[], T_Result],
        locale_disabled: typing.Callable[[], T_Result],
        library_shared: typing.Callable[[], T_Result],
        library_unshared: typing.Callable[[], T_Result],
        library_installed: typing.Callable[[], T_Result],
        library_uninstalled: typing.Callable[[], T_Result],
        library_update_shared: typing.Callable[[], T_Result],
        library_update_accepted: typing.Callable[[], T_Result],
        branch_review_created: typing.Callable[[], T_Result],
        branch_review_approved: typing.Callable[[], T_Result],
        branch_review_canceled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActivityLogsResponseItemsItemEvent.STYLES_MODIFIED:
            return styles_modified()
        if self is ListActivityLogsResponseItemsItemEvent.SITE_PUBLISHED:
            return site_published()
        if self is ListActivityLogsResponseItemsItemEvent.IX2MODIFIED_ON_PAGE:
            return ix2modified_on_page()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_DOM_MODIFIED:
            return page_dom_modified()
        if self is ListActivityLogsResponseItemsItemEvent.CMS_ITEM:
            return cms_item()
        if self is ListActivityLogsResponseItemsItemEvent.BACKUP_CREATED:
            return backup_created()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_CUSTOM_CODE_MODIFIED:
            return page_custom_code_modified()
        if self is ListActivityLogsResponseItemsItemEvent.SYMBOLS_MODIFIED:
            return symbols_modified()
        if self is ListActivityLogsResponseItemsItemEvent.VARIABLE_MODIFIED:
            return variable_modified()
        if self is ListActivityLogsResponseItemsItemEvent.VARIABLES_MODIFIED:
            return variables_modified()
        if self is ListActivityLogsResponseItemsItemEvent.CMS_COLLECTION:
            return cms_collection()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_SETTINGS_MODIFIED:
            return page_settings_modified()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_SETTINGS_CUSTOM_CODE_MODIFIED:
            return page_settings_custom_code_modified()
        if self is ListActivityLogsResponseItemsItemEvent.IX2MODIFIED_ON_COMPONENT:
            return ix2modified_on_component()
        if self is ListActivityLogsResponseItemsItemEvent.IX2MODIFIED_ON_CLASS:
            return ix2modified_on_class()
        if self is ListActivityLogsResponseItemsItemEvent.SITE_CUSTOM_CODE_MODIFIED:
            return site_custom_code_modified()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_DUPLICATED:
            return page_duplicated()
        if self is ListActivityLogsResponseItemsItemEvent.SECONDARY_LOCALE_PAGE_CONTENT_MODIFIED:
            return secondary_locale_page_content_modified()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_RENAMED:
            return page_renamed()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_CREATED:
            return page_created()
        if self is ListActivityLogsResponseItemsItemEvent.PAGE_DELETED:
            return page_deleted()
        if self is ListActivityLogsResponseItemsItemEvent.SITE_UNPUBLISHED:
            return site_unpublished()
        if self is ListActivityLogsResponseItemsItemEvent.BACKUP_RESTORED:
            return backup_restored()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_ADDED:
            return locale_added()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_CREATED:
            return branch_created()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_DISPLAY_NAME_UPDATED:
            return locale_display_name_updated()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_SUBDIRECTORY_UPDATED:
            return locale_subdirectory_updated()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_MERGED:
            return branch_merged()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_TAG_UPDATED:
            return locale_tag_updated()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_DELETED:
            return branch_deleted()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_ENABLED:
            return locale_enabled()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_REMOVED:
            return locale_removed()
        if self is ListActivityLogsResponseItemsItemEvent.LOCALE_DISABLED:
            return locale_disabled()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_SHARED:
            return library_shared()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_UNSHARED:
            return library_unshared()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_INSTALLED:
            return library_installed()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_UNINSTALLED:
            return library_uninstalled()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_UPDATE_SHARED:
            return library_update_shared()
        if self is ListActivityLogsResponseItemsItemEvent.LIBRARY_UPDATE_ACCEPTED:
            return library_update_accepted()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_REVIEW_CREATED:
            return branch_review_created()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_REVIEW_APPROVED:
            return branch_review_approved()
        if self is ListActivityLogsResponseItemsItemEvent.BRANCH_REVIEW_CANCELED:
            return branch_review_canceled()
