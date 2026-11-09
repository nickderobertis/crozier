

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CoveredFields(UniversalBaseModel):
    whole_transaction: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="wholeTransaction"), pydantic.Field(alias="wholeTransaction")
    ] = None
    siacoin_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="siacoinInputs"), pydantic.Field(alias="siacoinInputs")
    ] = None
    siacoin_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="siacoinOutputs"), pydantic.Field(alias="siacoinOutputs")
    ] = None
    file_contracts: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="fileContracts"), pydantic.Field(alias="fileContracts")
    ] = None
    file_contract_revisions: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="fileContractRevisions"),
        pydantic.Field(alias="fileContractRevisions"),
    ] = None
    storage_proofs: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="storageProofs"), pydantic.Field(alias="storageProofs")
    ] = None
    siafund_inputs: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="siafundInputs"), pydantic.Field(alias="siafundInputs")
    ] = None
    siafund_outputs: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="siafundOutputs"), pydantic.Field(alias="siafundOutputs")
    ] = None
    miner_fees: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="minerFees"), pydantic.Field(alias="minerFees")
    ] = None
    arbitrary_data: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="arbitraryData"), pydantic.Field(alias="arbitraryData")
    ] = None
    signatures: typing.Optional[typing.List[int]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
