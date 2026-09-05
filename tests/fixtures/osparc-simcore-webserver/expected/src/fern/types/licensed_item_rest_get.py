

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .itis_vip_resource_rest_data import ItisVipResourceRestData
from .licensed_resource_type import LicensedResourceType


class LicensedItemRestGet(UniversalBaseModel):
    licensed_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="licensedItemId"), pydantic.Field(alias="licensedItemId")
    ]
    key: str
    version: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ]
    licensed_resource_type: typing_extensions.Annotated[
        LicensedResourceType, FieldMetadata(alias="licensedResourceType"), pydantic.Field(alias="licensedResourceType")
    ]
    licensed_resources: typing_extensions.Annotated[
        typing.List[ItisVipResourceRestData],
        FieldMetadata(alias="licensedResources"),
        pydantic.Field(alias="licensedResources"),
    ]
    pricing_plan_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pricingPlanId"), pydantic.Field(alias="pricingPlanId")
    ]
    category_id: typing_extensions.Annotated[str, FieldMetadata(alias="categoryId"), pydantic.Field(alias="categoryId")]
    category_display: typing_extensions.Annotated[
        str, FieldMetadata(alias="categoryDisplay"), pydantic.Field(alias="categoryDisplay")
    ]
    category_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="categoryIcon"), pydantic.Field(alias="categoryIcon")
    ] = None
    terms_of_use_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="termsOfUseUrl"), pydantic.Field(alias="termsOfUseUrl")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
