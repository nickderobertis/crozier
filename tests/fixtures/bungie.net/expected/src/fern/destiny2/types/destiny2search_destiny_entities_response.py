

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.destiny_definitions_destiny_entity_search_result import DestinyDefinitionsDestinyEntitySearchResult


class Destiny2SearchDestinyEntitiesResponse(UniversalBaseModel):
    detailed_error_trace: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="DetailedErrorTrace")
    ] = None
    error_code: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="ErrorCode")] = None
    error_status: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ErrorStatus")] = None
    message: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Message")] = None
    message_data: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="MessageData")
    ] = None
    response: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyEntitySearchResult], FieldMetadata(alias="Response")
    ] = None
    throttle_seconds: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="ThrottleSeconds")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
