

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DashboardWidgetItem(UniversalBaseModel):
    subtitle: str
    title: str
    link: str
    icon_url: typing_extensions.Annotated[str, FieldMetadata(alias="iconUrl"), pydantic.Field(alias="iconUrl")]
    since_id: typing_extensions.Annotated[str, FieldMetadata(alias="sinceId"), pydantic.Field(alias="sinceId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
