

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser


class ShareInviteMonetaryAccountInquiryRead(UniversalBaseModel):
    access_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of access that is in place.
    """

    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label of the monetary account that's being shared.
    """

    counter_user_alias: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The label of the user to share with.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the newly created share invite.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the monetary account the share applies to.
    """

    relationship: typing.Optional[str] = pydantic.Field(default=None)
    """
    The relationship: COMPANY_DIRECTOR, COMPANY_EMPLOYEE, etc
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the share. Can be ACTIVE, REVOKED, REJECTED.
    """

    user_alias_created: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user who created the share.
    """

    user_alias_revoked: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user who revoked the share.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
