

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .save_image_response_mode import SaveImageResponseMode


class SaveImageResponse(UniversalBaseModel):
    asset_id: typing.Optional[str] = None
    image_id: str
    image_url: str
    mode: SaveImageResponseMode
    replaced: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
