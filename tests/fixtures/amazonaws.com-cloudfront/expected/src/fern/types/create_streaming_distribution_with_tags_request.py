

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_streaming_distribution_with_tags_request_streaming_distribution_config_with_tags import (
    CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags,
)


class CreateStreamingDistributionWithTagsRequest(UniversalBaseModel):
    """
    The request to create a new streaming distribution with tags.
    """

    streaming_distribution_config_with_tags: typing_extensions.Annotated[
        CreateStreamingDistributionWithTagsRequestStreamingDistributionConfigWithTags,
        FieldMetadata(alias="StreamingDistributionConfigWithTags"),
        pydantic.Field(
            alias="StreamingDistributionConfigWithTags",
            description=" The streaming distribution's configuration information. ",
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
