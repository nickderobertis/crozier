

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .load_capture_source import LoadCaptureSource


class LoadCapture(UniversalBaseModel):
    """
    a declarative cross-step capture / correlation rule: extracts a value from a step's response and binds it to a variable name that a later step in the same iteration can reference from its templated request fields. Best-effort: on no match it falls back to defaultValue (when set) or leaves the variable unset, never failing the run.
    """

    name: str = pydantic.Field()
    """
    the variable name later steps reference (e.g. 'token' for $iteration.captured.token)
    """

    source: LoadCaptureSource = pydantic.Field()
    """
    where to extract from: a JSONPath over the response body, a response header value, or a regex over the response body string
    """

    expression: str = pydantic.Field()
    """
    the JSONPath (BODY_JSONPATH), header name (HEADER), or regex (BODY_REGEX, capture group 1) driving the extraction
    """

    default_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="defaultValue"),
        pydantic.Field(
            alias="defaultValue",
            description="optional fallback value bound to the variable when extraction yields nothing; when omitted the variable is left unset on no match",
        ),
    ] = None
    """
    optional fallback value bound to the variable when extraction yields nothing; when omitted the variable is left unset on no match
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
