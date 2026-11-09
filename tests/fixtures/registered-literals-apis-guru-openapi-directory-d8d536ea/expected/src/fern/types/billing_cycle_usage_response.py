

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .billing_cycle_usage_response_api_calls_billable import BillingCycleUsageResponseApiCallsBillable
from .billing_cycle_usage_response_api_calls_credited import BillingCycleUsageResponseApiCallsCredited
from .billing_cycle_usage_response_api_calls_made import BillingCycleUsageResponseApiCallsMade
from .billing_cycle_usage_response_billing_cycle import BillingCycleUsageResponseBillingCycle


class BillingCycleUsageResponse(UniversalBaseModel):
    api_calls_billable: typing_extensions.Annotated[
        BillingCycleUsageResponseApiCallsBillable,
        FieldMetadata(alias="apiCallsBillable"),
        pydantic.Field(alias="apiCallsBillable", description="Total number of API calls billed for the billing cycle."),
    ]
    """
    Total number of API calls billed for the billing cycle.
    """

    api_calls_credited: typing_extensions.Annotated[
        BillingCycleUsageResponseApiCallsCredited,
        FieldMetadata(alias="apiCallsCredited"),
        pydantic.Field(
            alias="apiCallsCredited",
            description="Total number of callbackFailures including caseUpdate, caseDocumentOrder and caseExport for the billing cycle.",
        ),
    ]
    """
    Total number of callbackFailures including caseUpdate, caseDocumentOrder and caseExport for the billing cycle.
    """

    api_calls_made: typing_extensions.Annotated[
        BillingCycleUsageResponseApiCallsMade,
        FieldMetadata(alias="apiCallsMade"),
        pydantic.Field(alias="apiCallsMade", description="Total API calls made for the billing cycle."),
    ]
    """
    Total API calls made for the billing cycle.
    """

    api_usage: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="apiUsage"),
        pydantic.Field(alias="apiUsage", description="Billing cycle apiUsage."),
    ]
    """
    Billing cycle apiUsage.
    """

    billing_cycle: typing_extensions.Annotated[
        BillingCycleUsageResponseBillingCycle,
        FieldMetadata(alias="billingCycle"),
        pydantic.Field(alias="billingCycle", description="StartDate and endDate of the billing cycle."),
    ]
    """
    StartDate and endDate of the billing cycle.
    """

    days: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Billing cycle days.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    total_cases_tracked: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCasesTracked"),
        pydantic.Field(alias="totalCasesTracked", description="Total number of successful case tracks."),
    ]
    """
    Total number of successful case tracks.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
