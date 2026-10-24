

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .pilot_ads_component import PilotAdsComponent
from .pilot_amazon_spapi_component import PilotAmazonSpapiComponent
from .pilot_count_component import PilotCountComponent
from .pilot_open_ai_component import PilotOpenAiComponent
from .pilot_schema_component import PilotSchemaComponent


class PilotTenantComponents(UniversalBaseModel):
    schema_: typing_extensions.Annotated[
        PilotSchemaComponent, FieldMetadata(alias="schema"), pydantic.Field(alias="schema")
    ]
    amazon_spapi: PilotAmazonSpapiComponent
    agent_graph: PilotCountComponent
    daily_ops: PilotCountComponent
    openai: PilotOpenAiComponent
    amazon_ads_l5: PilotAdsComponent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
