

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .inclusion_proof import InclusionProof


class LogEntryValueVerification(UniversalBaseModel):
    inclusion_proof: typing_extensions.Annotated[
        typing.Optional[InclusionProof], FieldMetadata(alias="inclusionProof"), pydantic.Field(alias="inclusionProof")
    ] = None
    signed_entry_timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signedEntryTimestamp"),
        pydantic.Field(
            alias="signedEntryTimestamp", description="Signature over the logID, logIndex, body and integratedTime."
        ),
    ] = None
    """
    Signature over the logID, logIndex, body and integratedTime.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
