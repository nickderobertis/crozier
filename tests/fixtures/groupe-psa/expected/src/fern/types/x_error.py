

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class XError(UniversalBaseModel):
    """
    Detailed error
    """

    code: typing.Optional[int] = None
    uuid_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None
    message: typing.Optional[str] = None
    timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
