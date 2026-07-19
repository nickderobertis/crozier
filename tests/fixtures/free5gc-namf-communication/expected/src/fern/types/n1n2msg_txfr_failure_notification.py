

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n1n2message_transfer_cause import N1N2MessageTransferCause


class N1N2MsgTxfrFailureNotification(UniversalBaseModel):
    cause: N1N2MessageTransferCause
    n1n2msg_data_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="n1n2MsgDataUri"), pydantic.Field(alias="n1n2MsgDataUri")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
