

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_time_system import Dbv0037JobTimeSystem
from .dbv0037job_time_total import Dbv0037JobTimeTotal
from .dbv0037job_time_user import Dbv0037JobTimeUser


class Dbv0037JobStepTime(UniversalBaseModel):
    """
    Time properties
    """

    elapsed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time elapsed
    """

    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job ended
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job started
    """

    suspended: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job last suspended
    """

    system: typing.Optional[Dbv0037JobTimeSystem] = None
    total: typing.Optional[Dbv0037JobTimeTotal] = None
    user: typing.Optional[Dbv0037JobTimeUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
