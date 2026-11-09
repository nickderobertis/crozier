

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BillingCycleUsageResponseBillingCycle(UniversalBaseModel):
    """
    StartDate and endDate of the billing cycle.
    """

    end_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="endDate"),
        pydantic.Field(alias="endDate", description="End date of the billing cycle."),
    ]
    """
    End date of the billing cycle.
    """

    start_date: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startDate"),
        pydantic.Field(alias="startDate", description="Start date of the billing cycle."),
    ]
    """
    Start date of the billing cycle.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
