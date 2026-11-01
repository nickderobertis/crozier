

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .person_a_explicit_parent import PersonAExplicitParent
from .person_b import PersonB


class SchemaWithTwoAllOfRefsOneIsMarkedAsParent(PersonAExplicitParent, PersonB):
    """
    A schema that has two allOfs with refs, but one of the allOfs is explicitly marked with x-parent
    """

    age: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
