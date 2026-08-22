

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GovernmentIdNumber(UniversalBaseModel):
    """
    A government-issued ID number, such as a Social Security Number or Personal ID Number. A country code must be supplied to determine the issuing country. If not issued by an entity that can be identified using as country code, use a generic CustomIdentifier instead.
    """

    country_code: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
