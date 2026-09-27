

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .title_role import TitleRole
from .title_sub_role import TitleSubRole


class Title(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The inputted title from our data sources with some basic cleaning and mapping in order to help with merging
    """

    levels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Levels associated with a title
    """

    role: typing.Optional[TitleRole] = pydantic.Field(default=None)
    """
    A person's job title derived role
    """

    sub_role: typing.Optional[TitleSubRole] = pydantic.Field(default=None)
    """
    A person's job title derived subrole. Each subrole maps to a role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
