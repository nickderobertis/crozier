

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2
from ...core.serialization import FieldMetadata
from ...types.axis_treeless import AxisTreeless


class Axis(AxisTreeless):
    """
    Read more about axes in the [definition for the axisSection resource](reference/Organization-v3.yaml/components/schemas/AxisSection).
    """

    parent_axis: typing_extensions.Annotated[
        typing.Optional[AxisTreeless], FieldMetadata(alias="parentAxis"), pydantic.Field(alias="parentAxis")
    ] = None
    children_axes: typing_extensions.Annotated[
        typing.Optional[typing.List[AxisTreeless]],
        FieldMetadata(alias="childrenAxes"),
        pydantic.Field(alias="childrenAxes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
