

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_balance_transfers_response_embedded import ListBalanceTransfersResponseEmbedded


class ListBalanceTransfersResponse(UniversalBaseModel):
    embedded: typing_extensions.Annotated[
        typing.Optional[ListBalanceTransfersResponseEmbedded],
        FieldMetadata(alias="_embedded"),
        pydantic.Field(alias="_embedded"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
