

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ShipRef(UniversalBaseModel):
    ship: str = pydantic.Field()
    """
    Host ship, `~`-prefixed (e.g. `~zod`).
    """

    name: str = pydantic.Field()
    """
    Slug part of the flag (`@tas`-validated, lowercase).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
