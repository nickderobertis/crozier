

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem(enum.StrEnum):
    INTERNAL = "internal"
    ALPHA = "alpha"
    BETA = "beta"
    GA = "ga"
    WITHDRAWN = "withdrawn"
    PREVIEW = "preview"

    def visit(
        self,
        internal: typing.Callable[[], T_Result],
        alpha: typing.Callable[[], T_Result],
        beta: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
        preview: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.INTERNAL:
            return internal()
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.ALPHA:
            return alpha()
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.BETA:
            return beta()
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.GA:
            return ga()
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.WITHDRAWN:
            return withdrawn()
        if self is V1OrganizationSlugResponseOutputAllowedReleaseChannelsItem.PREVIEW:
            return preview()
