

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OpenApiDefinition(UniversalBaseModel):
    """
    open api or swagger request matcher
    """

    spec_url_or_payload: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="specUrlOrPayload"), pydantic.Field(alias="specUrlOrPayload")
    ] = None
    operation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="operationId"), pydantic.Field(alias="operationId")
    ] = None
    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
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
