

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .operation_metadata_state import OperationMetadataState


class OperationMetadata(UniversalBaseModel):
    """
    Contains metadata for longrunning operation for the edit Metrics Scope endpoints.
    """

    create_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createTime"),
        pydantic.Field(alias="createTime", description="The time when the batch request was received."),
    ] = None
    """
    The time when the batch request was received.
    """

    state: typing.Optional[OperationMetadataState] = pydantic.Field(default=None)
    """
    Current state of the batch operation.
    """

    update_time: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="updateTime"),
        pydantic.Field(alias="updateTime", description="The time when the operation result was last updated."),
    ] = None
    """
    The time when the operation result was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
