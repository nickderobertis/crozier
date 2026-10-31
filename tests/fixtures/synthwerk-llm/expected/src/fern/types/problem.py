

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Problem(UniversalBaseModel):
    """
    RFC 9457 problem details with the stable Synthwerk `code`.
    Clients branch on `code`, never on `title` or `detail`, and must accept unknown codes.

    | Code | Status | Cause |
    |---|---|---|
    | `invalid_request` | 400 | Body or parameter not valid. |
    | `unauthenticated` | 401 | Token missing or not valid. |
    | `forbidden` | 403 | Scope or origin does not allow the call. |
    | `not_found` | 404 | Unknown id or another owner's id. |
    | `input_too_large` | 413 | Message above the input limit. |
    | `too_many_streams` | 429 | Owner has the max number of open streams. |
    | `quota_exhausted` | 429 | Reserved (D-46). Not sent in M2. |
    | `model_unavailable` | 503 | Provider down or busy. Also as an `error` event mid-stream. |
    """

    type: str = pydantic.Field()
    """
    `https://schemas.synthwerk.dev/problems/<code>`.
    """

    title: str = pydantic.Field()
    """
    Short summary of the problem type. Same for every instance.
    """

    status: int = pydantic.Field()
    """
    HTTP status. In an `error` event the HTTP status stays 200; this field holds the status the error maps to.
    """

    code: str = pydantic.Field()
    """
    Stable machine code, for example `model_unavailable`.
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Explanation for this instance. No secrets, no personal data, no provider error text.
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI of this instance, for example the request path.
    """

    trace_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    W3C trace id of the request, for support.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
