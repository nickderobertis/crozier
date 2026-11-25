

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SurveyRequest(UniversalBaseModel):
    area: typing.Optional[str] = pydantic.Field(default=None)
    """
    
    The surveyed area.
        Give it as a basin name or a pontoon range.
    """

    depth: typing.Optional[int] = pydantic.Field(default=None)
    """
    
    The deepest sounding wanted.
    Metres below chart datum.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
