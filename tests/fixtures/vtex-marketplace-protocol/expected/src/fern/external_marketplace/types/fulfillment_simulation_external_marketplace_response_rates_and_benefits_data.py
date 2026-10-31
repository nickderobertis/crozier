

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class FulfillmentSimulationExternalMarketplaceResponseRatesAndBenefitsData(UniversalBaseModel):
    """
    Information on rates and benefits that apply to the order.
    """

    rate_and_benefits_identifiers: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]],
        FieldMetadata(alias="rateAndBenefitsIdentifiers"),
        pydantic.Field(alias="rateAndBenefitsIdentifiers", description="List with rates and benefits identifiers."),
    ] = None
    """
    List with rates and benefits identifiers.
    """

    teaser: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    List with rates and benefits teasers.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
