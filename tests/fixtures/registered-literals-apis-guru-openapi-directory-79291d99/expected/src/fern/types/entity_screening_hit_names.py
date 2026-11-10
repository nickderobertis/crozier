

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weak_alias_determination import WeakAliasDetermination


class EntityScreeningHitNames(UniversalBaseModel):
    """
    Name information for the associated entity watchlist hit
    """

    full: str = pydantic.Field()
    """
    The full name of the entity.
    """

    is_primary: bool = pydantic.Field()
    """
    Primary names are those most commonly used to refer to this entity. Only one name will ever be marked as primary.
    """

    weak_alias_determination: WeakAliasDetermination

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
