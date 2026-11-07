

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mandate_response_status import MandateResponseStatus


class MandateResponse(UniversalBaseModel):
    """
    Details of the mandate linked to the saved payment instrument.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of mandate stored for the checkout or payment instrument.
    """

    status: typing.Optional[MandateResponseStatus] = pydantic.Field(default=None)
    """
    Current lifecycle status of the mandate.
    """

    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short unique identifier for the merchant for which the mandate is valid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
