

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_patch_openzgy_v1meta_item_two_kind import DatasetPatchOpenzgyV1MetaItemTwoKind


class DatasetPatchOpenzgyV1MetaItemTwo(UniversalBaseModel):
    kind: DatasetPatchOpenzgyV1MetaItemTwoKind = pydantic.Field()
    """
    The kind of reference, constant 'DateTime', for FrameOfReferenceDateTime.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the DateTime format and reference.
    """

    persistable_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="persistableReference"),
        pydantic.Field(
            alias="persistableReference",
            description="The self-contained, persistable reference string uniquely identifying DateTime reference.",
        ),
    ]
    """
    The self-contained, persistable reference string uniquely identifying DateTime reference.
    """

    property_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="propertyNames"),
        pydantic.Field(
            alias="propertyNames",
            description='The list of property names, to which this meta data item provides DateTime context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.',
        ),
    ] = None
    """
    The list of property names, to which this meta data item provides DateTime context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
