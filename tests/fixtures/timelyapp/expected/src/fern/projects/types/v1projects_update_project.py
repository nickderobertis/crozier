

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1projects_update_project_budget_recurrence_item import V1ProjectsUpdateProjectBudgetRecurrenceItem
from .v1projects_update_project_budget_scope import V1ProjectsUpdateProjectBudgetScope
from .v1projects_update_project_budget_type import V1ProjectsUpdateProjectBudgetType
from .v1projects_update_project_labels_item import V1ProjectsUpdateProjectLabelsItem
from .v1projects_update_project_rate_type import V1ProjectsUpdateProjectRateType
from .v1projects_update_project_users_item import V1ProjectsUpdateProjectUsersItem


class V1ProjectsUpdateProject(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project name
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Hex color code (3-6 characters, without #)
    """

    company_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Client ID. Not required if "new_company" or "client_id" attribute filled
    """

    client_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    Client ID (alias for company_id). Not required if "new_company" or "company_id" attribute filled
    """

    new_company: typing.Optional[str] = pydantic.Field(default=None)
    """
    Create new client with this name. Not required if "company_id" or "client_id" attribute filled
    """

    hour_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Hourly rate for the project
    """

    rate_type: typing.Optional[V1ProjectsUpdateProjectRateType] = pydantic.Field(default=None)
    """
    Rate type for the project (e.g., project, user)
    """

    budget: typing.Optional[float] = pydantic.Field(default=None)
    """
    Budget amount (hours or money depending on budget_type)
    """

    budget_type: typing.Optional[V1ProjectsUpdateProjectBudgetType] = pydantic.Field(default=None)
    """
    Budget type: hours or money
    """

    billable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the project is billable by default
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the project is active
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External reference ID for integrations
    """

    budget_scope: typing.Optional[V1ProjectsUpdateProjectBudgetScope] = pydantic.Field(default=None)
    """
    Budget scope: project-wide or per tag
    """

    send_invite: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to send invitation emails to project users
    """

    required_notes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Deprecated: Use required_label_ids instead
    """

    required_labels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Deprecated: Use label_ids with required_label_ids instead
    """

    enable_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether tags are enabled for this project
    """

    default_labels: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to use default tags
    """

    allow_only_one_tag: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether only one tag is allowed per time entry
    """

    invoice_by_budget: typing.Optional[int] = pydantic.Field(default=None)
    """
    Invoice settings based on budget
    """

    team_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of team IDs to assign to the project
    """

    update_hour_billable_state: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to update billable state of existing hours
    """

    currency_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Currency code for the project (e.g., USD, EUR)
    """

    exchange_rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    Exchange rate for currency conversion
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Project description
    """

    label_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of tag IDs to assign to the project
    """

    required_label_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of tag IDs that are required for time entries
    """

    users: typing.Optional[typing.List[V1ProjectsUpdateProjectUsersItem]] = pydantic.Field(default=None)
    """
    Array of users to assign to the project with their hourly rates
    """

    labels: typing.Optional[typing.List[V1ProjectsUpdateProjectLabelsItem]] = pydantic.Field(default=None)
    """
    Array of tags with their configurations
    """

    budget_recurrence: typing.Optional[typing.List[V1ProjectsUpdateProjectBudgetRecurrenceItem]] = pydantic.Field(
        default=None
    )
    """
    Budget recurrence rules for recurring budget allocation
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
