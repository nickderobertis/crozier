

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_callout_output_data_kind import MarimoCalloutOutputDataKind


class MarimoCalloutOutputData(UniversalBaseModel):
    html: str
    kind: typing.Optional[MarimoCalloutOutputDataKind] = None
    title: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
