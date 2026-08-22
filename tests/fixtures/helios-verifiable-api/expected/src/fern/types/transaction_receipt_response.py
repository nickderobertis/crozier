

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bytes import Bytes
from .receipt_info import ReceiptInfo


class TransactionReceiptResponse(UniversalBaseModel):
    receipt: typing.Optional[ReceiptInfo] = None
    receipt_proof: typing_extensions.Annotated[
        typing.Optional[typing.List[Bytes]], FieldMetadata(alias="receiptProof"), pydantic.Field(alias="receiptProof")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
