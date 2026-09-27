

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item_action_part_clip_clip_mask_opacity import (
    TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacity,
)
from .transaction_request_operations_operations_item_action_part_clip_clip_mode import (
    TransactionRequestOperationsOperationsItemActionPartClipClipMode,
)


class TransactionRequestOperationsOperationsItemActionPartClipClip(UniversalBaseModel):
    mode: TransactionRequestOperationsOperationsItemActionPartClipClipMode
    mask_part_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="maskPartId"), pydantic.Field(alias="maskPartId")
    ] = None
    mask_part_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="maskPartIds"), pydantic.Field(alias="maskPartIds")
    ] = None
    mask_opacity: typing_extensions.Annotated[
        typing.Optional[TransactionRequestOperationsOperationsItemActionPartClipClipMaskOpacity],
        FieldMetadata(alias="maskOpacity"),
        pydantic.Field(alias="maskOpacity"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
