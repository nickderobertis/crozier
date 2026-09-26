

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectSetupRequestStep(enum.StrEnum):
    """
    Workflow step: "discover" (default) starts new session and returns file list, "reportScan" analyzes scan results, "generateScope" generates all files in a scope. Defaults to "discover" if omitted.
    """

    DISCOVER = "discover"
    REPORT_SCAN = "reportScan"
    GENERATE_SCOPE = "generateScope"

    def visit(
        self,
        discover: typing.Callable[[], T_Result],
        report_scan: typing.Callable[[], T_Result],
        generate_scope: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectSetupRequestStep.DISCOVER:
            return discover()
        if self is ProjectSetupRequestStep.REPORT_SCAN:
            return report_scan()
        if self is ProjectSetupRequestStep.GENERATE_SCOPE:
            return generate_scope()
