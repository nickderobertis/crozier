

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037account import Dbv0037Account
from .dbv0037association import Dbv0037Association
from .dbv0037error import Dbv0037Error
from .dbv0037qos import Dbv0037Qos
from .dbv0037tres_list import Dbv0037TresList
from .dbv0037user import Dbv0037User
from .dbv0037wckey import Dbv0037Wckey


class Dbv0037ConfigInfo(UniversalBaseModel):
    errors: typing.Optional[typing.List[Dbv0037Error]] = pydantic.Field(default=None)
    """
    Slurm errors
    """

    tres: typing.Optional[typing.List[Dbv0037TresList]] = pydantic.Field(default=None)
    """
    Array of TRES
    """

    accounts: typing.Optional[typing.List[Dbv0037Account]] = pydantic.Field(default=None)
    """
    Array of accounts
    """

    associations: typing.Optional[typing.List[Dbv0037Association]] = pydantic.Field(default=None)
    """
    Array of associations
    """

    users: typing.Optional[typing.List[Dbv0037User]] = pydantic.Field(default=None)
    """
    Array of users
    """

    qos: typing.Optional[typing.List[Dbv0037Qos]] = pydantic.Field(default=None)
    """
    Array of qos
    """

    wckeys: typing.Optional[typing.List[Dbv0037Wckey]] = pydantic.Field(default=None)
    """
    Array of wckeys
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
