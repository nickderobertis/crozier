

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount


class GrantOfferFee(UniversalBaseModel):
    amount: Amount = pydantic.Field()
    """
    Contains the amount of the offer fee.
    """

    apr_basis_points: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="aprBasisPoints"),
        pydantic.Field(
            alias="aprBasisPoints",
            description="Annual Percentage Rate (APR) of the offer. The percentage is expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).",
        ),
    ] = None
    """
    Annual Percentage Rate (APR) of the offer. The percentage is expressed in [basis points](https://www.investopedia.com/terms/b/basispoint.asp).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
