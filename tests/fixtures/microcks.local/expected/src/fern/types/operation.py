

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .binding import Binding
from .parameter_constraint import ParameterConstraint


class Operation(UniversalBaseModel):
    """
    An Operation of a Service or API
    """

    bindings: typing.Optional[typing.Dict[str, Binding]] = pydantic.Field(default=None)
    """
    Map of protocol binding details for this operation
    """

    default_delay: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="defaultDelay")] = (
        pydantic.Field(default=None)
    )
    """
    Default response time delay for mocks
    """

    dispatcher: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dispatcher strategy used for mocks
    """

    dispatcher_rules: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dispatcherRules")] = (
        pydantic.Field(default=None)
    )
    """
    DispatcherRules used for mocks
    """

    input_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="inputName")] = pydantic.Field(
        default=None
    )
    """
    Name of input parameters in case of Xml based Service
    """

    method: str = pydantic.Field()
    """
    Represents transport method
    """

    name: str = pydantic.Field()
    """
    Unique name of this Operation within Service scope
    """

    output_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="outputName")] = pydantic.Field(
        default=None
    )
    """
    Name of output parameters in case of Xml based Service
    """

    parameter_contraints: typing_extensions.Annotated[
        typing.Optional[typing.List[ParameterConstraint]], FieldMetadata(alias="parameterContraints")
    ] = pydantic.Field(default=None)
    """
    Contraints that may apply to mock invocatino on this operation
    """

    resource_paths: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="resourcePaths")
    ] = pydantic.Field(default=None)
    """
    Paths the mocks endpoints are mapped on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
