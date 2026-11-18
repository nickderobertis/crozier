

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QueryRequestConditionsItem(UniversalBaseModel):
    source: str = pydantic.Field()
    """
    The source of the relation
    """

    target: str = pydantic.Field()
    """
    The target of the relation
    """

    relation: str = pydantic.Field()
    """
    The relationship of the condition
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
