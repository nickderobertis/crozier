

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BillingCyclesResponse(UniversalBaseModel):
    billing_cycle_array: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Optional[str]]],
        FieldMetadata(alias="billingCycleArray"),
        pydantic.Field(alias="billingCycleArray", description="Array of previous 12 Billing Cycles."),
    ] = None
    """
    Array of previous 12 Billing Cycles.
    """

    object: str = pydantic.Field()
    """
    Name of the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
