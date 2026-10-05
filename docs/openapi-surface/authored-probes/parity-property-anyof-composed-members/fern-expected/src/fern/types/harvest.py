

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .harvest_container import HarvestContainer
from .harvest_grade import HarvestGrade
from .harvest_holder import HarvestHolder
from .harvest_yield_note import HarvestYieldNote


class Harvest(UniversalBaseModel):
    orchard: str
    yield_note: typing.Optional[HarvestYieldNote] = None
    grade: typing.Optional[HarvestGrade] = None
    container: typing.Optional[HarvestContainer] = None
    holder: typing.Optional[HarvestHolder] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
