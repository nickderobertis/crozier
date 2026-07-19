

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_short_info import Dbv0037AssociationShortInfo
from .dbv0037coordinator_info import Dbv0037CoordinatorInfo


class Dbv0037Account(UniversalBaseModel):
    """
    Account description
    """

    associations: typing.Optional[typing.List[Dbv0037AssociationShortInfo]] = pydantic.Field(default=None)
    """
    List of assigned associations
    """

    coordinators: typing.Optional[typing.List[Dbv0037CoordinatorInfo]] = pydantic.Field(default=None)
    """
    List of assigned coordinators
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of account
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of account
    """

    organization: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned organization of account
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
