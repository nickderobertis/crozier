

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IbanAccountIdentification(UniversalBaseModel):
    bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    The bank's 8- or 11-character BIC or SWIFT code.
    """

    iban: str = pydantic.Field()
    """
    The international bank account number as defined in the [ISO-13616](https://www.iso.org/standard/81090.html) standard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
