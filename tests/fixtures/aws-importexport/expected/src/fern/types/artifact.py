

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .description import Description
from .url import Url


class Artifact(UniversalBaseModel):
    """
    A discrete item that contains the description and URL of an artifact (such as a PDF).
    """

    description: typing_extensions.Annotated[
        typing.Optional[Description], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    url: typing_extensions.Annotated[typing.Optional[Url], FieldMetadata(alias="URL"), pydantic.Field(alias="URL")] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
