

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .survey_cores_fragments import SurveyCoresFragments


class SurveyCores(UniversalBaseModel):
    """
    Drill cores, untyped with empty items and nested properties.
    """

    length: typing.Optional[float] = None
    fragments: typing.Optional[SurveyCoresFragments] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
