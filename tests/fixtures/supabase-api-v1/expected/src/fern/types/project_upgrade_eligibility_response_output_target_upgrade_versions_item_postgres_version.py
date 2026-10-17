

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion(enum.StrEnum):
    THIRTEEN = "13"
    FOURTEEN = "14"
    FIFTEEN = "15"
    SEVENTEEN = "17"
    SEVENTEEN_ORIOLE = "17-oriole"

    def visit(
        self,
        thirteen: typing.Callable[[], T_Result],
        fourteen: typing.Callable[[], T_Result],
        fifteen: typing.Callable[[], T_Result],
        seventeen: typing.Callable[[], T_Result],
        seventeen_oriole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion.THIRTEEN:
            return thirteen()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion.FOURTEEN:
            return fourteen()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion.FIFTEEN:
            return fifteen()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion.SEVENTEEN:
            return seventeen()
        if self is ProjectUpgradeEligibilityResponseOutputTargetUpgradeVersionsItemPostgresVersion.SEVENTEEN_ORIOLE:
            return seventeen_oriole()
