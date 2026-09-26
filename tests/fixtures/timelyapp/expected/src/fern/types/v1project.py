

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1project_billable_duration import V1ProjectBillableDuration
from .v1project_billed_cost import V1ProjectBilledCost
from .v1project_billed_duration import V1ProjectBilledDuration
from .v1project_budget_calculation import V1ProjectBudgetCalculation
from .v1project_budget_scope import V1ProjectBudgetScope
from .v1project_budget_type import V1ProjectBudgetType
from .v1project_client import V1ProjectClient
from .v1project_cost import V1ProjectCost
from .v1project_currency import V1ProjectCurrency
from .v1project_duration import V1ProjectDuration
from .v1project_enable_labels import V1ProjectEnableLabels
from .v1project_estimated_cost import V1ProjectEstimatedCost
from .v1project_estimated_duration import V1ProjectEstimatedDuration
from .v1project_internal_cost import V1ProjectInternalCost
from .v1project_labels_item import V1ProjectLabelsItem
from .v1project_non_billable_duration import V1ProjectNonBillableDuration
from .v1project_profit import V1ProjectProfit
from .v1project_rate_type import V1ProjectRateType
from .v1project_tic import V1ProjectTic
from .v1project_unbilled_cost import V1ProjectUnbilledCost
from .v1project_unbilled_duration import V1ProjectUnbilledDuration
from .v1project_users_item import V1ProjectUsersItem


class V1Project(UniversalBaseModel):
    id: int
    active: bool
    account_id: int
    name: str
    description: typing.Optional[str] = None
    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    hex code
    """

    rate_type: V1ProjectRateType
    billable: bool
    created_at: int
    updated_at: int
    external_id: typing.Optional[str] = None
    budget_scope: typing.Optional[V1ProjectBudgetScope] = None
    client: V1ProjectClient
    required_notes: bool
    required_labels: bool
    budget_expired_on: typing.Optional[dt.datetime] = None
    has_recurrence: bool
    enable_labels: V1ProjectEnableLabels
    created_from: str
    default_labels: bool
    allow_only_one_tag: bool = pydantic.Field()
    """
    Whether only one tag is allowed per time entry
    """

    currency: V1ProjectCurrency
    team_ids: typing.Optional[typing.List[int]] = None
    update_hour_billable_state: typing.Optional[bool] = None
    budget: typing.Optional[float] = None
    budget_type: typing.Optional[V1ProjectBudgetType] = None
    budget_calculation: typing.Optional[V1ProjectBudgetCalculation] = None
    hour_rate: typing.Optional[float] = None
    hour_rate_in_cents: typing.Optional[float] = None
    budget_progress: typing.Optional[float] = None
    budget_percent: typing.Optional[float] = None
    invoice_by_budget: typing.Optional[bool] = None
    users: typing.Optional[typing.List[V1ProjectUsersItem]] = None
    labels: typing.Optional[typing.List[V1ProjectLabelsItem]] = None
    label_ids: typing.Optional[typing.List[int]] = None
    required_label_ids: typing.Optional[typing.List[int]] = None
    default_label_ids: typing.Optional[typing.List[int]] = None
    first_logged_on: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date in ISO 8601 format (YYYY-MM-DD)
    """

    last_logged_on: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date in ISO 8601 format (YYYY-MM-DD)
    """

    locked_hours: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the project has locked or billed or invoiced hours
    """

    tic: typing.Optional[V1ProjectTic] = pydantic.Field(default=None)
    """
    Integration metadata (internal only). Present for synced projects.
    """

    cost: typing.Optional[V1ProjectCost] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    estimated_cost: typing.Optional[V1ProjectEstimatedCost] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    billed_cost: typing.Optional[V1ProjectBilledCost] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    unbilled_cost: typing.Optional[V1ProjectUnbilledCost] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    internal_cost: typing.Optional[V1ProjectInternalCost] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    profit: typing.Optional[V1ProjectProfit] = pydantic.Field(default=None)
    """
    V1::Cost schema or empty object
    """

    duration: typing.Optional[V1ProjectDuration] = None
    estimated_duration: typing.Optional[V1ProjectEstimatedDuration] = None
    billed_duration: typing.Optional[V1ProjectBilledDuration] = None
    unbilled_duration: typing.Optional[V1ProjectUnbilledDuration] = None
    billable_duration: typing.Optional[V1ProjectBillableDuration] = None
    non_billable_duration: typing.Optional[V1ProjectNonBillableDuration] = None
    profitability: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
