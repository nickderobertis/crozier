

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_distribution_config_result_distribution_config import GetDistributionConfigResultDistributionConfig


class GetDistributionConfigResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    distribution_config: typing_extensions.Annotated[
        typing.Optional[GetDistributionConfigResultDistributionConfig],
        FieldMetadata(alias="DistributionConfig"),
        pydantic.Field(alias="DistributionConfig", description="The distribution's configuration information."),
    ] = None
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
