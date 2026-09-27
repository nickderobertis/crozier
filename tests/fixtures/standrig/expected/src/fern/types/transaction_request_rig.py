

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .qa_check_request import QaCheckRequest
from .transaction_request_rig_kind import TransactionRequestRigKind


class TransactionRequestRig(UniversalBaseModel):
    kind: TransactionRequestRigKind
    expected_revision: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]
    commit: typing.Optional[bool] = None
    rig: typing.Dict[str, typing.Any]
    qa: QaCheckRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
