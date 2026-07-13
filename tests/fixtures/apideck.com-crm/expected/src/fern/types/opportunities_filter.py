

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpportunitiesFilter(UniversalBaseModel):
    company_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company ID to filter on
    """

    monetary_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Monetary amount to filter on
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status to filter on
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Title of the opportunity to filter on
    """

    win_probability: typing.Optional[float] = pydantic.Field(default=None)
    """
    Win probability to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
