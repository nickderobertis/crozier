

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .modeling_operation_action_symmetry_contract_contract_links_item_axis import (
    ModelingOperationActionSymmetryContractContractLinksItemAxis,
)
from .modeling_operation_action_symmetry_contract_contract_links_item_kind import (
    ModelingOperationActionSymmetryContractContractLinksItemKind,
)


class ModelingOperationActionSymmetryContractContractLinksItem(UniversalBaseModel):
    kind: ModelingOperationActionSymmetryContractContractLinksItemKind
    source_id: typing_extensions.Annotated[str, FieldMetadata(alias="sourceId"), pydantic.Field(alias="sourceId")]
    target_id: typing_extensions.Annotated[str, FieldMetadata(alias="targetId"), pydantic.Field(alias="targetId")]
    axis: ModelingOperationActionSymmetryContractContractLinksItemAxis
    invert_x: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="invertX"), pydantic.Field(alias="invertX")
    ] = None
    preserve_y: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="preserveY"), pydantic.Field(alias="preserveY")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
