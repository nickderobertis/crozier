

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .create_distribution_request_distribution_config import CreateDistributionRequestDistributionConfig


class CreateDistributionRequest(UniversalBaseModel):
    """
    The request to create a new distribution.
    """

    distribution_config: typing_extensions.Annotated[
        CreateDistributionRequestDistributionConfig,
        FieldMetadata(alias="DistributionConfig"),
        pydantic.Field(alias="DistributionConfig", description="The distribution's configuration information."),
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
