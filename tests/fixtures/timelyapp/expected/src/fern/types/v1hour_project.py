

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1hour_project_billed_cost import V1HourProjectBilledCost
from .v1hour_project_billed_duration import V1HourProjectBilledDuration
from .v1hour_project_client import V1HourProjectClient
from .v1hour_project_cost import V1HourProjectCost
from .v1hour_project_currency import V1HourProjectCurrency
from .v1hour_project_duration import V1HourProjectDuration
from .v1hour_project_estimated_cost import V1HourProjectEstimatedCost
from .v1hour_project_estimated_duration import V1HourProjectEstimatedDuration
from .v1hour_project_labels_item import V1HourProjectLabelsItem
from .v1hour_project_unbilled_cost import V1HourProjectUnbilledCost
from .v1hour_project_unbilled_duration import V1HourProjectUnbilledDuration


class V1HourProject(UniversalBaseModel):
    """
    Project this time was logged to
    """

    id: int
    active: bool
    account_id: int
    name: str
    description: typing.Optional[str] = None
    color: str
    rate_type: str
    billable: bool
    created_at: int
    updated_at: int
    external_id: typing.Optional[str] = None
    budget_scope: typing.Optional[str] = None
    client: V1HourProjectClient
    required_notes: bool
    required_labels: bool
    budget_expired_on: typing.Optional[str] = None
    has_recurrence: bool
    enable_labels: str
    default_labels: bool
    allow_only_one_tag: bool
    currency: V1HourProjectCurrency
    team_ids: typing.List[int]
    budget: typing.Optional[int] = None
    budget_type: typing.Optional[str] = None
    budget_calculation: typing.Optional[str] = None
    hour_rate: typing.Optional[float] = None
    hour_rate_in_cents: typing.Optional[float] = None
    budget_progress: typing.Optional[float] = None
    budget_percent: typing.Optional[float] = None
    invoice_by_budget: typing.Optional[bool] = None
    labels: typing.List[V1HourProjectLabelsItem]
    label_ids: typing.List[int]
    required_label_ids: typing.List[int]
    default_label_ids: typing.List[int]
    created_from: str
    cost: typing.Optional[V1HourProjectCost] = None
    estimated_cost: typing.Optional[V1HourProjectEstimatedCost] = None
    billed_cost: typing.Optional[V1HourProjectBilledCost] = None
    unbilled_cost: typing.Optional[V1HourProjectUnbilledCost] = None
    duration: typing.Optional[V1HourProjectDuration] = None
    estimated_duration: typing.Optional[V1HourProjectEstimatedDuration] = None
    billed_duration: typing.Optional[V1HourProjectBilledDuration] = None
    unbilled_duration: typing.Optional[V1HourProjectUnbilledDuration] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
