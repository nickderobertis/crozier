

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_meta_pagination import ListMetaPagination


class ListMeta(UniversalBaseModel):
    pagination: typing.Optional[ListMetaPagination] = pydantic.Field(default=None)
    """
    Page-based responses include page/pageSize/pageCount/total; offset-based include start/limit/total.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
