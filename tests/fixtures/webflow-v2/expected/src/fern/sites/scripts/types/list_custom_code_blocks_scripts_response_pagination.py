

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCustomCodeBlocksScriptsResponsePagination(UniversalBaseModel):
    """
    Pagination object
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    The limit used for pagination
    """

    offset: typing.Optional[int] = pydantic.Field(default=None)
    """
    The offset used for pagination
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of records
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
