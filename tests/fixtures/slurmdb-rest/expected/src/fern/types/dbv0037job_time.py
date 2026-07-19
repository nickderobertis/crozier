

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037job_time_system import Dbv0037JobTimeSystem
from .dbv0037job_time_total import Dbv0037JobTimeTotal
from .dbv0037job_time_user import Dbv0037JobTimeUser


class Dbv0037JobTime(UniversalBaseModel):
    """
    Time properties
    """

    elapsed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time elapsed
    """

    eligible: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time eligible to run
    """

    end: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job ended
    """

    start: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job started
    """

    submission: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job submitted
    """

    suspended: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of when job last suspended
    """

    system: typing.Optional[Dbv0037JobTimeSystem] = None
    total: typing.Optional[Dbv0037JobTimeTotal] = None
    user: typing.Optional[Dbv0037JobTimeUser] = None
    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Job wall clock time limit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
