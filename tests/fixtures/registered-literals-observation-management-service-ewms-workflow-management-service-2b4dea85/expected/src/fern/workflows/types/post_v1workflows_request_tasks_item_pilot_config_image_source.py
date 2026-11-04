

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostV1WorkflowsRequestTasksItemPilotConfigImageSource(enum.StrEnum):
    """
    The canonical source name for the image.
    """

    CVMFS = "cvmfs"
    AUTO = "auto"

    def visit(self, cvmfs: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostV1WorkflowsRequestTasksItemPilotConfigImageSource.CVMFS:
            return cvmfs()
        if self is PostV1WorkflowsRequestTasksItemPilotConfigImageSource.AUTO:
            return auto()
