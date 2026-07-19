

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .uuid_ import Uuid


class CollectionItem(UniversalBaseModel):
    """
    Describes how an entity (Source or Flow) is collected into another entity of the same type
    """

    id: Uuid = pydantic.Field()
    """
    Source or Flow Identifier of the member of this collection. Sources MUST only collect Sources, and Flows MUST only collect Flows. Must already be registered in this service instance
    """

    role: str = pydantic.Field()
    """
    A human-readable role of the element in this collection (e.g. 'R' to denote a right audio channel in a collection of mono audio Sources)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
