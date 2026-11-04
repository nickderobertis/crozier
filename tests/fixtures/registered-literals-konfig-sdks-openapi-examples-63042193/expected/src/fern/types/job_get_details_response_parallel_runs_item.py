

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobGetDetailsResponseParallelRunsItem(UniversalBaseModel):
    """
    Info about a status of the parallel run.
    """

    index: int = pydantic.Field()
    """
    Index of the parallel run.
    """

    status: str = pydantic.Field()
    """
    Status of the parallel run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
