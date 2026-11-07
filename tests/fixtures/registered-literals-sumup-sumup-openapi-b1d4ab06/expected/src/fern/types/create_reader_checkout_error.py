

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_reader_checkout_error_errors import CreateReaderCheckoutErrorErrors


class CreateReaderCheckoutError(UniversalBaseModel):
    """
    Error description
    """

    errors: CreateReaderCheckoutErrorErrors

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
