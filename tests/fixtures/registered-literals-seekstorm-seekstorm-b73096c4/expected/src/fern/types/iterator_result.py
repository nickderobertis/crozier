

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .iterator_result_item import IteratorResultItem


class IteratorResult(UniversalBaseModel):
    """
    Iterator
    """

    skip: int = pydantic.Field()
    """
    number of actually skipped documents
    """

    results: typing.List[IteratorResultItem] = pydantic.Field()
    """
    document IDs, and optionally the documents themselves
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
