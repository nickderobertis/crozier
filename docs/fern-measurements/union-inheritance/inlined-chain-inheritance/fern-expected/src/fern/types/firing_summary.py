

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FiringSummary(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The kiln model that fired.
    """

    shelves: typing.List[str]
    created: typing.Optional[int] = None
    id: typing.Optional[str] = None
    usage: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
