

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60service_taxable import V60ServiceTaxable


class V60Service(UniversalBaseModel):
    adjustment_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="adjustmentType"),
        pydantic.Field(
            alias="adjustmentType", description="Service taxation classification. Currently always 'SERVICE_TAXABLE'."
        ),
    ]
    """
    Service taxation classification. Currently always 'SERVICE_TAXABLE'.
    """

    description: str = pydantic.Field()
    """
    Human-readable explanation of the service taxability determination.
    """

    taxable: V60ServiceTaxable = pydantic.Field()
    """
    Whether services/labor are taxable in this jurisdiction. 'Y' = the service is fully taxable and must be separately stated on the invoice; 'N' = the service is not taxable and must be separately stated on the invoice; 'L' = the service is not taxable, but the labor portion is taxable and both must be separately stated on the invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
