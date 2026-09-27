

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Parameter(UniversalBaseModel):
    """
    Preview: Parameter value applied to the aggregation function. This is a preview feature and may be subject to change before final release.
    """

    double_value: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="doubleValue"),
        pydantic.Field(alias="doubleValue", description="A floating-point parameter value."),
    ] = None
    """
    A floating-point parameter value.
    """

    int_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="intValue"),
        pydantic.Field(alias="intValue", description="An integer parameter value."),
    ] = None
    """
    An integer parameter value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
