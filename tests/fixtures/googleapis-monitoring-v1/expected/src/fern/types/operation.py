

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .status import Status


class Operation(UniversalBaseModel):
    """
    This resource represents a long-running operation that is the result of a network API call.
    """

    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the value is false, it means the operation is still in progress. If true, the operation is completed, and either error or response is available.
    """

    error: typing.Optional[Status] = pydantic.Field(default=None)
    """
    The error result of the operation in case of failure or cancellation.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the name should be a resource name ending with operations/{unique_id}.
    """

    response: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The normal, successful response of the operation. If the original method returns no data on success, such as Delete, the response is google.protobuf.Empty. If the original method is standard Get/Create/Update, the response should be the resource. For other methods, the response should have the type XxxResponse, where Xxx is the original method name. For example, if the original method name is TakeSnapshot(), the inferred response type is TakeSnapshotResponse.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
