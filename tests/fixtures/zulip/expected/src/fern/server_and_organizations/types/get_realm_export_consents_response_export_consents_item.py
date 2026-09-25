

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.email_address_visibility import EmailAddressVisibility


class GetRealmExportConsentsResponseExportConsentsItem(UniversalBaseModel):
    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The user ID.
    """

    consented: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user has consented for their private data export.
    """

    email_address_visibility: typing.Optional[EmailAddressVisibility] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
