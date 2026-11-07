

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attestation_element import AttestationElement
from .chain_index_element import ChainIndexElement
from .file_contract_element_diff import FileContractElementDiff
from .hash256 import Hash256
from .siacoin_element_diff import SiacoinElementDiff
from .siafund_element_diff import SiafundElementDiff
from .state_element import StateElement
from .v2file_contract_element_diff import V2FileContractElementDiff


class ApplyUpdateData(UniversalBaseModel):
    siacoin_elements: typing_extensions.Annotated[
        typing.List[SiacoinElementDiff], FieldMetadata(alias="siacoinElements"), pydantic.Field(alias="siacoinElements")
    ]
    siafund_element_diffs: typing_extensions.Annotated[
        typing.List[SiafundElementDiff],
        FieldMetadata(alias="siafundElementDiffs"),
        pydantic.Field(alias="siafundElementDiffs"),
    ]
    file_contract_element_diffs: typing_extensions.Annotated[
        typing.List[FileContractElementDiff],
        FieldMetadata(alias="fileContractElementDiffs"),
        pydantic.Field(alias="fileContractElementDiffs"),
    ]
    v2file_contract_element_diffs: typing_extensions.Annotated[
        typing.List[V2FileContractElementDiff],
        FieldMetadata(alias="v2FileContractElementDiffs"),
        pydantic.Field(alias="v2FileContractElementDiffs"),
    ]
    attestation_elements: typing_extensions.Annotated[
        typing.List[AttestationElement],
        FieldMetadata(alias="attestationElements"),
        pydantic.Field(alias="attestationElements"),
    ]
    chain_index_element: typing_extensions.Annotated[
        ChainIndexElement, FieldMetadata(alias="chainIndexElement"), pydantic.Field(alias="chainIndexElement")
    ]
    updated_leaves: typing_extensions.Annotated[
        typing.Dict[str, typing.List[StateElement]],
        FieldMetadata(alias="updatedLeaves"),
        pydantic.Field(alias="updatedLeaves"),
    ]
    tree_growth: typing_extensions.Annotated[
        typing.Dict[str, typing.List[Hash256]], FieldMetadata(alias="treeGrowth"), pydantic.Field(alias="treeGrowth")
    ]
    old_num_leaves: typing_extensions.Annotated[
        int, FieldMetadata(alias="oldNumLeaves"), pydantic.Field(alias="oldNumLeaves")
    ]
    num_leaves: typing_extensions.Annotated[int, FieldMetadata(alias="numLeaves"), pydantic.Field(alias="numLeaves")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
