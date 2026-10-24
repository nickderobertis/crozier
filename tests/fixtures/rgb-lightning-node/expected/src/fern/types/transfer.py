

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assignment import Assignment
from .transfer_kind import TransferKind
from .transfer_status import TransferStatus
from .transfer_transport_endpoint import TransferTransportEndpoint


class Transfer(UniversalBaseModel):
    idx: int
    created_at: int
    updated_at: int
    status: TransferStatus
    requested_assignment: typing.Optional[Assignment] = None
    assignments: typing.List[Assignment]
    kind: TransferKind
    txid: typing.Optional[str] = None
    recipient_id: typing.Optional[str] = None
    receive_utxo: typing.Optional[str] = None
    change_utxo: typing.Optional[str] = None
    expiration_timestamp: typing.Optional[int] = None
    transport_endpoints: typing.List[TransferTransportEndpoint]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
