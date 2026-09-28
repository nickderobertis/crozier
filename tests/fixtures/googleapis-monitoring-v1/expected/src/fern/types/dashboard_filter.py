

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dashboard_filter_filter_type import DashboardFilterFilterType


class DashboardFilter(UniversalBaseModel):
    """
    A filter to reduce the amount of data charted in relevant widgets.
    """

    filter_type: typing_extensions.Annotated[
        typing.Optional[DashboardFilterFilterType],
        FieldMetadata(alias="filterType"),
        pydantic.Field(alias="filterType", description="The specified filter type"),
    ] = None
    """
    The specified filter type
    """

    label_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="labelKey"),
        pydantic.Field(alias="labelKey", description="Required. The key for the label"),
    ] = None
    """
    Required. The key for the label
    """

    string_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="stringValue"),
        pydantic.Field(alias="stringValue", description="A variable-length string value."),
    ] = None
    """
    A variable-length string value.
    """

    template_variable: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateVariable"),
        pydantic.Field(
            alias="templateVariable",
            description="The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard.",
        ),
    ] = None
    """
    The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
