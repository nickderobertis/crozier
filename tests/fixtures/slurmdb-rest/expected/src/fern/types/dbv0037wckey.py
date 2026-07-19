

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037Wckey(UniversalBaseModel):
    accounts: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of assigned accounts
    """

    cluster: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster name
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    wckey database unique id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    wckey name
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    wckey user
    """

    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of wckey
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
