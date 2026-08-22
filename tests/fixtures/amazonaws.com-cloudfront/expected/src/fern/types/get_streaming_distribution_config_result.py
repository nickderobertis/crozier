

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_streaming_distribution_config_result_streaming_distribution_config import (
    GetStreamingDistributionConfigResultStreamingDistributionConfig,
)


class GetStreamingDistributionConfigResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    streaming_distribution_config: typing_extensions.Annotated[
        typing.Optional[GetStreamingDistributionConfigResultStreamingDistributionConfig],
        FieldMetadata(alias="StreamingDistributionConfig"),
        pydantic.Field(
            alias="StreamingDistributionConfig", description="The streaming distribution's configuration information."
        ),
    ] = None
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
