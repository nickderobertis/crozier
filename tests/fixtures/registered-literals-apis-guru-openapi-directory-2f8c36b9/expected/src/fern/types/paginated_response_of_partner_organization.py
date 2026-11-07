

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .partner_organization import PartnerOrganization


class PaginatedResponseOfPartnerOrganization(UniversalBaseModel):
    elements: typing.List[PartnerOrganization]
    limit: int = pydantic.Field()
    """
    The number of returned elements
    """

    offset: int = pydantic.Field()
    """
    Starting with the n-th element
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of elements
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
