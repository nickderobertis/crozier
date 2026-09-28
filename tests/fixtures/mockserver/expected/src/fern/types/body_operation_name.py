

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_operation_name_type import BodyOperationNameType


class BodyOperationName(UniversalBaseModel):
    """
    GraphQL body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: BodyOperationNameType
    query: str
    operation_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="operationName"), pydantic.Field(alias="operationName")
    ] = None
    variables_schema: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="variablesSchema"), pydantic.Field(alias="variablesSchema")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
