

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_streaming_distribution_config import (
    CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfig,
)
from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags_tags import (
    CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTags,
)


class CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags(UniversalBaseModel):
    """
    The streaming distribution's configuration information.
    """

    streaming_distribution_config: typing_extensions.Annotated[
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsStreamingDistributionConfig,
        FieldMetadata(alias="StreamingDistributionConfig"),
        pydantic.Field(alias="StreamingDistributionConfig", description="A streaming distribution Configuration."),
    ]
    """
    A streaming distribution Configuration.
    """

    tags: typing_extensions.Annotated[
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTagsTags,
        FieldMetadata(alias="Tags"),
        pydantic.Field(
            alias="Tags", description="A complex type that contains zero or more <code>Tag</code> elements."
        ),
    ]
    """
    A complex type that contains zero or more <code>Tag</code> elements.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
