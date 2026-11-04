

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TermCode(UniversalBaseModel):
    """
    The termCode defines a concept based on a coding system (i.e. LOINC). The triplet of code, system and version identify the concept.
    """

    code: str
    system: str
    version: typing.Optional[str] = None
    display: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
