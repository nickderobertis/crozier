

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .taxpayer_identifier_type import TaxpayerIdentifierType


class TaxpayerIdentifier(UniversalBaseModel):
    """
    Information about the Taxpayer identification values assigned to the individual or legal entity.Information about the Taxpayer identification values assigned to the individual or legal entity.
    """

    taxpayer_identifier_type: typing_extensions.Annotated[
        typing.Optional[TaxpayerIdentifierType],
        FieldMetadata(alias="TaxpayerIdentifierType"),
        pydantic.Field(alias="TaxpayerIdentifierType"),
    ] = None
    taxpayer_identifier_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TaxpayerIdentifierValue"),
        pydantic.Field(
            alias="TaxpayerIdentifierValue",
            description="The value of the taxpayer identifier as assigned by the IRS to the individual or legal entity.",
        ),
    ] = None
    """
    The value of the taxpayer identifier as assigned by the IRS to the individual or legal entity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
