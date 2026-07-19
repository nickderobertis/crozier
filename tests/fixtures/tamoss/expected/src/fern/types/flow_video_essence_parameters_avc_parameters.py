

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowVideoEssenceParametersAvcParameters(UniversalBaseModel):
    profile: int = pydantic.Field()
    """
    AVC / H.264 profile byte. For more information on the use of this property in codec strings, see https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#using_the_codecs_parameter
    """

    level: int = pydantic.Field()
    """
    AVC / H.264 level byte. For more information on the use of this property in codec strings, see https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#using_the_codecs_parameter
    """

    flags: int = pydantic.Field()
    """
    AVC / H.264 flags byte. For more information on the use of this property in codec strings, see https://developer.mozilla.org/en-US/docs/Web/Media/Formats/codecs_parameter#using_the_codecs_parameter
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
