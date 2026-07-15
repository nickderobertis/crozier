

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .api_reference import ApiReference


class Alignment(ApiReference):
    """
    `Alignment`
    """

    abbreviation: typing.Optional[str] = pydantic.Field(default=None)
    """
    Abbreviation/initials/acronym for the alignment.
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brief description of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
