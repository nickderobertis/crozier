

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_deformer_targets_set_mode import (
    TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode,
)


class TransactionRequestOperationsOperationsItemActionDeformerTargetsSet(UniversalBaseModel):
    deformer_id: typing_extensions.Annotated[str, FieldMetadata(alias="deformerId"), pydantic.Field(alias="deformerId")]
    target_part_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="targetPartIds"), pydantic.Field(alias="targetPartIds")
    ]
    mode: typing.Optional[TransactionRequestOperationsOperationsItemActionDeformerTargetsSetMode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
