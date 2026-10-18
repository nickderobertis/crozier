

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel(enum.StrEnum):
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
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.INTERNAL:
            return internal()
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.ALPHA:
            return alpha()
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.BETA:
            return beta()
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.GA:
            return ga()
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.WITHDRAWN:
            return withdrawn()
        if self is ProjectUpgradeEligibilityResponseOutputCurrentAppVersionReleaseChannel.PREVIEW:
            return preview()
