

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_number import AttemptNumber


class AttemptNormalizationStatusRead(UniversalBaseModel):
    attempt_number: typing_extensions.Annotated[
        typing.Optional[AttemptNumber], FieldMetadata(alias="attemptNumber")
    ] = None
    has_normalization_failed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasNormalizationFailed")
    ] = None
    has_records_committed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasRecordsCommitted")
    ] = None
    records_committed: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="recordsCommitted")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
