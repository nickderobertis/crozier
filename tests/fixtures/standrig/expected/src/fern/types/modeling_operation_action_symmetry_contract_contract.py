

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_symmetry_contract_contract_axis import (
    ModelingOperationActionSymmetryContractContractAxis,
)
from .modeling_operation_action_symmetry_contract_contract_links_item import (
    ModelingOperationActionSymmetryContractContractLinksItem,
)


class ModelingOperationActionSymmetryContractContract(UniversalBaseModel):
    version: float
    axis: ModelingOperationActionSymmetryContractContractAxis
    axis_u: typing_extensions.Annotated[float, FieldMetadata(alias="axisU"), pydantic.Field(alias="axisU")]
    tolerance: float
    confidence: float
    protected_part_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="protectedPartIds"), pydantic.Field(alias="protectedPartIds")
    ]
    protected_deformer_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="protectedDeformerIds"), pydantic.Field(alias="protectedDeformerIds")
    ]
    protected_vertex_ids: typing_extensions.Annotated[
        typing.Dict[str, typing.List[str]],
        FieldMetadata(alias="protectedVertexIds"),
        pydantic.Field(alias="protectedVertexIds"),
    ]
    links: typing.List[ModelingOperationActionSymmetryContractContractLinksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
