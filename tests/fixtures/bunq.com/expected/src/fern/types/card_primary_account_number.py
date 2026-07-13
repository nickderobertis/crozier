

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CardPrimaryAccountNumber(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for this PAN.
    """

    four_digit: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last four digits of the PAN.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID for this Virtual PAN.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the monetary account to assign to this PAN, only for Online Cards.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status for this PAN, only for Online Cards.
    """

    uuid_: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="uuid")] = pydantic.Field(default=None)
    """
    The UUID for this Virtual PAN.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
