

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transaction_request_operations_operations_item import TransactionRequestOperationsOperationsItem
from .transaction_request_operations_qa import TransactionRequestOperationsQa


class TransactionRequestOperations(UniversalBaseModel):
    expected_revision: typing_extensions.Annotated[
        str, FieldMetadata(alias="expectedRevision"), pydantic.Field(alias="expectedRevision")
    ]
    commit: bool
    operations: typing.List[TransactionRequestOperationsOperationsItem]
    qa: TransactionRequestOperationsQa

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
