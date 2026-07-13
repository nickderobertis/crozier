

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser
from .share_detail import ShareDetail


class ShareInviteMonetaryAccountInquiry(UniversalBaseModel):
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

    draft_share_invite_bank_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    DEPRECATED: USE `access_type` INSTEAD | The id of the draft share invite bank.
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    DEPRECATED: USE `access_type` INSTEAD | The expiration date of this share.
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

    share_detail: typing.Optional[ShareDetail] = pydantic.Field(default=None)
    """
    DEPRECATED: USE `access_type` INSTEAD | The share details. Only one of these objects may be passed.
    """

    share_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    DEPRECATED: USE `access_type` INSTEAD | The share type, either STANDARD or MUTUAL.
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    DEPRECATED: USE `access_type` INSTEAD | The start date of this share.
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
