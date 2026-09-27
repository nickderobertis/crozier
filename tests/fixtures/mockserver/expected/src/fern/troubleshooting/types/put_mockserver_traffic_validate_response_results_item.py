

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PutMockserverTrafficValidateResponseResultsItem(UniversalBaseModel):
    method: typing.Optional[str] = None
    path: typing.Optional[str] = None
    matched_operation: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="matchedOperation"), pydantic.Field(alias="matchedOperation")
    ] = None
    passed: typing.Optional[bool] = None
    request_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="requestErrors"), pydantic.Field(alias="requestErrors")
    ] = None
    response_errors: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="responseErrors"), pydantic.Field(alias="responseErrors")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
