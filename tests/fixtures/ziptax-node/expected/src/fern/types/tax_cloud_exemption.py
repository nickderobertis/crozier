

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TaxCloudExemption(UniversalBaseModel):
    exemption_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="exemptionId"),
        pydantic.Field(
            alias="exemptionId",
            description="Identifier of an exemption certificate previously created for the customer (see /merchant/cert/create). When provided, the customer is treated as exempt and the certificate is associated with the transaction.",
        ),
    ] = None
    """
    Identifier of an exemption certificate previously created for the customer (see /merchant/cert/create). When provided, the customer is treated as exempt and the certificate is associated with the transaction.
    """

    is_exempt: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isExempt"),
        pydantic.Field(
            alias="isExempt",
            description="Whether the customer is exempt from sales tax. Assumed true when exemptionId is provided.",
        ),
    ] = None
    """
    Whether the customer is exempt from sales tax. Assumed true when exemptionId is provided.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
