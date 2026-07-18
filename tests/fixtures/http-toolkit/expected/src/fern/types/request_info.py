

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RequestInfo(UniversalBaseModel):
    """
    Details of an incoming HTTP request
    """

    method: str
    path: str
    remote_addr: typing_extensions.Annotated[str, FieldMetadata(alias="remoteAddr"), pydantic.Field(alias="remoteAddr")]
    headers: typing.Dict[str, str]
    query: typing.Optional[typing.Dict[str, str]] = None
    body: typing.Optional[str] = None
    timestamp: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
