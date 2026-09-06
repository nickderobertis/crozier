

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .communication_models_field_filter_comparison import CommunicationModelsFieldFilterComparison
from .communication_models_field_filter_type import CommunicationModelsFieldFilterType


class CommunicationModelsFieldFilter(UniversalBaseModel):
    comparison: typing_extensions.Annotated[
        typing.Optional[CommunicationModelsFieldFilterComparison],
        FieldMetadata(alias="Comparison"),
        pydantic.Field(
            alias="Comparison", description="Optional. The type of value comparison to apply.  Default is Equal."
        ),
    ] = None
    """
    Optional. The type of value comparison to apply.  Default is Equal.
    """

    field: typing_extensions.Annotated[
        str, FieldMetadata(alias="Field"), pydantic.Field(alias="Field", description="The field to filter")
    ]
    """
    The field to filter
    """

    type: typing_extensions.Annotated[
        typing.Optional[CommunicationModelsFieldFilterType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="Optional. The filter type. Default is HasFieldMatching."),
    ] = None
    """
    Optional. The filter type. Default is HasFieldMatching.
    """

    value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Value"),
        pydantic.Field(
            alias="Value",
            description='The value used with comparison to filter results. Do not use with "Set" comparisons',
        ),
    ] = None
    """
    The value used with comparison to filter results. Do not use with "Set" comparisons
    """

    values: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Values"),
        pydantic.Field(
            alias="Values",
            description='The set of values to use with comparison to filter results.  Use with "Set" comparisons.',
        ),
    ] = None
    """
    The set of values to use with comparison to filter results.  Use with "Set" comparisons.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
