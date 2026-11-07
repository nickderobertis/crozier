

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .currency import Currency
from .hash256 import Hash256
from .siacoin_output import SiacoinOutput


class FileContractElementDiffRevision(UniversalBaseModel):
    filesize: int
    file_merkle_root: typing_extensions.Annotated[
        Hash256, FieldMetadata(alias="fileMerkleRoot"), pydantic.Field(alias="fileMerkleRoot")
    ]
    window_start: typing_extensions.Annotated[
        int, FieldMetadata(alias="windowStart"), pydantic.Field(alias="windowStart")
    ]
    window_end: typing_extensions.Annotated[int, FieldMetadata(alias="windowEnd"), pydantic.Field(alias="windowEnd")]
    payout: Currency
    valid_proof_outputs: typing_extensions.Annotated[
        typing.List[SiacoinOutput], FieldMetadata(alias="validProofOutputs"), pydantic.Field(alias="validProofOutputs")
    ]
    missed_proof_outputs: typing_extensions.Annotated[
        typing.List[SiacoinOutput],
        FieldMetadata(alias="missedProofOutputs"),
        pydantic.Field(alias="missedProofOutputs"),
    ]
    unlock_hash: typing_extensions.Annotated[
        Address, FieldMetadata(alias="unlockHash"), pydantic.Field(alias="unlockHash")
    ]
    revision_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="revisionNumber"), pydantic.Field(alias="revisionNumber")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
