

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pending_deletion_response_code import PendingDeletionResponseCode


class PendingDeletionResponse(UniversalBaseModel):
    code: PendingDeletionResponseCode
    deletion_date: typing_extensions.Annotated[
        str, FieldMetadata(alias="deletionDate"), pydantic.Field(alias="deletionDate")
    ]
    restore_url: typing_extensions.Annotated[str, FieldMetadata(alias="restoreUrl"), pydantic.Field(alias="restoreUrl")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
