

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InventorySearchRequestPrivacy(UniversalBaseModel):
    """
    Privacy hints from the buyer agent. AAP RECOMMENDS anonymous searches by default; user identity is only attached when a lead is submitted.
    """

    anonymous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True when no user-identifying information is included with the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
