

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1projects_update_project_budget_recurrence_item_recur import V1ProjectsUpdateProjectBudgetRecurrenceItemRecur
from .v1projects_update_project_budget_recurrence_item_recur_until import (
    V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil,
)


class V1ProjectsUpdateProjectBudgetRecurrenceItem(UniversalBaseModel):
    recur: V1ProjectsUpdateProjectBudgetRecurrenceItemRecur = pydantic.Field()
    """
    Recurrence pattern: monthly or until end date
    """

    start_date: dt.datetime = pydantic.Field()
    """
    Start date for budget recurrence
    """

    end_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    End date for budget recurrence. Required when recur_until is end_date
    """

    recur_until: V1ProjectsUpdateProjectBudgetRecurrenceItemRecurUntil = pydantic.Field()
    """
    When to stop recurring: until end date or until project is archived
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
