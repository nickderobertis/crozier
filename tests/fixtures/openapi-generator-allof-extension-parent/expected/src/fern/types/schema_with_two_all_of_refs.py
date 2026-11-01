

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .person_a import PersonA
from .person_b import PersonB


class SchemaWithTwoAllOfRefs(PersonA, PersonB):
    """
    A schema that has two allOfs with refs
    """

    age: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
