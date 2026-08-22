

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_distribution_with_tags_request_distribution_config_with_tags import (
    CreateDistributionWithTagsRequestDistributionConfigWithTags,
)


class CreateDistributionWithTagsRequest(UniversalBaseModel):
    """
    The request to create a new distribution with tags.
    """

    distribution_config_with_tags: typing_extensions.Annotated[
        CreateDistributionWithTagsRequestDistributionConfigWithTags,
        FieldMetadata(alias="DistributionConfigWithTags"),
        pydantic.Field(
            alias="DistributionConfigWithTags", description="The distribution's configuration information. "
        ),
    ]
    """
    The distribution's configuration information. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
