

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .page import Page
from .relation import Relation


class ResponsePageRelationData(Page):
    items: typing.Optional[typing.List[Relation]] = pydantic.Field(default=None)
    """
    Items in the current page of results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
