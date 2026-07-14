

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dag_state import DagState


class BasicDagRun(UniversalBaseModel):
    dag_id: typing.Optional[str] = None
    data_interval_end: typing.Optional[dt.datetime] = None
    data_interval_start: typing.Optional[dt.datetime] = None
    end_date: typing.Optional[dt.datetime] = None
    logical_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The logical date (previously called execution date). This is the time or interval covered by
    this DAG run, according to the DAG definition.
    
    The value of this field can be set only when creating the object. If you try to modify the
    field of an existing object, the request fails with an BAD_REQUEST error.
    
    This together with DAG_ID are a unique key.
    
    *New in version 2.2.0*
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Run ID.
    """

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
