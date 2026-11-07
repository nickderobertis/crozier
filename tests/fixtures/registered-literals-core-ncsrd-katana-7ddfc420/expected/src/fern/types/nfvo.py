

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nfvo_config import NfvoConfig


class Nfvo(UniversalBaseModel):
    """
    A new NFVO
    """

    id: str = pydantic.Field()
    """
    Unique id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name for the new NFVO
    """

    nfvoip: str = pydantic.Field()
    """
    NFVO's authentication URL - example: http://10.200.64.2:5000/v3/
    """

    nfvousername: str = pydantic.Field()
    """
    The admin username
    """

    nfvopassword: str = pydantic.Field()
    """
    The admin password
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    NFVO's type
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the NFVO's OS
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the NFVO
    """

    config: typing.Optional[NfvoConfig] = pydantic.Field(default=None)
    """
    Optional parameters regarding the NFVO operation - example: network: flat
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
