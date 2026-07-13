

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyDefinitionsDestinyVendorServiceDefinition(UniversalBaseModel):
    """
    When a vendor provides services, this is the localized name of those services.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The localized name of a service provided.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
