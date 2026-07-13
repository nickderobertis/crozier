

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyDefinitionsDestinyVendorRequirementDisplayEntryDefinition(UniversalBaseModel):
    """
    The localized properties of the requirementsDisplay, allowing information about the requirement or item being featured to be seen.
    """

    icon: typing.Optional[str] = None
    name: typing.Optional[str] = None
    source: typing.Optional[str] = None
    type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
