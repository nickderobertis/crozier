

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TaxpayerId(UniversalBaseModel):
    """
    Taxpayer ID of the individual receiving the paystub.
    """

    id_mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID mask; i.e. last 4 digits of the taxpayer ID
    """

    id_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of ID, e.g. 'SSN'
    """

    last4digits: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="last_4_digits"),
        pydantic.Field(alias="last_4_digits", description="Last 4 digits of unique number of ID."),
    ] = None
    """
    Last 4 digits of unique number of ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
