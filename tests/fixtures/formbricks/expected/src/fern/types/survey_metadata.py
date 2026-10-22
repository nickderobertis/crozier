

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SurveyMetadata(UniversalBaseModel):
    """
    Custom link metadata for social sharing
    """

    title: typing.Optional[typing.Dict[str, str]] = None
    description: typing.Optional[typing.Dict[str, str]] = None
    og_image: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ogImage"), pydantic.Field(alias="ogImage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
