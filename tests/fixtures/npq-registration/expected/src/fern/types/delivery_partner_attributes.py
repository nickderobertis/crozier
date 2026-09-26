

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeliveryPartnerAttributes(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the delivery partner
    """

    cohort: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The starting years of the cohorts the delivery partner is valid for
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the delivery partner was created
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the delivery partner was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
