

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InstallationListing(UniversalBaseModel):
    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the Installation as created on the server. You can use this id to request the server's public key again.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
