

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dag_run_run_type import DagRunRunType
from .dag_state import DagState


class DagRun(UniversalBaseModel):
    conf: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    JSON object describing additional configuration parameters.
    
    The value of this field can be set only when creating the object. If you try to modify the
    field of an existing object, the request fails with an BAD_REQUEST error.
    """

    dag_id: typing.Optional[str] = None
    dag_run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Run ID.
    
    The value of this field can be set only when creating the object. If you try to modify the
    field of an existing object, the request fails with an BAD_REQUEST error.
    
    If not provided, a value will be generated based on execution_date.
    
    If the specified dag_run_id is in use, the creation request fails with an ALREADY_EXISTS error.
    
    This together with DAG_ID are a unique key.
    """

    data_interval_end: typing.Optional[dt.datetime] = None
    data_interval_start: typing.Optional[dt.datetime] = None
    end_date: typing.Optional[dt.datetime] = None
    execution_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The execution date. This is the same as logical_date, kept for backwards compatibility.
    If both this field and logical_date are provided but with different values, the request
    will fail with an BAD_REQUEST error.
    
    *Changed in version 2.2.0*&#58; Field becomes nullable.
    
    *Deprecated since version 2.2.0*&#58; Use 'logical_date' instead.
    """

    external_trigger: typing.Optional[bool] = None
    last_scheduling_decision: typing.Optional[dt.datetime] = None
    logical_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The logical date (previously called execution date). This is the time or interval covered by
    this DAG run, according to the DAG definition.
    
    The value of this field can be set only when creating the object. If you try to modify the
    field of an existing object, the request fails with an BAD_REQUEST error.
    
    This together with DAG_ID are a unique key.
    
    *New in version 2.2.0*
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contains manually entered notes by the user about the DagRun.
    
    *New in version 2.5.0*
    """

    run_type: typing.Optional[DagRunRunType] = None
    start_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The start time. The time when DAG run was actually created.
    
    *Changed in version 2.1.3*&#58; Field becomes nullable.
    """

    state: typing.Optional[DagState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
