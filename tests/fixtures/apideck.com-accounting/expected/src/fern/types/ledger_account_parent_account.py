

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LedgerAccountParentAccount(UniversalBaseModel):
    display_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human readable display ID used when displaying the parent account
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the parent account.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the parent account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
