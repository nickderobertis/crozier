

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_distributions_result_distribution_list import ListDistributionsResultDistributionList


class ListDistributionsResult(UniversalBaseModel):
    """
    The returned result of the corresponding request.
    """

    distribution_list: typing_extensions.Annotated[
        typing.Optional[ListDistributionsResultDistributionList],
        FieldMetadata(alias="DistributionList"),
        pydantic.Field(alias="DistributionList", description="The <code>DistributionList</code> type. "),
    ] = None
    """
    The <code>DistributionList</code> type. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
