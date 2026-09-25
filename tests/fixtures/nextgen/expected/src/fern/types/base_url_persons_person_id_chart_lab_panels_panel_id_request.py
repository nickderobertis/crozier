

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BaseUrlPersonsPersonIdChartLabPanelsPanelIdRequest(UniversalBaseModel):
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="OrderId"), pydantic.Field(alias="OrderId")]
    ordered_test_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="OrderedTestId"), pydantic.Field(alias="OrderedTestId")
    ]
    collection_date_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="CollectionDateTime"), pydantic.Field(alias="CollectionDateTime")
    ]
    status: typing_extensions.Annotated[str, FieldMetadata(alias="Status"), pydantic.Field(alias="Status")]
    panel_comment: typing_extensions.Annotated[
        str, FieldMetadata(alias="PanelComment"), pydantic.Field(alias="PanelComment")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
