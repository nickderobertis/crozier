

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Permit(UniversalBaseModel):
    exemption_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="exemptionCode"),
        pydantic.Field(alias="exemptionCode", description="Exemption codes - Code\tReason 1.\tResident 2.\tVisitor"),
    ] = None
    """
    Exemption codes - Code    Reason 1.    Resident 2.    Visitor
    """

    berth: typing.Optional[str] = pydantic.Field(default=None)
    """
    Berth    letter and number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
