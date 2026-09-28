

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .open_api_expectation_spec_url_or_payload import OpenApiExpectationSpecUrlOrPayload


class OpenApiExpectation(UniversalBaseModel):
    """
    open api or swagger expectation
    """

    spec_url_or_payload: typing_extensions.Annotated[
        OpenApiExpectationSpecUrlOrPayload,
        FieldMetadata(alias="specUrlOrPayload"),
        pydantic.Field(alias="specUrlOrPayload"),
    ]
    operations_and_responses: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="operationsAndResponses"),
        pydantic.Field(alias="operationsAndResponses"),
    ] = None
    context_path_prefix: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contextPathPrefix"), pydantic.Field(alias="contextPathPrefix")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
