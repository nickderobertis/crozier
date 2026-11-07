

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DetectImageMetrics(UniversalBaseModel):
    """
    Image detection metrics (for image media type)
    """

    type: str = pydantic.Field()
    """
    Type of image analysis performed
    """

    label: str = pydantic.Field()
    """
    Detection label (fake or real)
    """

    image: str = pydantic.Field()
    """
    URL to visualization image
    """

    score: float = pydantic.Field()
    """
    Detection confidence score
    """

    children: typing.List[typing.Dict[str, typing.Any]] = pydantic.Field()
    """
    Nested analysis results (structure varies by pipeline)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
