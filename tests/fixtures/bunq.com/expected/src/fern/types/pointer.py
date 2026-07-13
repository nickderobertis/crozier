

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pointer(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The alias name.
    """

    service: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pointer service. Only required for external counterparties.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The alias type, can be: EMAIL|PHONE_NUMBER|IBAN.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The alias value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
