

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .property_difference_difference_type import PropertyDifferenceDifferenceType


class PropertyDifference(UniversalBaseModel):
    """
    Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose <code>StackResourceDriftStatus</code> is <code>MODIFIED</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.
    """

    property_path: typing_extensions.Annotated[str, FieldMetadata(alias="PropertyPath")] = pydantic.Field()
    """
    The fully-qualified path to the resource property.
    """

    expected_value: typing_extensions.Annotated[str, FieldMetadata(alias="ExpectedValue")] = pydantic.Field()
    """
    The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.
    """

    actual_value: typing_extensions.Annotated[str, FieldMetadata(alias="ActualValue")] = pydantic.Field()
    """
    The actual property value of the resource property.
    """

    difference_type: typing_extensions.Annotated[
        PropertyDifferenceDifferenceType, FieldMetadata(alias="DifferenceType")
    ] = pydantic.Field()
    """
    <p>The type of property difference.</p> <ul> <li> <p> <code>ADD</code>: A value has been added to a resource property that's an array or list data type.</p> </li> <li> <p> <code>REMOVE</code>: The property has been removed from the current resource configuration.</p> </li> <li> <p> <code>NOT_EQUAL</code>: The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).</p> </li> </ul>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
