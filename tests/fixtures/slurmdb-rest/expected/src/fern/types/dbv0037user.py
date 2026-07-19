

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037coordinator_info import Dbv0037CoordinatorInfo
from .dbv0037user_associations import Dbv0037UserAssociations
from .dbv0037user_default import Dbv0037UserDefault


class Dbv0037User(UniversalBaseModel):
    """
    User description
    """

    administrator_level: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of administrator level
    """

    associations: typing.Optional[Dbv0037UserAssociations] = None
    coordinators: typing.Optional[typing.List[Dbv0037CoordinatorInfo]] = pydantic.Field(default=None)
    """
    List of assigned coordinators
    """

    default: typing.Optional[Dbv0037UserDefault] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    User name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
