

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .attestation import Attestation
from .consensus_siacoin_output import ConsensusSiacoinOutput
from .consensus_v2siacoin_input import ConsensusV2SiacoinInput
from .currency import Currency
from .siafund_output import SiafundOutput
from .transaction_id import TransactionId
from .v2file_contract import V2FileContract
from .v2file_contract_resolution import V2FileContractResolution
from .v2file_contract_revision import V2FileContractRevision
from .v2siafund_input import V2SiafundInput


class ConsensusV2Transaction(UniversalBaseModel):
    """
    V2 transaction with origin information as returned by consensus block endpoints.
    """

    id: TransactionId
    siacoin_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[ConsensusV2SiacoinInput]],
        FieldMetadata(alias="siacoinInputs"),
        pydantic.Field(alias="siacoinInputs"),
    ] = None
    siacoin_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[ConsensusSiacoinOutput]],
        FieldMetadata(alias="siacoinOutputs"),
        pydantic.Field(alias="siacoinOutputs"),
    ] = None
    siafund_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[V2SiafundInput]],
        FieldMetadata(alias="siafundInputs"),
        pydantic.Field(alias="siafundInputs"),
    ] = None
    siafund_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiafundOutput]],
        FieldMetadata(alias="siafundOutputs"),
        pydantic.Field(alias="siafundOutputs"),
    ] = None
    file_contracts: typing_extensions.Annotated[
        typing.Optional[typing.List[V2FileContract]],
        FieldMetadata(alias="fileContracts"),
        pydantic.Field(alias="fileContracts"),
    ] = None
    file_contract_revisions: typing_extensions.Annotated[
        typing.Optional[typing.List[V2FileContractRevision]],
        FieldMetadata(alias="fileContractRevisions"),
        pydantic.Field(alias="fileContractRevisions"),
    ] = None
    file_contract_resolutions: typing_extensions.Annotated[
        typing.Optional[typing.List[V2FileContractResolution]],
        FieldMetadata(alias="fileContractResolutions"),
        pydantic.Field(alias="fileContractResolutions"),
    ] = None
    attestations: typing.Optional[typing.List[Attestation]] = None
    arbitrary_data: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="arbitraryData"),
        pydantic.Field(alias="arbitraryData", description="Arbitrary data encoded as a base64 string."),
    ] = None
    """
    Arbitrary data encoded as a base64 string.
    """

    new_foundation_address: typing_extensions.Annotated[
        typing.Optional[Address],
        FieldMetadata(alias="newFoundationAddress"),
        pydantic.Field(alias="newFoundationAddress"),
    ] = None
    miner_fee: typing_extensions.Annotated[
        typing.Optional[Currency], FieldMetadata(alias="minerFee"), pydantic.Field(alias="minerFee")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
