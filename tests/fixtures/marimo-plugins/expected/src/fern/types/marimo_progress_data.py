

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_progress_data_progress import MarimoProgressDataProgress


class MarimoProgressData(UniversalBaseModel):
    title: typing.Optional[str] = None
    subtitle: typing.Optional[str] = None
    progress: MarimoProgressDataProgress
    total: typing.Optional[float] = None
    eta: typing.Optional[float] = None
    rate: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
