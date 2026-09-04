

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .grant_offer import GrantOffer


class GrantOffers(UniversalBaseModel):
    grant_offers: typing_extensions.Annotated[
        typing.List[GrantOffer],
        FieldMetadata(alias="grantOffers"),
        pydantic.Field(
            alias="grantOffers", description="Contains a list of available offers for the specified account holder."
        ),
    ]
    """
    Contains a list of available offers for the specified account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
