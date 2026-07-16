

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_normalization_status_read import AttemptNormalizationStatusRead


class AttemptNormalizationStatusReadList(UniversalBaseModel):
    attempt_normalization_statuses: typing_extensions.Annotated[
        typing.Optional[typing.List[AttemptNormalizationStatusRead]],
        FieldMetadata(alias="attemptNormalizationStatuses"),
        pydantic.Field(alias="attemptNormalizationStatuses"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
