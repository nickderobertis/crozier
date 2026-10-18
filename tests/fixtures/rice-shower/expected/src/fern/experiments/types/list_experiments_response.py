

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_experiments_response_experiments_item import ListExperimentsResponseExperimentsItem


class ListExperimentsResponse(UniversalBaseModel):
    total: float = pydantic.Field()
    """
    Total experiments matching the filter
    """

    experiments: typing.List[ListExperimentsResponseExperimentsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
