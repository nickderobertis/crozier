

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037association_default import Dbv0037AssociationDefault
from .dbv0037association_max import Dbv0037AssociationMax
from .dbv0037association_min import Dbv0037AssociationMin
from .dbv0037association_usage import Dbv0037AssociationUsage


class Dbv0037Association(UniversalBaseModel):
    """
    Association description
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned account
    """

    cluster: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned cluster
    """

    default: typing.Optional[Dbv0037AssociationDefault] = None
    flags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of properties of association
    """

    max: typing.Optional[Dbv0037AssociationMax] = None
    min: typing.Optional[Dbv0037AssociationMin] = None
    parent_account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Parent account name
    """

    partition: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned partition
    """

    priority: typing.Optional[int] = pydantic.Field(default=None)
    """
    Assigned priority
    """

    qos: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Assigned QOS
    """

    shares_raw: typing.Optional[int] = pydantic.Field(default=None)
    """
    Raw fairshare shares
    """

    usage: typing.Optional[Dbv0037AssociationUsage] = None
    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assigned user
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
