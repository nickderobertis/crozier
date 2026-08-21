

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_streaming_distributions_result_streaming_distribution_list import (
    ListStreamingDistributionsResultStreamingDistributionList,
)


class ListStreamingDistributionsResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    streaming_distribution_list: typing_extensions.Annotated[
        typing.Optional[ListStreamingDistributionsResultStreamingDistributionList],
        FieldMetadata(alias="StreamingDistributionList"),
        pydantic.Field(
            alias="StreamingDistributionList", description="The <code>StreamingDistributionList</code> type. "
        ),
    ] = None
    """
    The <code>StreamingDistributionList</code> type. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
