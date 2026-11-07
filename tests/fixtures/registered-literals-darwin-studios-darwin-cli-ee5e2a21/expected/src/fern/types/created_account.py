

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .created_account_status import CreatedAccountStatus
from .created_account_type import CreatedAccountType


class CreatedAccount(UniversalBaseModel):
    id: str
    type: CreatedAccountType
    name: str
    status: CreatedAccountStatus
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    next_step: typing_extensions.Annotated[str, FieldMetadata(alias="nextStep"), pydantic.Field(alias="nextStep")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
