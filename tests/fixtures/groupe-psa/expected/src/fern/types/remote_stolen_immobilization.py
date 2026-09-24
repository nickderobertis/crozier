

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RemoteStolenImmobilization(UniversalBaseModel):
    """
    Requesting the stolen vehicle for immobilization.
    """

    activate: bool = pydantic.Field()
    """
    Set, if ```true```, the vehicle as immobilized or not (otherwise).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
