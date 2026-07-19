

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037AssociationShortInfo(UniversalBaseModel):
    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account name
    """

    cluster: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cluster name
    """

    partition: typing.Optional[str] = pydantic.Field(default=None)
    """
    Partition name (optional)
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
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
