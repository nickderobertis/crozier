

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SuppliersFilter(UniversalBaseModel):
    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company Name of supplier to search for
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of supplier to search for
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
