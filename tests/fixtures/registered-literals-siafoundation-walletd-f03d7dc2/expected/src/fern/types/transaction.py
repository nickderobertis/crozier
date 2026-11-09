

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .currency import Currency
from .file_contract import FileContract
from .file_contract_revision import FileContractRevision
from .siacoin_input import SiacoinInput
from .siacoin_output_with_id import SiacoinOutputWithId
from .siafund_input import SiafundInput
from .siafund_output_with_id import SiafundOutputWithId
from .storage_proof import StorageProof
from .transaction_id import TransactionId
from .transaction_signature import TransactionSignature


class Transaction(UniversalBaseModel):
    """
    Sia v1 transaction including derived identifiers returned by walletd.
    """

    id: TransactionId
    siacoin_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiacoinInput]],
        FieldMetadata(alias="siacoinInputs"),
        pydantic.Field(alias="siacoinInputs"),
    ] = None
    siacoin_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiacoinOutputWithId]],
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
        typing.Optional[typing.List[SiafundOutputWithId]],
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
