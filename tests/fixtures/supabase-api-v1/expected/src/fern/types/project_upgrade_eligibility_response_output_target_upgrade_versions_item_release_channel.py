

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel(enum.StrEnum):
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
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.INTERNAL:
            return internal()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.ALPHA:
            return alpha()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.BETA:
            return beta()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.GA:
            return ga()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.WITHDRAWN:
            return withdrawn()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemReleaseChannel.PREVIEW:
            return preview()
