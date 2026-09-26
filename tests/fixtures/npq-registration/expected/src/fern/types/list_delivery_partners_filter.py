

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListDeliveryPartnersFilter(UniversalBaseModel):
    """
    Filter delivery partners to return more specific results
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Return only delivery partners from the specified cohort.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
