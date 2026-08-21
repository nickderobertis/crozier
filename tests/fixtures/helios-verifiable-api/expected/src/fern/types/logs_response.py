

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .log import Log
from .receipt_proofs_map import ReceiptProofsMap


class LogsResponse(UniversalBaseModel):
    logs: typing.Optional[typing.List[Log]] = None
    receipt_proofs: typing_extensions.Annotated[
        typing.Optional[ReceiptProofsMap], FieldMetadata(alias="receiptProofs"), pydantic.Field(alias="receiptProofs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
