

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BillingProperties(UniversalBaseModel):
    billing_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="billingType"), pydantic.Field(alias="billingType")
    ] = None
    channel_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="channelType"), pydantic.Field(alias="channelType")
    ] = None
    payment_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="paymentType"), pydantic.Field(alias="paymentType")
    ] = None
    tier: typing.Optional[str] = None
    workload_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workloadType"), pydantic.Field(alias="workloadType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
