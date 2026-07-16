

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_offer1data_offer_item import ObReadOffer1DataOfferItem


class ObReadOffer1Data(UniversalBaseModel):
    offer: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadOffer1DataOfferItem]], FieldMetadata(alias="Offer")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
