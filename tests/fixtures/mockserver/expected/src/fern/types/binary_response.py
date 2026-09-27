

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class BinaryResponse(UniversalBaseModel):
    """
    binary response to return
    """

    delay: typing.Optional[Delay] = None
    binary_data: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="binaryData"), pydantic.Field(alias="binaryData")
    ] = None
    primary: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
