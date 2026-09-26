

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Item(UniversalBaseModel):
    """
    Represents a single document or data entry in the graph's Store. Items are used to store cross-thread memories.
    """

    namespace: typing.List[str] = pydantic.Field()
    """
    The namespace of the item. A namespace is analogous to a document's directory.
    """

    key: str = pydantic.Field()
    """
    The unique identifier of the item within its namespace. In general, keys needn't be globally unique.
    """

    value: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    The value stored in the item. This is the document itself.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    The timestamp when the item was created.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The timestamp when the item was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
