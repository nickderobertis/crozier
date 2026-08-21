

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_streaming_distribution_result_streaming_distribution import (
    CreateStreamingDistributionResultStreamingDistribution,
)


class CreateStreamingDistributionResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    streaming_distribution: typing_extensions.Annotated[
        typing.Optional[CreateStreamingDistributionResultStreamingDistribution],
        FieldMetadata(alias="StreamingDistribution"),
        pydantic.Field(alias="StreamingDistribution", description="The streaming distribution's information."),
    ] = None
    """
    The streaming distribution's information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
