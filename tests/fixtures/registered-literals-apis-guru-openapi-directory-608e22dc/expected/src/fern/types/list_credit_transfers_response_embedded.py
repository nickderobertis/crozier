

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transfer_credit_response import TransferCreditResponse


class ListCreditTransfersResponseEmbedded(UniversalBaseModel):
    credit_transfers: typing_extensions.Annotated[
        typing.Optional[typing.List[TransferCreditResponse]],
        FieldMetadata(alias="credit-transfers"),
        pydantic.Field(alias="credit-transfers"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
