

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FindObject(UniversalBaseModel):
    """
    The fields and values used to search.
    """

    query: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The search criteria (MongoDB-filter syntax)
    """

    projection: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The fields to include in the response
    """

    after: typing.Optional[str] = pydantic.Field(default=None)
    """
    The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
