

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .another_person import AnotherPerson


class AnotherChild(AnotherPerson):
    """
    another child class that does NOT extend/inherit AnotherPerson
    """

    age: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
