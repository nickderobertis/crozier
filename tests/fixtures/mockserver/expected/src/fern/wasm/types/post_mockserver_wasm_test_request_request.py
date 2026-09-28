

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostMockserverWasmTestRequestRequest(UniversalBaseModel):
    """
    the sample request the rule is evaluated against
    """

    method: typing.Optional[str] = None
    path: typing.Optional[str] = None
    headers: typing.Optional[typing.Dict[str, typing.List[str]]] = None
    query_string_parameters: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.List[str]]],
        FieldMetadata(alias="queryStringParameters"),
        pydantic.Field(alias="queryStringParameters"),
    ] = None
    cookies: typing.Optional[typing.Dict[str, str]] = None
    body: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
