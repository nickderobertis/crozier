

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .links import Links


class StockOnHandItem(UniversalBaseModel):
    id: float
    item_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="itemDescription"), pydantic.Field(alias="itemDescription")
    ]
    job_id: typing_extensions.Annotated[float, FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")]
    job_phase_id: typing_extensions.Annotated[
        float, FieldMetadata(alias="jobPhaseId"), pydantic.Field(alias="jobPhaseId")
    ]
    item_cost: typing_extensions.Annotated[float, FieldMetadata(alias="itemCost"), pydantic.Field(alias="itemCost")]
    item_cost_quantity: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemCostQuantity"), pydantic.Field(alias="itemCostQuantity")
    ]
    item_cost_total: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemCostTotal"), pydantic.Field(alias="itemCostTotal")
    ]
    item_price: typing_extensions.Annotated[float, FieldMetadata(alias="itemPrice"), pydantic.Field(alias="itemPrice")]
    item_quantity: typing_extensions.Annotated[
        float, FieldMetadata(alias="itemQuantity"), pydantic.Field(alias="itemQuantity")
    ]
    item_total: typing_extensions.Annotated[float, FieldMetadata(alias="itemTotal"), pydantic.Field(alias="itemTotal")]
    created_by: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    date_entered: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateEntered"), pydantic.Field(alias="dateEntered")
    ]
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    links: typing.List[Links]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
