

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RetireRequest(UniversalBaseModel):
    id: typing.Optional[str] = None
    contract_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contractId"), pydantic.Field(alias="contractId")
    ] = None
    base_token_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="baseTokenId"), pydantic.Field(alias="baseTokenId")
    ] = None
    owner: typing.Optional[str] = None
    opposite_token_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oppositeTokenId"), pydantic.Field(alias="oppositeTokenId")
    ] = None
    base_token_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="baseTokenCount"), pydantic.Field(alias="baseTokenCount")
    ] = None
    opposite_token_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="oppositeTokenCount"), pydantic.Field(alias="oppositeTokenCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
