

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .grace_period import GracePeriod
from .insurance_pension_reclaim_table_item import InsurancePensionReclaimTableItem


class InsurancePensionReclaim(UniversalBaseModel):
    table: typing.Optional[typing.List[InsurancePensionReclaimTableItem]] = None
    grace_period: typing_extensions.Annotated[
        typing.Optional[GracePeriod], FieldMetadata(alias="gracePeriod"), pydantic.Field(alias="gracePeriod")
    ] = None
    differenciated_percentage: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="differenciatedPercentage"),
        pydantic.Field(alias="differenciatedPercentage", description="Campo aberto (possibilidade de incluir URL)"),
    ] = None
    """
    Campo aberto (possibilidade de incluir URL)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
