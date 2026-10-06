

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HttpRequest(UniversalBaseModel):
    """
    Serializable HTTP request representation.

        Mimics Starlette/FastAPI Request but is pickle-able and contains only a safe
        subset of data. Excludes session and auth to prevent exposing sensitive data.

        Attributes:
            url: Serialized URL with path, port, scheme, netloc, query, hostname.
            base_url: Serialized base URL.
            headers: Request headers (marimo-specific headers excluded).
            query_params: Query parameters mapped to lists of values.
            path_params: Path parameters from the URL route.
            cookies: Request cookies.
            meta: User-defined storage for custom data.
            user: User info from authentication middleware (e.g., is_authenticated, username).
    """

    base_url: typing.Dict[str, typing.Any]
    cookies: typing.Dict[str, str]
    headers: typing.Dict[str, str]
    meta: typing.Dict[str, typing.Any]
    path_params: typing.Dict[str, typing.Any]
    query_params: typing.Dict[str, typing.List[str]]
    url: typing.Dict[str, typing.Any]
    user: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
