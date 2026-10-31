

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .properties_by_id_response_data_unit_statuses_item import PropertiesByIdResponseDataUnitStatusesItem


class PropertiesByIdResponseData(UniversalBaseModel):
    unit_statuses: typing_extensions.Annotated[
        typing.List[PropertiesByIdResponseDataUnitStatusesItem],
        FieldMetadata(alias="unitStatuses"),
        pydantic.Field(alias="unitStatuses", description="Unit status values available for filtering."),
    ]
    """
    Unit status values available for filtering.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
