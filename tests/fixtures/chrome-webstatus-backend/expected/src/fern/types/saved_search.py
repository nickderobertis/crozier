

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SavedSearch(UniversalBaseModel):
    """
    Represents a saved search with a name and a query.
    Both `name` and `query` are required when creating a new saved search.
    """

    name: str
    description: typing.Optional[str] = None
    query: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
