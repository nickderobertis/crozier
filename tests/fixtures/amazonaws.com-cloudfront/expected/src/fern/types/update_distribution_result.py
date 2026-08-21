

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .update_distribution_result_distribution import UpdateDistributionResultDistribution


class UpdateDistributionResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    distribution: typing_extensions.Annotated[
        typing.Optional[UpdateDistributionResultDistribution],
        FieldMetadata(alias="Distribution"),
        pydantic.Field(alias="Distribution", description="The distribution's information."),
    ] = None
    """
    The distribution's information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
