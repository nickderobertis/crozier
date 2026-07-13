

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .share_detail_draft_payment import ShareDetailDraftPayment
from .share_detail_payment import ShareDetailPayment
from .share_detail_read_only import ShareDetailReadOnly


class ShareDetail(UniversalBaseModel):
    draft_payment: typing.Optional[ShareDetailDraftPayment] = pydantic.Field(default=None)
    """
    The share details for a draft payment share. In the response 'draft_payment' is replaced by 'ShareDetailDraftPayment'.
    """

    payment: typing.Optional[ShareDetailPayment] = pydantic.Field(default=None)
    """
    The share details for a payment share. In the response 'payment' is replaced by 'ShareDetailPayment'.
    """

    read_only: typing.Optional[ShareDetailReadOnly] = pydantic.Field(default=None)
    """
    The share details for viewing a share. In the response 'read_only' is replaced by 'ShareDetailReadOnly'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
