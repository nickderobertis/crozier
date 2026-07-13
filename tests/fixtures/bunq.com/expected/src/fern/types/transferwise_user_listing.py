

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransferwiseUserListing(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the TransferwiseUser's creation.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email the user is registered with at TransferWise.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the TransferwiseUser.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name the user is registered with at TransferWise.
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    The source of the user at TransferWise.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the TransferwiseUser's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
