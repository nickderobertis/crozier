

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .get_site_plan_plans_response_id import GetSitePlanPlansResponseId
from .get_site_plan_plans_response_name import GetSitePlanPlansResponseName


class GetSitePlanPlansResponse(UniversalBaseModel):
    id: typing.Optional[GetSitePlanPlansResponseId] = pydantic.Field(default=None)
    """
    ID of the hosting plan.
    """

    name: typing.Optional[GetSitePlanPlansResponseName] = pydantic.Field(default=None)
    """
    Name of the hosting plan.
    """

    pricing_info: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pricingInfo"),
        pydantic.Field(alias="pricingInfo", description="URL for more information about Webflow hosting plan pricing."),
    ] = None
    """
    URL for more information about Webflow hosting plan pricing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
