

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .invalidation_invalidation_batch import InvalidationInvalidationBatch


class Invalidation(UniversalBaseModel):
    """
    An invalidation.
    """

    id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Id"),
        pydantic.Field(
            alias="Id",
            description="The identifier for the invalidation request. For example: <code>IDFDVBD632BHDS5</code>.",
        ),
    ]
    """
    The identifier for the invalidation request. For example: <code>IDFDVBD632BHDS5</code>.
    """

    status: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="Status"),
        pydantic.Field(
            alias="Status",
            description="The status of the invalidation request. When the invalidation batch is finished, the status is <code>Completed</code>.",
        ),
    ]
    """
    The status of the invalidation request. When the invalidation batch is finished, the status is <code>Completed</code>.
    """

    create_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="CreateTime"),
        pydantic.Field(alias="CreateTime", description="The date and time the invalidation request was first made. "),
    ]
    """
    The date and time the invalidation request was first made. 
    """

    invalidation_batch: typing_extensions.Annotated[
        InvalidationInvalidationBatch,
        FieldMetadata(alias="InvalidationBatch"),
        pydantic.Field(
            alias="InvalidationBatch", description="The current invalidation information for the batch request. "
        ),
    ]
    """
    The current invalidation information for the batch request. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
