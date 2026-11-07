

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Excerpt(UniversalBaseModel):
    """
    Excerpt generation configuration for a post or single page.
    """

    auto_generate: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoGenerate"),
        pydantic.Field(
            alias="autoGenerate",
            description="Whether Halo should generate the excerpt from the released content automatically.",
        ),
    ]
    """
    Whether Halo should generate the excerpt from the released content automatically.
    """

    raw: typing.Optional[str] = pydantic.Field(default=None)
    """
    Manual excerpt text used when autoGenerate is false.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
