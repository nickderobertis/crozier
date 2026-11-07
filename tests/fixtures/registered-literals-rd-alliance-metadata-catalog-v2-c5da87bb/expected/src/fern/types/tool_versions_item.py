

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .identifier import Identifier
from .location import Location


class ToolVersionsItem(UniversalBaseModel):
    number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number, code or other string used to identify the version, omitting any initial “v”, “v.” or “ver.”.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full, human understandable name of this version of the tool. This should be provided only if it differs from the title given for the tool as a whole.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    If this version requires some explanation, give it here.
    """

    issued: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date on which the version was released.
    """

    locations: typing.Optional[typing.List[Location]] = pydantic.Field(default=None)
    """
    Locations where further information about this version of the tool may be accessed.
    """

    identifiers: typing.Optional[typing.List[Identifier]] = pydantic.Field(default=None)
    """
    Strings used to identify this version of the tool.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
