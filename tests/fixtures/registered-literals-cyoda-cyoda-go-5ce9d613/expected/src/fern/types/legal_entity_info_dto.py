

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LegalEntityInfoDto(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the legal entity
    """

    name: str = pydantic.Field()
    """
    Name of the legal entity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
