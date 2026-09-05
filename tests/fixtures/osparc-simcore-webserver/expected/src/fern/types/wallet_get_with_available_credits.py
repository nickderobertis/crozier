

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .group_id_int import GroupIdInt
from .wallet_id_int import WalletIdInt
from .wallet_status import WalletStatus


class WalletGetWithAvailableCredits(UniversalBaseModel):
    wallet_id: typing_extensions.Annotated[
        WalletIdInt, FieldMetadata(alias="walletId"), pydantic.Field(alias="walletId")
    ]
    name: str
    description: typing.Optional[str] = None
    owner: GroupIdInt
    thumbnail: typing.Optional[str] = None
    status: WalletStatus
    created: dt.datetime
    modified: dt.datetime
    available_credits: typing_extensions.Annotated[
        str, FieldMetadata(alias="availableCredits"), pydantic.Field(alias="availableCredits")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
