

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency import Currency
from .custom_field import CustomField
from .tags import Tags


class Opportunity(UniversalBaseModel):
    close_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The actual closing date for the opportunity. If close_date is null, the opportunity is not closed yet.
    """

    company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the company associated with the opportunity.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the company associated with the opportunity.
    """

    contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the contact associated with the opportunity.
    """

    contact_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of unique identifiers of all contacts associated with the opportunity.
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the opportunity was created.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the user who created the opportunity.
    """

    currency: typing.Optional[Currency] = None
    custom_fields: typing.Optional[typing.List[CustomField]] = None
    date_last_contacted: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the opportunity was last contacted.
    """

    date_lead_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the lead associated with the opportunity was created.
    """

    date_stage_changed: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the stage of the opportunity was last changed.
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the opportunity has been deleted.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description of the opportunity.
    """

    expected_revenue: typing.Optional[float] = pydantic.Field(default=None)
    """
    The expected revenue from the opportunity
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for the opportunity.
    """

    interaction_count: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of interactions with the opportunity.
    """

    last_activity_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date and time of the last activity associated with the opportunity.
    """

    lead_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the lead associated with the opportunity.
    """

    lead_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source of the lead associated with the opportunity.
    """

    loss_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason why the opportunity was lost.
    """

    loss_reason_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the reason why the opportunity was lost.
    """

    monetary_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    The monetary value associated with the opportunity
    """

    owner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the user who owns the opportunity.
    """

    pipeline_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the pipeline associated with the opportunity
    """

    pipeline_stage_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the stage in the pipeline associated with the opportunity.
    """

    primary_contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the primary contact associated with the opportunity.
    """

    priority: typing.Optional[str] = pydantic.Field(default=None)
    """
    The priority level of the opportunity.
    """

    source_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the source of the opportunity.
    """

    stage_last_changed_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the stage of the opportunity was last changed.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current status of the opportunity.
    """

    status_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the current status of the opportunity.
    """

    tags: typing.Optional[Tags] = None
    title: str = pydantic.Field()
    """
    The title or name of the opportunity.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the opportunity
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the opportunity was last updated.
    """

    updated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the user who last updated the opportunity.
    """

    win_probability: typing.Optional[float] = pydantic.Field(default=None)
    """
    The probability of winning the opportunity, expressed as a percentage.
    """

    won_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason why the opportunity was won.
    """

    won_reason_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the reason why the opportunity was won.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
