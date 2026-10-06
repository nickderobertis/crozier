

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .query_input import QueryInput


class QueryUpdateInput(UniversalBaseModel):
    """
    Input data to update a query definition.
    """

    meta: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    User metadata for the query definition.
    """

    query: typing.Optional[QueryInput] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
