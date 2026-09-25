

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .link import Link


class Ok47(UniversalBaseModel):
    id: str
    vaccine_id: typing_extensions.Annotated[str, FieldMetadata(alias="vaccineId"), pydantic.Field(alias="vaccineId")]
    cvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="cvxCode"), pydantic.Field(alias="cvxCode")]
    vaccine_description: typing_extensions.Annotated[
        str, FieldMetadata(alias="vaccineDescription"), pydantic.Field(alias="vaccineDescription")
    ]
    lot_number: typing_extensions.Annotated[str, FieldMetadata(alias="lotNumber"), pydantic.Field(alias="lotNumber")]
    cpt_code: typing_extensions.Annotated[str, FieldMetadata(alias="cptCode"), pydantic.Field(alias="cptCode")]
    mvx_code: typing_extensions.Annotated[str, FieldMetadata(alias="mvxCode"), pydantic.Field(alias="mvxCode")]
    manufacturer_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="manufacturerName"), pydantic.Field(alias="manufacturerName")
    ]
    manufacturer_number: typing_extensions.Annotated[
        str, FieldMetadata(alias="manufacturerNumber"), pydantic.Field(alias="manufacturerNumber")
    ]
    strength: str
    units: str
    units_code: typing_extensions.Annotated[str, FieldMetadata(alias="unitsCode"), pydantic.Field(alias="unitsCode")]
    dose: str
    route: str
    route_code: typing_extensions.Annotated[str, FieldMetadata(alias="routeCode"), pydantic.Field(alias="routeCode")]
    side: str
    side_code: typing_extensions.Annotated[str, FieldMetadata(alias="sideCode"), pydantic.Field(alias="sideCode")]
    site: str
    site_code: typing_extensions.Annotated[str, FieldMetadata(alias="siteCode"), pydantic.Field(alias="siteCode")]
    brand_name: typing_extensions.Annotated[str, FieldMetadata(alias="brandName"), pydantic.Field(alias="brandName")]
    purchase_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="purchaseType"), pydantic.Field(alias="purchaseType")
    ]
    wasted_reason: typing_extensions.Annotated[
        str, FieldMetadata(alias="wastedReason"), pydantic.Field(alias="wastedReason")
    ]
    wasted_date: typing_extensions.Annotated[str, FieldMetadata(alias="wastedDate"), pydantic.Field(alias="wastedDate")]
    order_id: typing_extensions.Annotated[str, FieldMetadata(alias="orderId"), pydantic.Field(alias="orderId")]
    person_id: typing_extensions.Annotated[str, FieldMetadata(alias="personId"), pydantic.Field(alias="personId")]
    links: typing_extensions.Annotated[typing.List[Link], FieldMetadata(alias="_links"), pydantic.Field(alias="_links")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
