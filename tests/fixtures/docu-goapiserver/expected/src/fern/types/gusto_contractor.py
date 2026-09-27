

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GustoContractor(UniversalBaseModel):
    """
    Gusto Contractor.
    """

    gusto_company_id: str
    id: str
    business_name: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    hourly_rate: str
    is_active: int
    type: typing.Optional[str] = None
    wage_type: typing.Optional[str] = None
    school_name: str
    school_id: typing.Optional[str] = None
    monday_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="MondayItemId"), pydantic.Field(alias="MondayItemId")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
