

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListOfGs1S(UniversalBaseModel):
    """
    A list of GS1/MAPP codes
    """

    codes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of GS1/MAPP codes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
