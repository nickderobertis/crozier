

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_failure_reason import AttemptFailureReason


class AttemptFailureSummary(UniversalBaseModel):
    failures: typing.List[AttemptFailureReason]
    partial_success: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="partialSuccess"),
        pydantic.Field(
            alias="partialSuccess",
            description="True if the number of committed records for this attempt was greater than 0. False if 0 records were committed. If not set, the number of committed records is unknown.",
        ),
    ] = None
    """
    True if the number of committed records for this attempt was greater than 0. False if 0 records were committed. If not set, the number of committed records is unknown.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
