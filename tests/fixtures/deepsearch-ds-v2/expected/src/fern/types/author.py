

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .affiliation import Affiliation


class Author(UniversalBaseModel):
    """
    Author.
    """

    name: str
    id: typing.Optional[str] = None
    source: typing.Optional[str] = None
    affiliations: typing.Optional[typing.List[Affiliation]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
