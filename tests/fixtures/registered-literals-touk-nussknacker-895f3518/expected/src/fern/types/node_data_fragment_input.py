

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fragment_parameter import FragmentParameter
from .fragment_ref import FragmentRef
from .user_defined_additional_node_fields import UserDefinedAdditionalNodeFields


class NodeDataFragmentInput(UniversalBaseModel):
    additional_fields: typing_extensions.Annotated[
        typing.Optional[UserDefinedAdditionalNodeFields],
        FieldMetadata(alias="additionalFields"),
        pydantic.Field(alias="additionalFields"),
    ] = None
    id: str
    is_disabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDisabled"), pydantic.Field(alias="isDisabled")
    ] = None
    fragment_params: typing_extensions.Annotated[
        typing.Optional[typing.List[FragmentParameter]],
        FieldMetadata(alias="fragmentParams"),
        pydantic.Field(alias="fragmentParams"),
    ] = None
    ref: FragmentRef

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
