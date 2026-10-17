

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrganizationProjectsResponseOutputPagination(UniversalBaseModel):
    count: float = pydantic.Field()
    """
    Total number of projects. Use this to calculate the total number of pages.
    """

    limit: float = pydantic.Field()
    """
    Maximum number of projects per page
    """

    offset: float = pydantic.Field()
    """
    Number of projects skipped in this response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
