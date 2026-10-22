

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .dataset_patch_segy_v1meta_item_unit_of_measure_id_kind import DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind


class DatasetPatchSegyV1MetaItemUnitOfMeasureId(UniversalBaseModel):
    kind: DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind = pydantic.Field()
    """
    The kind of reference, 'Unit' for FrameOfReferenceUOM.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unit symbol or name of the unit.
    """

    persistable_reference: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="persistableReference"),
        pydantic.Field(
            alias="persistableReference",
            description="The self-contained, persistable reference string uniquely identifying the Unit.",
        ),
    ]
    """
    The self-contained, persistable reference string uniquely identifying the Unit.
    """

    unit_of_measure_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unitOfMeasureID"),
        pydantic.Field(alias="unitOfMeasureID", description="SRN to unit of measure reference."),
    ] = None
    """
    SRN to unit of measure reference.
    """

    property_names: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="propertyNames"),
        pydantic.Field(
            alias="propertyNames",
            description='The list of property names, to which this meta data item provides Unit context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.',
        ),
    ] = None
    """
    The list of property names, to which this meta data item provides Unit context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "Data.StructureA.PropertyB" to define a unique context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
