

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .timestamp import Timestamp


class InvalidationSummaryListItem(UniversalBaseModel):
    """
    A summary of an invalidation request.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The unique ID for an invalidation request."),
    ]
    """
    The unique ID for an invalidation request.
    """

    create_time: typing_extensions.Annotated[
        Timestamp, FieldMetadata(alias="CreateTime"), pydantic.Field(alias="CreateTime")
    ]
    status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="The status of an invalidation request."),
    ]
    """
    The status of an invalidation request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
