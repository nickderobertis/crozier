

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V60DisplayRate(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Label for this display rate line (e.g. the jurisdiction name).
    """

    rate: float = pydantic.Field()
    """
    Rate for this display line, as a decimal fraction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
