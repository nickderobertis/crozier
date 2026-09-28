

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_checkpoint_id_kind import TransactionRequestCheckpointIdKind


class TransactionRequestCheckpointId(UniversalBaseModel):
    kind: TransactionRequestCheckpointIdKind
    expected_revision: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]
    commit: typing.Optional[bool] = None
    checkpoint_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="checkpointId"), pydantic.Field(alias="checkpointId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
