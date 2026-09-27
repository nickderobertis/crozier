

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TransactionRequestOperationsOperationsItemActionDeformerSplit(UniversalBaseModel):
    source_deformer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sourceDeformerId"), pydantic.Field(alias="sourceDeformerId")
    ]
    parent_deformer_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="parentDeformerId"), pydantic.Field(alias="parentDeformerId")
    ]
    move_parameter_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="moveParameterIds"), pydantic.Field(alias="moveParameterIds")
    ]
    parent_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentName"), pydantic.Field(alias="parentName")
    ] = None
    expected_parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expectedParentId"), pydantic.Field(alias="expectedParentId")
    ] = None
    parent_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="parentTags"), pydantic.Field(alias="parentTags")
    ] = None
    source_tags: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="sourceTags"), pydantic.Field(alias="sourceTags")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
