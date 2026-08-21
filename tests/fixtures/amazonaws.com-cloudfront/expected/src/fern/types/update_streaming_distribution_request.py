

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_streaming_distribution_request_streaming_distribution_config import (
    UpdateStreamingDistributionRequestStreamingDistributionConfig,
)


class UpdateStreamingDistributionRequest(UniversalBaseModel):
    """
    The request to update a streaming distribution.
    """

    streaming_distribution_config: typing_extensions.Annotated[
        UpdateStreamingDistributionRequestStreamingDistributionConfig,
        FieldMetadata(alias="StreamingDistributionConfig"),
        pydantic.Field(
            alias="StreamingDistributionConfig", description="The streaming distribution's configuration information."
        ),
    ]
    """
    The streaming distribution's configuration information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
