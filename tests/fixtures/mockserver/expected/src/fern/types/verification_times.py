

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VerificationTimes(UniversalBaseModel):
    """
    number of request to verify
    """

    at_least: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="atLeast"), pydantic.Field(alias="atLeast")
    ] = None
    at_most: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="atMost"), pydantic.Field(alias="atMost")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
