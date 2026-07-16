

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListWorkweekConfigsRequest(UniversalBaseModel):
    """
    A request for a set of `WorkweekConfig` objects.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pointer to the next page of `WorkweekConfig` results to fetch.
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of `WorkweekConfigs` results to return per page.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
