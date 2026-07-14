

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_selector import ImageSelector


class AnalysisArchiveTransitionRuleExclude(UniversalBaseModel):
    """
    Which Images to exclude from auto-archiving logic
    """

    expiration_days: typing.Optional[int] = pydantic.Field(default=None)
    """
    How long the image selected will be excluded from the archive transition
    """

    selector: typing.Optional[ImageSelector] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
