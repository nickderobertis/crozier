

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskforceObjectPilotConfigImageSource(enum.StrEnum):
    """
    The canonical source name for the image.
    """

    CVMFS = "cvmfs"
    AUTO = "auto"

    def visit(self, cvmfs: typing.Callable[[], T_Result], auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaskforceObjectPilotConfigImageSource.CVMFS:
            return cvmfs()
        if self is TaskforceObjectPilotConfigImageSource.AUTO:
            return auto()
