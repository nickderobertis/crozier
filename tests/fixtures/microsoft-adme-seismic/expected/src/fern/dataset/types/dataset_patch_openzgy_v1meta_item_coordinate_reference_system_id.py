

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_patch_openzgy_v1meta_item_coordinate_reference_system_id_kind import (
    DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemIdKind,
)


class DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemId(UniversalBaseModel):
    kind: DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemIdKind = pydantic.Field()
    """
    The kind of reference, constant 'CRS' for FrameOfReferenceCRS.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the CRS.
    """

    persistable_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="persistableReference"),
        pydantic.Field(
            alias="persistableReference",
            description="The self-contained, persistable reference string uniquely identifying the CRS.",
        ),
    ]
    """
    The self-contained, persistable reference string uniquely identifying the CRS.
    """

    coordinate_reference_system_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="coordinateReferenceSystemID"),
        pydantic.Field(alias="coordinateReferenceSystemID", description="SRN to CRS reference."),
    ] = None
    """
    SRN to CRS reference.
    """

    property_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="propertyNames"),
        pydantic.Field(
            alias="propertyNames",
            description='The list of property names, to which this meta data item provides CRS context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.',
        ),
    ] = None
    """
    The list of property names, to which this meta data item provides CRS context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
