

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_distribution_with_tags_request_distribution_config_with_tags_distribution_config import (
    CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfig,
)
from .create_distribution_with_tags_request_distribution_config_with_tags_tags import (
    CreateDistributionWithTagsRequestDistributionConfigWithTagsTags,
)


class CreateDistributionWithTagsRequestDistributionConfigWithTags(UniversalBaseModel):
    """
    The distribution's configuration information.
    """

    distribution_config: typing_extensions.Annotated[
        CreateDistributionWithTagsRequestDistributionConfigWithTagsDistributionConfig,
        FieldMetadata(alias="DistributionConfig"),
        pydantic.Field(alias="DistributionConfig", description="A distribution configuration."),
    ]
    """
    A distribution configuration.
    """

    tags: typing_extensions.Annotated[
        CreateDistributionWithTagsRequestDistributionConfigWithTagsTags,
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
