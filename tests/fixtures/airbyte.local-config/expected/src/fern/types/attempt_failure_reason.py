

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attempt_failure_origin import AttemptFailureOrigin
from .attempt_failure_type import AttemptFailureType


class AttemptFailureReason(UniversalBaseModel):
    external_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="externalMessage")] = None
    failure_origin: typing_extensions.Annotated[
        typing.Optional[AttemptFailureOrigin], FieldMetadata(alias="failureOrigin")
    ] = None
    failure_type: typing_extensions.Annotated[
        typing.Optional[AttemptFailureType], FieldMetadata(alias="failureType")
    ] = None
    internal_message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="internalMessage")] = None
    retryable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if it is known that retrying may succeed, e.g. for a transient failure. False if it is known that a retry will not succeed, e.g. for a configuration issue. If not set, retryable status is not well known.
    """

    stacktrace: typing.Optional[str] = None
    timestamp: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
