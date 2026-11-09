

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .highlight_info import HighlightInfo


class OneShotInfo(UniversalBaseModel):
    data: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Data found during scan, e.g. Licenses, Copyrights
    """

    highlights: typing.Optional[typing.List[HighlightInfo]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
