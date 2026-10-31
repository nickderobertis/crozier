

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .child import Child
from .person import Person


class Adult(Person):
    """
    A representation of an adult
    """

    children: typing.Optional[typing.List[Child]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
