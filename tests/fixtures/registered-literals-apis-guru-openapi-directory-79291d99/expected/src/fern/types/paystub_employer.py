

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paystub_address import PaystubAddress


class PaystubEmployer(UniversalBaseModel):
    """
    Information about the employer on the paystub
    """

    address: typing.Optional[PaystubAddress] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the employer on the paystub.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
