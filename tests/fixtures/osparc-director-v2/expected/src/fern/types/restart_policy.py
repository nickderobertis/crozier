

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RestartPolicy(enum.StrEnum):
    """
    Content of "simcore.service.restart-policy" label
    """

    NO_RESTART = "no-restart"
    ON_INPUTS_DOWNLOADED = "on-inputs-downloaded"

    def visit(
        self, no_restart: typing.Callable[[], T_Result], on_inputs_downloaded: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is RestartPolicy.NO_RESTART:
            return no_restart()
        if self is RestartPolicy.ON_INPUTS_DOWNLOADED:
            return on_inputs_downloaded()
