

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .retouch_photo_request_options_finish import RetouchPhotoRequestOptionsFinish


class RetouchPhotoRequestOptions(UniversalBaseModel):
    """
    How to retouch the photo.
    """

    finish: typing.Optional[RetouchPhotoRequestOptionsFinish] = None
    strength: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
