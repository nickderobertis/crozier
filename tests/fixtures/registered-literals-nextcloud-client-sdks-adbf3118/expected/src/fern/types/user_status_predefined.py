

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_status_clear_at import UserStatusClearAt


class UserStatusPredefined(UniversalBaseModel):
    id: str
    icon: str
    message: str
    clear_at: typing_extensions.Annotated[
        UserStatusClearAt, FieldMetadata(alias="clearAt"), pydantic.Field(alias="clearAt")
    ]
    visible: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
