

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .account_deletion_info import AccountDeletionInfo
from .requires_reconsent_info import RequiresReconsentInfo
from .user import User


class MeResponse(User):
    """
    Flattened user payload plus verification banner, deletion grace,
    and reconsent fields.
    """

    email_verified: typing_extensions.Annotated[
        bool, FieldMetadata(alias="emailVerified"), pydantic.Field(alias="emailVerified")
    ]
    email_verification_deadline: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="emailVerificationDeadline"),
        pydantic.Field(alias="emailVerificationDeadline"),
    ] = None
    account_deletion: typing_extensions.Annotated[
        typing.Optional[AccountDeletionInfo],
        FieldMetadata(alias="accountDeletion"),
        pydantic.Field(alias="accountDeletion"),
    ] = None
    requires_reconsent: typing_extensions.Annotated[
        typing.Optional[RequiresReconsentInfo],
        FieldMetadata(alias="requiresReconsent"),
        pydantic.Field(alias="requiresReconsent"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
