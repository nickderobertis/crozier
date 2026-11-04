

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.node_types2 import NodeTypes2
from ...types.parameter import Parameter
from ...types.service_ref import ServiceRef
from ...types.user_defined_additional_node_fields import UserDefinedAdditionalNodeFields


class GenerateEnricherMockRequestDtoEnricher(UniversalBaseModel):
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    branch_parameters_template: typing_extensions.Annotated[
        typing.Optional[typing.List[Parameter]],
        FieldMetadata(alias="branchParametersTemplate"),
        pydantic.Field(alias="branchParametersTemplate"),
    ] = None
    id: str
    output: str
    service: ServiceRef
    type: NodeTypes2

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
