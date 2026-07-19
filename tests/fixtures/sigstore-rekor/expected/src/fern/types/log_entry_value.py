

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .log_entry_value_attestation import LogEntryValueAttestation
from .log_entry_value_verification import LogEntryValueVerification


class LogEntryValue(UniversalBaseModel):
    attestation: typing.Optional[LogEntryValueAttestation] = None
    body: str
    integrated_time: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="integratedTime"),
        pydantic.Field(
            alias="integratedTime", description="The time the entry was added to the log as a Unix timestamp in seconds"
        ),
    ]
    """
    The time the entry was added to the log as a Unix timestamp in seconds
    """

    log_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="logID"),
        pydantic.Field(
            alias="logID",
            description="This is the SHA256 hash of the DER-encoded public key for the log at the time the entry was included in the log",
        ),
    ]
    """
    This is the SHA256 hash of the DER-encoded public key for the log at the time the entry was included in the log
    """

    log_index: typing_extensions.Annotated[int, FieldMetadata(alias="logIndex"), pydantic.Field(alias="logIndex")]
    verification: typing.Optional[LogEntryValueVerification] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
