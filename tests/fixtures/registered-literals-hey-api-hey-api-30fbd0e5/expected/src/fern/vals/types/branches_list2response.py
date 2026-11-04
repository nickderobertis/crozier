

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.branch import Branch
from ...types.pagination_links import PaginationLinks


class BranchesList2Response(UniversalBaseModel):
    """
    A paginated result set
    """

    data: typing.List[Branch]
    links: PaginationLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
