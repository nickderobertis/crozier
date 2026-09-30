

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .email_account_deletion_credentials import EmailAccountDeletionCredentials


class MeDeletionEmailCredentials(UniversalBaseModel):
    email_credentials: typing_extensions.Annotated[
        EmailAccountDeletionCredentials,
        FieldMetadata(alias="emailCredentials"),
        pydantic.Field(alias="emailCredentials"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
