

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MonsterSenses(UniversalBaseModel):
    blindsight: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster with blindsight can perceive its surroundings without relying on sight, within a specific radius.
    """

    darkvision: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster with darkvision can see in the dark within a specific radius.
    """

    passive_perception: typing.Optional[float] = pydantic.Field(default=None)
    """
    The monster's passive perception (wisdom) score.
    """

    tremorsense: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster with tremorsense can detect and pinpoint the origin of vibrations within a specific radius, provided that the monster and the source of the vibrations are in contact with the same ground or substance.
    """

    truesight: typing.Optional[str] = pydantic.Field(default=None)
    """
    A monster with truesight can, out to a specific range, see in normal and magical darkness, see invisible creatures and objects, automatically detect visual illusions and succeed on saving throws against them, and perceive the original form of a shapechanger or a creature that is transformed by magic. Furthermore, the monster can see into the Ethereal Plane within the same range.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
