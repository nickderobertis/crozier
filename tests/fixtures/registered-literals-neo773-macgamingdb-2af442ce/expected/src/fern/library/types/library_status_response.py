

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class LibraryStatusResponse(UniversalBaseModel):
    linked: bool
    provider: typing.Optional[str] = None
    external_user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="externalUserId"), pydantic.Field(alias="externalUserId")
    ] = None
    last_synced_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastSyncedAt"), pydantic.Field(alias="lastSyncedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
