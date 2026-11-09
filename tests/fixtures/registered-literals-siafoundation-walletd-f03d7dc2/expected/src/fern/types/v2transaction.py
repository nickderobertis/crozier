

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attestation import Attestation
from .currency import Currency
from .siacoin_output_with_id import SiacoinOutputWithId
from .siafund_output_with_id import SiafundOutputWithId
from .transaction_id import TransactionId
from .v2file_contract import V2FileContract
from .v2file_contract_resolution import V2FileContractResolution
from .v2file_contract_revision import V2FileContractRevision
from .v2siacoin_input import V2SiacoinInput
from .v2siafund_input import V2SiafundInput


class V2Transaction(UniversalBaseModel):
    """
    Sia v2 transaction including derived identifiers returned by walletd.
    """

    id: TransactionId
    miner_fee: typing_extensions.Annotated[Currency, FieldMetadata(alias="minerFee"), pydantic.Field(alias="minerFee")]
    siacoin_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[V2SiacoinInput]],
        FieldMetadata(alias="siacoinInputs"),
        pydantic.Field(alias="siacoinInputs"),
    ] = None
    siacoin_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiacoinOutputWithId]],
        FieldMetadata(alias="siacoinOutputs"),
        pydantic.Field(alias="siacoinOutputs"),
    ] = None
    siafund_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[V2SiafundInput]],
        FieldMetadata(alias="siafundInputs"),
        pydantic.Field(alias="siafundInputs"),
    ] = None
    siafund_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[SiafundOutputWithId]],
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
        pydantic.Field(alias="arbitraryData", description="Arbitrary payload encoded as base64."),
    ] = None
    """
    Arbitrary payload encoded as base64.
    """

    new_foundation_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="newFoundationAddress"),
        pydantic.Field(alias="newFoundationAddress", description="The hash of a set of UnlockConditions"),
    ] = None
    """
    The hash of a set of UnlockConditions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
