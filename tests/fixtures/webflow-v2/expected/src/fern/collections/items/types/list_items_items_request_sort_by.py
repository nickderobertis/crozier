

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListItemsItemsRequestSortBy(enum.StrEnum):
    CREATED_ON = "createdOn"
    LAST_PUBLISHED = "lastPublished"
    LAST_UPDATED = "lastUpdated"
    NAME = "name"
    SLUG = "slug"

    def visit(
        self,
        created_on: typing.Callable[[], T_Result],
        last_published: typing.Callable[[], T_Result],
        last_updated: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        slug: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListItemsItemsRequestSortBy.CREATED_ON:
            return created_on()
        if self is ListItemsItemsRequestSortBy.LAST_PUBLISHED:
            return last_published()
        if self is ListItemsItemsRequestSortBy.LAST_UPDATED:
            return last_updated()
        if self is ListItemsItemsRequestSortBy.NAME:
            return name()
        if self is ListItemsItemsRequestSortBy.SLUG:
            return slug()
