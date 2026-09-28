

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OtoroshiModelsRemainingQuotas(UniversalBaseModel):
    """
    Remaining quotas for an apikey
    """

    throttling_calls_per_window: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="throttlingCallsPerWindow"),
        pydantic.Field(alias="throttlingCallsPerWindow", description="Current number of call per window"),
    ] = None
    """
    Current number of call per window
    """

    remaining_calls_per_window: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="remainingCallsPerWindow"),
        pydantic.Field(alias="remainingCallsPerWindow", description="Remaining number of call per window"),
    ] = None
    """
    Remaining number of call per window
    """

    current_calls_per_day: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentCallsPerDay"),
        pydantic.Field(alias="currentCallsPerDay", description="Current number of call per day"),
    ] = None
    """
    Current number of call per day
    """

    authorized_calls_per_day: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="authorizedCallsPerDay"),
        pydantic.Field(alias="authorizedCallsPerDay", description="Number of authorized call per day"),
    ] = None
    """
    Number of authorized call per day
    """

    current_calls_per_month: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="currentCallsPerMonth"),
        pydantic.Field(alias="currentCallsPerMonth", description="Current number of call per month"),
    ] = None
    """
    Current number of call per month
    """

    remaining_calls_per_month: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="remainingCallsPerMonth"),
        pydantic.Field(alias="remainingCallsPerMonth", description="Remaining number of call per month"),
    ] = None
    """
    Remaining number of call per month
    """

    authorized_calls_per_window: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="authorizedCallsPerWindow"),
        pydantic.Field(alias="authorizedCallsPerWindow", description="Number of authorized call per window"),
    ] = None
    """
    Number of authorized call per window
    """

    authorized_calls_per_month: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="authorizedCallsPerMonth"),
        pydantic.Field(alias="authorizedCallsPerMonth", description="Number of authorized call per month"),
    ] = None
    """
    Number of authorized call per month
    """

    remaining_calls_per_day: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="remainingCallsPerDay"),
        pydantic.Field(alias="remainingCallsPerDay", description="Remaining number of call per day"),
    ] = None
    """
    Remaining number of call per day
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
