

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .class_reference import ClassReference
from .color import Color
from .dag import Dag
from .task_extra_links_item import TaskExtraLinksItem
from .time_delta import TimeDelta
from .trigger_rule import TriggerRule
from .weight_rule import WeightRule


class Task(UniversalBaseModel):
    """
    For details see:
    [airflow.models.BaseOperator](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/index.html#airflow.models.BaseOperator)
    """

    class_ref: typing.Optional[ClassReference] = None
    depends_on_past: typing.Optional[bool] = None
    downstream_task_ids: typing.Optional[typing.List[str]] = None
    end_date: typing.Optional[dt.datetime] = None
    execution_timeout: typing.Optional[TimeDelta] = None
    extra_links: typing.Optional[typing.List[TaskExtraLinksItem]] = None
    is_mapped: typing.Optional[bool] = None
    owner: typing.Optional[str] = None
    pool: typing.Optional[str] = None
    pool_slots: typing.Optional[float] = None
    priority_weight: typing.Optional[float] = None
    queue: typing.Optional[str] = None
    retries: typing.Optional[float] = None
    retry_delay: typing.Optional[TimeDelta] = None
    retry_exponential_backoff: typing.Optional[bool] = None
    start_date: typing.Optional[dt.datetime] = None
    sub_dag: typing.Optional[Dag] = None
    task_id: typing.Optional[str] = None
    template_fields: typing.Optional[typing.List[str]] = None
    trigger_rule: typing.Optional[TriggerRule] = None
    ui_color: typing.Optional[Color] = None
    ui_fgcolor: typing.Optional[Color] = None
    wait_for_downstream: typing.Optional[bool] = None
    weight_rule: typing.Optional[WeightRule] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
