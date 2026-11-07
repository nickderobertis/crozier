

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cancel_async_search_dto_current_search_job_status import CancelAsyncSearchDtoCurrentSearchJobStatus


class CancelAsyncSearchDto(UniversalBaseModel):
    is_cancelled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isCancelled"),
        pydantic.Field(alias="isCancelled", description="Whether the cancellation was successful"),
    ]
    """
    Whether the cancellation was successful
    """

    current_search_job_status: typing_extensions.Annotated[
        CancelAsyncSearchDtoCurrentSearchJobStatus,
        FieldMetadata(alias="currentSearchJobStatus"),
        pydantic.Field(alias="currentSearchJobStatus"),
    ]
    cancelled: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
