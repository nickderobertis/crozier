

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .theme_rules_item_border_width import ThemeRulesItemBorderWidth
from .theme_rules_item_filter_type import ThemeRulesItemFilterType
from .theme_rules_item_filter_value import ThemeRulesItemFilterValue
from .theme_rules_item_shape import ThemeRulesItemShape


class ThemeRulesItem(UniversalBaseModel):
    description: typing.Optional[str] = None
    text: str
    background: str
    border: str
    shape: ThemeRulesItemShape
    border_width: typing_extensions.Annotated[
        ThemeRulesItemBorderWidth, FieldMetadata(alias="borderWidth"), pydantic.Field(alias="borderWidth")
    ]
    filter_type: typing_extensions.Annotated[
        ThemeRulesItemFilterType, FieldMetadata(alias="filterType"), pydantic.Field(alias="filterType")
    ]
    filter_value: typing_extensions.Annotated[
        ThemeRulesItemFilterValue, FieldMetadata(alias="filterValue"), pydantic.Field(alias="filterValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
