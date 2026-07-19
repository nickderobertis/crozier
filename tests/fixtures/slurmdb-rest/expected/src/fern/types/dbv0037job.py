

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_short_info import Dbv0037AssociationShortInfo
from .dbv0037job_array import Dbv0037JobArray
from .dbv0037job_comment import Dbv0037JobComment
from .dbv0037job_exit_code import Dbv0037JobExitCode
from .dbv0037job_het import Dbv0037JobHet
from .dbv0037job_mcs import Dbv0037JobMcs
from .dbv0037job_required import Dbv0037JobRequired
from .dbv0037job_reservation import Dbv0037JobReservation
from .dbv0037job_state import Dbv0037JobState
from .dbv0037job_step import Dbv0037JobStep
from .dbv0037job_time import Dbv0037JobTime
from .dbv0037job_tres import Dbv0037JobTres
from .dbv0037job_wckey import Dbv0037JobWckey


class Dbv0037Job(UniversalBaseModel):
    """
    Single job description
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account charged by job
    """

    comment: typing.Optional[Dbv0037JobComment] = None
    allocation_nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    Nodes allocated to job
    """

    array: typing.Optional[Dbv0037JobArray] = None
    time: typing.Optional[Dbv0037JobTime] = None
    association: typing.Optional[Dbv0037AssociationShortInfo] = None
    cluster: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned cluster
    """

    constraints: typing.Optional[str] = pydantic.Field(default=None)
    """
    Constraints on job
    """

    derived_exit_code: typing.Optional[Dbv0037JobExitCode] = None
    exit_code: typing.Optional[Dbv0037JobExitCode] = None
    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of job
    """

    group: typing.Optional[str] = pydantic.Field(default=None)
    """
    User's group to run job
    """

    het: typing.Optional[Dbv0037JobHet] = None
    job_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Job id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned job name
    """

    mcs: typing.Optional[Dbv0037JobMcs] = None
    nodes: typing.Optional[str] = pydantic.Field(default=None)
    """
    List of nodes allocated for job
    """

    partition: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned job's partition
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    Priority
    """

    qos: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned qos name
    """

    required: typing.Optional[Dbv0037JobRequired] = None
    kill_request_user: typing.Optional[str] = pydantic.Field(default=None)
    """
    User who requested job killed
    """

    reservation: typing.Optional[Dbv0037JobReservation] = None
    state: typing.Optional[Dbv0037JobState] = None
    steps: typing.Optional[typing.List[Dbv0037JobStep]] = pydantic.Field(default=None)
    """
    Job step description
    """

    tres: typing.Optional[Dbv0037JobTres] = None
    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    Job user
    """

    wckey: typing.Optional[Dbv0037JobWckey] = None
    working_directory: typing.Optional[str] = pydantic.Field(default=None)
    """
    Directory where job was initially started
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
