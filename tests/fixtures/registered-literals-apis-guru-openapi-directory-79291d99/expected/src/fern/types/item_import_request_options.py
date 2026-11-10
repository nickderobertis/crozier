

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ItemImportRequestOptions(UniversalBaseModel):
    """
    An optional object to configure `/item/import` request.
    """

    webhook: typing.Optional[str] = pydantic.Field(default=None)
    """
    Specifies a webhook URL to associate with an Item. Plaid fires a webhook if credentials fail.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
