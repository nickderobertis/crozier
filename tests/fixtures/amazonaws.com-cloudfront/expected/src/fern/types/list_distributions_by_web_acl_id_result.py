

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .list_distributions_by_web_acl_id_result_distribution_list import ListDistributionsByWebAclIdResultDistributionList


class ListDistributionsByWebAclIdResult(UniversalBaseModel):
    """
    The response to a request to list the distributions that are associated with a specified AWS WAF web ACL.
    """

    distribution_list: typing_extensions.Annotated[
        typing.Optional[ListDistributionsByWebAclIdResultDistributionList],
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
