

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TokensTwitchDropHistoryResponse(UniversalBaseModel):
    claim_state: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ClaimState"), pydantic.Field(alias="ClaimState")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="CreatedAt"), pydantic.Field(alias="CreatedAt")
    ] = None
    description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Description"), pydantic.Field(alias="Description")
    ] = None
    title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="Title"), pydantic.Field(alias="Title")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
