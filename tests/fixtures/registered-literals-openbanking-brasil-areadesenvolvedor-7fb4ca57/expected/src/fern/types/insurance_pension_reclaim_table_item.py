

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class InsurancePensionReclaimTableItem(UniversalBaseModel):
    initial_month_range: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="initialMonthRange"), pydantic.Field(alias="initialMonthRange")
    ] = None
    final_month_range: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="finalMonthRange"), pydantic.Field(alias="finalMonthRange")
    ] = None
    percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    Percentual de faixa de resgate.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
