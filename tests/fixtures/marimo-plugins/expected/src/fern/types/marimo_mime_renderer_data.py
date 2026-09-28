

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .marimo_mime_renderer_data_data import MarimoMimeRendererDataData


class MarimoMimeRendererData(UniversalBaseModel):
    mime: str
    data: typing.Optional[MarimoMimeRendererDataData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
