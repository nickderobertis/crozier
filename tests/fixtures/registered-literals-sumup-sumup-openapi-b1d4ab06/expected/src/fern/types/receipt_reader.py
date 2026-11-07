

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReceiptReader(UniversalBaseModel):
    """
    Card reader details displayed on the receipt.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the physical card reader.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model of the physical card reader.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
