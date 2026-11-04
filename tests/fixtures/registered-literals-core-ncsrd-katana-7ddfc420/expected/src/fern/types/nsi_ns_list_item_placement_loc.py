

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NsiNsListItemPlacementLoc(UniversalBaseModel):
    """
    Detailed info regarding the placement of the NS
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location where the NS is running
    """

    vim: typing.Optional[str] = pydantic.Field(default=None)
    """
    The VIM ID of the location where the NS is hosted
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
