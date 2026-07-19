

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_exit_code_signal import Dbv0037JobExitCodeSignal


class Dbv0037JobExitCode(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job exit status
    """

    return_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Return code from parent process
    """

    signal: typing.Optional[Dbv0037JobExitCodeSignal] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
