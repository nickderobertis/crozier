

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dynamic_offer import DynamicOffer


class GetDynamicOffersResponse(UniversalBaseModel):
    dynamic_offers: typing_extensions.Annotated[
        typing.List[DynamicOffer],
        FieldMetadata(alias="dynamicOffers"),
        pydantic.Field(
            alias="dynamicOffers",
            description="Contains a list of available dynamic offers for the specified account holder.",
        ),
    ]
    """
    Contains a list of available dynamic offers for the specified account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
