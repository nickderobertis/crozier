

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .consensus_siacoin_input import ConsensusSiacoinInput
from .consensus_siacoin_output import ConsensusSiacoinOutput
from .currency import Currency
from .file_contract import FileContract
from .file_contract_revision import FileContractRevision
from .siafund_input import SiafundInput
from .siafund_output import SiafundOutput
from .storage_proof import StorageProof
from .transaction_id import TransactionId
from .transaction_signature import TransactionSignature


class ConsensusTransaction(UniversalBaseModel):
    """
    V1 transaction with origin information as returned by consensus block endpoints.
    """

    id: TransactionId
    siacoin_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[ConsensusSiacoinInput]],
        FieldMetadata(alias="siacoinInputs"),
        pydantic.Field(alias="siacoinInputs"),
    ] = None
    siacoin_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[ConsensusSiacoinOutput]],
        FieldMetadata(alias="siacoinOutputs"),
        pydantic.Field(alias="siacoinOutputs"),
    ] = None
    file_contracts: typing_extensions.Annotated[
        typing.Optional[typing.List[FileContract]],
        FieldMetadata(alias="fileContracts"),
        pydantic.Field(alias="fileContracts"),
    ] = None
    file_contract_revisions: typing_extensions.Annotated[
        typing.Optional[typing.List[FileContractRevision]],
        FieldMetadata(alias="fileContractRevisions"),
        pydantic.Field(alias="fileContractRevisions"),
    ] = None
    storage_proofs: typing_extensions.Annotated[
        typing.Optional[typing.List[StorageProof]],
        FieldMetadata(alias="storageProofs"),
        pydantic.Field(alias="storageProofs"),
    ] = None
    siafund_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiafundInput]],
        FieldMetadata(alias="siafundInputs"),
        pydantic.Field(alias="siafundInputs"),
    ] = None
    siafund_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiafundOutput]],
        FieldMetadata(alias="siafundOutputs"),
        pydantic.Field(alias="siafundOutputs"),
    ] = None
    miner_fees: typing_extensions.Annotated[
        typing.Optional[typing.List[Currency]], FieldMetadata(alias="minerFees"), pydantic.Field(alias="minerFees")
    ] = None
    arbitrary_data: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="arbitraryData"),
        pydantic.Field(alias="arbitraryData", description="Arbitrary data entries encoded as base64 strings."),
    ] = None
    """
    Arbitrary data entries encoded as base64 strings.
    """

    signatures: typing.Optional[typing.List[TransactionSignature]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
