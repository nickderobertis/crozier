

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .string import String


class TooManyCookieNamesInWhiteList(UniversalBaseModel):
    """
    Your request contains more cookie names in the whitelist than are allowed per cache behavior.
    """

    message: typing_extensions.Annotated[
        typing.Optional[String], FieldMetadata(alias="Message"), pydantic.Field(alias="Message")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
