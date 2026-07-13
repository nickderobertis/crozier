

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .label_monetary_account import LabelMonetaryAccount
from .label_user import LabelUser
from .relation_user import RelationUser
from .share_detail import ShareDetail


class ShareInviteMonetaryAccountResponse(UniversalBaseModel):
    access_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of access that is wanted, one of VIEW_BALANCE, VIEW_TRANSACTION, DRAFT_PAYMENT or FULL_TRANSIENT
    """

    card_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The card to link to the shared monetary account. Used only if share_detail is ShareDetailCardPayment.
    """

    counter_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The monetary account and user who created the share.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the ShareInviteBankResponse creation.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of this share. It is basically the monetary account description.
    """

    draft_share_invite_bank_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the draft share invite bank.
    """

    end_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expiration date of this share.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the ShareInviteBankResponse.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the monetary account the ACCEPTED share applies to. null otherwise.
    """

    relation_user: typing.Optional[RelationUser] = pydantic.Field(default=None)
    """
    All of the relation users towards this MA.
    """

    share_detail: typing.Optional[ShareDetail] = pydantic.Field(default=None)
    """
    The share details.
    """

    share_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The share type, either STANDARD or MUTUAL.
    """

    start_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The start date of this share.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the share. Can be ACTIVE, REVOKED, REJECTED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the ShareInviteBankResponse last update.
    """

    user_alias_cancelled: typing.Optional[LabelUser] = pydantic.Field(default=None)
    """
    The user who cancelled the share if it has been revoked or rejected.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
