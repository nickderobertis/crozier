

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CatalogCustomAttributeDefinitionAppVisibility(str, enum.Enum):
    """
    Defines the visibility of a custom attribute to applications other than their
    creating application.
    """

    APP_VISIBILITY_HIDDEN = "APP_VISIBILITY_HIDDEN"
    APP_VISIBILITY_READ_ONLY = "APP_VISIBILITY_READ_ONLY"
    APP_VISIBILITY_READ_WRITE_VALUES = "APP_VISIBILITY_READ_WRITE_VALUES"

    def visit(
        self,
        app_visibility_hidden: typing.Callable[[], T_Result],
        app_visibility_read_only: typing.Callable[[], T_Result],
        app_visibility_read_write_values: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogCustomAttributeDefinitionAppVisibility.APP_VISIBILITY_HIDDEN:
            return app_visibility_hidden()
        if self is CatalogCustomAttributeDefinitionAppVisibility.APP_VISIBILITY_READ_ONLY:
            return app_visibility_read_only()
        if self is CatalogCustomAttributeDefinitionAppVisibility.APP_VISIBILITY_READ_WRITE_VALUES:
            return app_visibility_read_write_values()
