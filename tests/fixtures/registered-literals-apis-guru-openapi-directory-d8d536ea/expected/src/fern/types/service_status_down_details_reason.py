

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceStatusDownDetailsReason(enum.StrEnum):
    """
    This field determines the reason behind status being down. Following are the possible reason for the service to be down:

        underMaintenance: It means that the site is under scheduled maintenance.

        notIntegrated: When an court with specific case type is not integrated in UniCourt.

        brokenIntegration: Due to some updates made to the court site our existing Integration has broken and will require a fix to be made to support this court again for a spcific case type category.

        sourceMigrated: When a source is migrated from one site to another for a specific case type category.
    """

    UNDER_MAINTENANCE = "underMaintenance"
    NOT_INTEGRATED = "notIntegrated"
    BROKEN_INTEGRATION = "brokenIntegration"
    SOURCE_MIGRATED = "sourceMigrated"

    def visit(
        self,
        under_maintenance: typing.Callable[[], T_Result],
        not_integrated: typing.Callable[[], T_Result],
        broken_integration: typing.Callable[[], T_Result],
        source_migrated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ServiceStatusDownDetailsReason.UNDER_MAINTENANCE:
            return under_maintenance()
        if self is ServiceStatusDownDetailsReason.NOT_INTEGRATED:
            return not_integrated()
        if self is ServiceStatusDownDetailsReason.BROKEN_INTEGRATION:
            return broken_integration()
        if self is ServiceStatusDownDetailsReason.SOURCE_MIGRATED:
            return source_migrated()
