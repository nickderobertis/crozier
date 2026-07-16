

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveCashDrawerShiftRequest(UniversalBaseModel):
    """ """

    location_id: str = pydantic.Field()
    """
    The ID of the location to retrieve cash drawer shifts from.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
