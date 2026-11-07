

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency
from .hash256 import Hash256
from .public_key import PublicKey
from .siacoin_output import SiacoinOutput
from .signature import Signature


class V2FileContractElementDiffRevision(UniversalBaseModel):
    capacity: int
    filesize: int
    file_merkle_root: typing_extensions.Annotated[
        Hash256, FieldMetadata(alias="fileMerkleRoot"), pydantic.Field(alias="fileMerkleRoot")
    ]
    proof_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="proofHeight"), pydantic.Field(alias="proofHeight")
    ]
    expiration_height: typing_extensions.Annotated[
        int, FieldMetadata(alias="expirationHeight"), pydantic.Field(alias="expirationHeight")
    ]
    renter_output: typing_extensions.Annotated[
        SiacoinOutput, FieldMetadata(alias="renterOutput"), pydantic.Field(alias="renterOutput")
    ]
    host_output: typing_extensions.Annotated[
        SiacoinOutput, FieldMetadata(alias="hostOutput"), pydantic.Field(alias="hostOutput")
    ]
    missed_host_value: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="missedHostValue"), pydantic.Field(alias="missedHostValue")
    ]
    total_collateral: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="totalCollateral"), pydantic.Field(alias="totalCollateral")
    ]
    renter_public_key: typing_extensions.Annotated[
        PublicKey, FieldMetadata(alias="renterPublicKey"), pydantic.Field(alias="renterPublicKey")
    ]
    host_public_key: typing_extensions.Annotated[
        PublicKey, FieldMetadata(alias="hostPublicKey"), pydantic.Field(alias="hostPublicKey")
    ]
    revision_number: typing_extensions.Annotated[
        int, FieldMetadata(alias="revisionNumber"), pydantic.Field(alias="revisionNumber")
    ]
    renter_signature: typing_extensions.Annotated[
        Signature, FieldMetadata(alias="renterSignature"), pydantic.Field(alias="renterSignature")
    ]
    host_signature: typing_extensions.Annotated[
        Signature, FieldMetadata(alias="hostSignature"), pydantic.Field(alias="hostSignature")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
