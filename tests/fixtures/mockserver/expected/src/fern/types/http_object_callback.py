

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay


class HttpObjectCallback(UniversalBaseModel):
    """
    object / method callback
    """

    delay: typing.Optional[Delay] = None
    client_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId")
    ] = None
    response_callback: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="responseCallback"), pydantic.Field(alias="responseCallback")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
