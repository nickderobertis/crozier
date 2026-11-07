

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identifier import Identifier
from .location import Location


class MappingVersionsItem(UniversalBaseModel):
    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number, code or other string used to identify the version, omitting any initial “v”, “v.” or “ver.”.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this version requires some explanation, give it here.
    """

    issued: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which the version was published.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about this version of the mapping may be accessed.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify this version of the mapping.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
