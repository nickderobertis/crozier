

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .retire_request_dto_tokens import RetireRequestDtoTokens


class RetireRequestDto(UniversalBaseModel):
    id: str
    contract_id: typing_extensions.Annotated[str, FieldMetadata(alias="contractId"), pydantic.Field(alias="contractId")]
    tokens: RetireRequestDtoTokens
    token_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="tokenIds"), pydantic.Field(alias="tokenIds")
    ]
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
