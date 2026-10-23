



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dataset_patch_acls import DatasetPatchAcls
    from .dataset_patch_openzgy_v1 import DatasetPatchOpenzgyV1
    from .dataset_patch_openzgy_v1acl import DatasetPatchOpenzgyV1Acl
    from .dataset_patch_openzgy_v1ancestry import DatasetPatchOpenzgyV1Ancestry
    from .dataset_patch_openzgy_v1data import DatasetPatchOpenzgyV1Data
    from .dataset_patch_openzgy_v1data_dataset_properties import DatasetPatchOpenzgyV1DataDatasetProperties
    from .dataset_patch_openzgy_v1data_dataset_properties_file_source_infos_item import (
        DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_patch_openzgy_v1data_endian import DatasetPatchOpenzgyV1DataEndian
    from .dataset_patch_openzgy_v1legal import DatasetPatchOpenzgyV1Legal
    from .dataset_patch_openzgy_v1meta_item import DatasetPatchOpenzgyV1MetaItem
    from .dataset_patch_openzgy_v1meta_item_coordinate_reference_system_id import (
        DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_patch_openzgy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_patch_openzgy_v1meta_item_three import DatasetPatchOpenzgyV1MetaItemThree
    from .dataset_patch_openzgy_v1meta_item_three_kind import DatasetPatchOpenzgyV1MetaItemThreeKind
    from .dataset_patch_openzgy_v1meta_item_two import DatasetPatchOpenzgyV1MetaItemTwo
    from .dataset_patch_openzgy_v1meta_item_two_kind import DatasetPatchOpenzgyV1MetaItemTwoKind
    from .dataset_patch_openzgy_v1meta_item_unit_of_measure_id import DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId
    from .dataset_patch_openzgy_v1meta_item_unit_of_measure_id_kind import (
        DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind,
    )
    from .dataset_patch_segy_v1 import DatasetPatchSegyV1
    from .dataset_patch_segy_v1acl import DatasetPatchSegyV1Acl
    from .dataset_patch_segy_v1ancestry import DatasetPatchSegyV1Ancestry
    from .dataset_patch_segy_v1data import DatasetPatchSegyV1Data
    from .dataset_patch_segy_v1data_dataset_properties import DatasetPatchSegyV1DataDatasetProperties
    from .dataset_patch_segy_v1data_dataset_properties_file_source_infos_item import (
        DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_patch_segy_v1data_endian import DatasetPatchSegyV1DataEndian
    from .dataset_patch_segy_v1data_vector_header_mapping_item import DatasetPatchSegyV1DataVectorHeaderMappingItem
    from .dataset_patch_segy_v1data_vector_header_mapping_item_scalar_indicator import (
        DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator,
    )
    from .dataset_patch_segy_v1legal import DatasetPatchSegyV1Legal
    from .dataset_patch_segy_v1meta_item import DatasetPatchSegyV1MetaItem
    from .dataset_patch_segy_v1meta_item_coordinate_reference_system_id import (
        DatasetPatchSegyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_patch_segy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetPatchSegyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_patch_segy_v1meta_item_three import DatasetPatchSegyV1MetaItemThree
    from .dataset_patch_segy_v1meta_item_three_kind import DatasetPatchSegyV1MetaItemThreeKind
    from .dataset_patch_segy_v1meta_item_two import DatasetPatchSegyV1MetaItemTwo
    from .dataset_patch_segy_v1meta_item_two_kind import DatasetPatchSegyV1MetaItemTwoKind
    from .dataset_patch_segy_v1meta_item_unit_of_measure_id import DatasetPatchSegyV1MetaItemUnitOfMeasureId
    from .dataset_patch_segy_v1meta_item_unit_of_measure_id_kind import DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind
    from .dataset_patch_seismicmeta import DatasetPatchSeismicmeta
    from .dataset_register_body_acls import DatasetRegisterBodyAcls
    from .dataset_register_body_openzgy_v1 import DatasetRegisterBodyOpenzgyV1
    from .dataset_register_body_openzgy_v1acl import DatasetRegisterBodyOpenzgyV1Acl
    from .dataset_register_body_openzgy_v1ancestry import DatasetRegisterBodyOpenzgyV1Ancestry
    from .dataset_register_body_openzgy_v1data import DatasetRegisterBodyOpenzgyV1Data
    from .dataset_register_body_openzgy_v1data_dataset_properties import (
        DatasetRegisterBodyOpenzgyV1DataDatasetProperties,
    )
    from .dataset_register_body_openzgy_v1data_dataset_properties_file_source_infos_item import (
        DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_register_body_openzgy_v1data_endian import DatasetRegisterBodyOpenzgyV1DataEndian
    from .dataset_register_body_openzgy_v1legal import DatasetRegisterBodyOpenzgyV1Legal
    from .dataset_register_body_openzgy_v1meta_item import DatasetRegisterBodyOpenzgyV1MetaItem
    from .dataset_register_body_openzgy_v1meta_item_coordinate_reference_system_id import (
        DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_register_body_openzgy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_register_body_openzgy_v1meta_item_three import DatasetRegisterBodyOpenzgyV1MetaItemThree
    from .dataset_register_body_openzgy_v1meta_item_three_kind import DatasetRegisterBodyOpenzgyV1MetaItemThreeKind
    from .dataset_register_body_openzgy_v1meta_item_two import DatasetRegisterBodyOpenzgyV1MetaItemTwo
    from .dataset_register_body_openzgy_v1meta_item_two_kind import DatasetRegisterBodyOpenzgyV1MetaItemTwoKind
    from .dataset_register_body_openzgy_v1meta_item_unit_of_measure_id import (
        DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId,
    )
    from .dataset_register_body_openzgy_v1meta_item_unit_of_measure_id_kind import (
        DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind,
    )
    from .dataset_register_body_segy_v1 import DatasetRegisterBodySegyV1
    from .dataset_register_body_segy_v1acl import DatasetRegisterBodySegyV1Acl
    from .dataset_register_body_segy_v1ancestry import DatasetRegisterBodySegyV1Ancestry
    from .dataset_register_body_segy_v1data import DatasetRegisterBodySegyV1Data
    from .dataset_register_body_segy_v1data_dataset_properties import DatasetRegisterBodySegyV1DataDatasetProperties
    from .dataset_register_body_segy_v1data_dataset_properties_file_source_infos_item import (
        DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_register_body_segy_v1data_endian import DatasetRegisterBodySegyV1DataEndian
    from .dataset_register_body_segy_v1data_vector_header_mapping_item import (
        DatasetRegisterBodySegyV1DataVectorHeaderMappingItem,
    )
    from .dataset_register_body_segy_v1data_vector_header_mapping_item_scalar_indicator import (
        DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator,
    )
    from .dataset_register_body_segy_v1legal import DatasetRegisterBodySegyV1Legal
    from .dataset_register_body_segy_v1meta_item import DatasetRegisterBodySegyV1MetaItem
    from .dataset_register_body_segy_v1meta_item_coordinate_reference_system_id import (
        DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_register_body_segy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_register_body_segy_v1meta_item_three import DatasetRegisterBodySegyV1MetaItemThree
    from .dataset_register_body_segy_v1meta_item_three_kind import DatasetRegisterBodySegyV1MetaItemThreeKind
    from .dataset_register_body_segy_v1meta_item_two import DatasetRegisterBodySegyV1MetaItemTwo
    from .dataset_register_body_segy_v1meta_item_two_kind import DatasetRegisterBodySegyV1MetaItemTwoKind
    from .dataset_register_body_segy_v1meta_item_unit_of_measure_id import (
        DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId,
    )
    from .dataset_register_body_segy_v1meta_item_unit_of_measure_id_kind import (
        DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind,
    )
    from .dataset_register_body_seismicmeta import DatasetRegisterBodySeismicmeta
    from .dataset_register_body_seismicmeta_data import DatasetRegisterBodySeismicmetaData
_dynamic_imports: typing.Dict[str, str] = {
    "DatasetPatchAcls": ".dataset_patch_acls",
    "DatasetPatchOpenzgyV1": ".dataset_patch_openzgy_v1",
    "DatasetPatchOpenzgyV1Acl": ".dataset_patch_openzgy_v1acl",
    "DatasetPatchOpenzgyV1Ancestry": ".dataset_patch_openzgy_v1ancestry",
    "DatasetPatchOpenzgyV1Data": ".dataset_patch_openzgy_v1data",
    "DatasetPatchOpenzgyV1DataDatasetProperties": ".dataset_patch_openzgy_v1data_dataset_properties",
    "DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_patch_openzgy_v1data_dataset_properties_file_source_infos_item",
    "DatasetPatchOpenzgyV1DataEndian": ".dataset_patch_openzgy_v1data_endian",
    "DatasetPatchOpenzgyV1Legal": ".dataset_patch_openzgy_v1legal",
    "DatasetPatchOpenzgyV1MetaItem": ".dataset_patch_openzgy_v1meta_item",
    "DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemId": ".dataset_patch_openzgy_v1meta_item_coordinate_reference_system_id",
    "DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_patch_openzgy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetPatchOpenzgyV1MetaItemThree": ".dataset_patch_openzgy_v1meta_item_three",
    "DatasetPatchOpenzgyV1MetaItemThreeKind": ".dataset_patch_openzgy_v1meta_item_three_kind",
    "DatasetPatchOpenzgyV1MetaItemTwo": ".dataset_patch_openzgy_v1meta_item_two",
    "DatasetPatchOpenzgyV1MetaItemTwoKind": ".dataset_patch_openzgy_v1meta_item_two_kind",
    "DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId": ".dataset_patch_openzgy_v1meta_item_unit_of_measure_id",
    "DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind": ".dataset_patch_openzgy_v1meta_item_unit_of_measure_id_kind",
    "DatasetPatchSegyV1": ".dataset_patch_segy_v1",
    "DatasetPatchSegyV1Acl": ".dataset_patch_segy_v1acl",
    "DatasetPatchSegyV1Ancestry": ".dataset_patch_segy_v1ancestry",
    "DatasetPatchSegyV1Data": ".dataset_patch_segy_v1data",
    "DatasetPatchSegyV1DataDatasetProperties": ".dataset_patch_segy_v1data_dataset_properties",
    "DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_patch_segy_v1data_dataset_properties_file_source_infos_item",
    "DatasetPatchSegyV1DataEndian": ".dataset_patch_segy_v1data_endian",
    "DatasetPatchSegyV1DataVectorHeaderMappingItem": ".dataset_patch_segy_v1data_vector_header_mapping_item",
    "DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator": ".dataset_patch_segy_v1data_vector_header_mapping_item_scalar_indicator",
    "DatasetPatchSegyV1Legal": ".dataset_patch_segy_v1legal",
    "DatasetPatchSegyV1MetaItem": ".dataset_patch_segy_v1meta_item",
    "DatasetPatchSegyV1MetaItemCoordinateReferenceSystemId": ".dataset_patch_segy_v1meta_item_coordinate_reference_system_id",
    "DatasetPatchSegyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_patch_segy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetPatchSegyV1MetaItemThree": ".dataset_patch_segy_v1meta_item_three",
    "DatasetPatchSegyV1MetaItemThreeKind": ".dataset_patch_segy_v1meta_item_three_kind",
    "DatasetPatchSegyV1MetaItemTwo": ".dataset_patch_segy_v1meta_item_two",
    "DatasetPatchSegyV1MetaItemTwoKind": ".dataset_patch_segy_v1meta_item_two_kind",
    "DatasetPatchSegyV1MetaItemUnitOfMeasureId": ".dataset_patch_segy_v1meta_item_unit_of_measure_id",
    "DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind": ".dataset_patch_segy_v1meta_item_unit_of_measure_id_kind",
    "DatasetPatchSeismicmeta": ".dataset_patch_seismicmeta",
    "DatasetRegisterBodyAcls": ".dataset_register_body_acls",
    "DatasetRegisterBodyOpenzgyV1": ".dataset_register_body_openzgy_v1",
    "DatasetRegisterBodyOpenzgyV1Acl": ".dataset_register_body_openzgy_v1acl",
    "DatasetRegisterBodyOpenzgyV1Ancestry": ".dataset_register_body_openzgy_v1ancestry",
    "DatasetRegisterBodyOpenzgyV1Data": ".dataset_register_body_openzgy_v1data",
    "DatasetRegisterBodyOpenzgyV1DataDatasetProperties": ".dataset_register_body_openzgy_v1data_dataset_properties",
    "DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_register_body_openzgy_v1data_dataset_properties_file_source_infos_item",
    "DatasetRegisterBodyOpenzgyV1DataEndian": ".dataset_register_body_openzgy_v1data_endian",
    "DatasetRegisterBodyOpenzgyV1Legal": ".dataset_register_body_openzgy_v1legal",
    "DatasetRegisterBodyOpenzgyV1MetaItem": ".dataset_register_body_openzgy_v1meta_item",
    "DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemId": ".dataset_register_body_openzgy_v1meta_item_coordinate_reference_system_id",
    "DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_register_body_openzgy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetRegisterBodyOpenzgyV1MetaItemThree": ".dataset_register_body_openzgy_v1meta_item_three",
    "DatasetRegisterBodyOpenzgyV1MetaItemThreeKind": ".dataset_register_body_openzgy_v1meta_item_three_kind",
    "DatasetRegisterBodyOpenzgyV1MetaItemTwo": ".dataset_register_body_openzgy_v1meta_item_two",
    "DatasetRegisterBodyOpenzgyV1MetaItemTwoKind": ".dataset_register_body_openzgy_v1meta_item_two_kind",
    "DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId": ".dataset_register_body_openzgy_v1meta_item_unit_of_measure_id",
    "DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind": ".dataset_register_body_openzgy_v1meta_item_unit_of_measure_id_kind",
    "DatasetRegisterBodySegyV1": ".dataset_register_body_segy_v1",
    "DatasetRegisterBodySegyV1Acl": ".dataset_register_body_segy_v1acl",
    "DatasetRegisterBodySegyV1Ancestry": ".dataset_register_body_segy_v1ancestry",
    "DatasetRegisterBodySegyV1Data": ".dataset_register_body_segy_v1data",
    "DatasetRegisterBodySegyV1DataDatasetProperties": ".dataset_register_body_segy_v1data_dataset_properties",
    "DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_register_body_segy_v1data_dataset_properties_file_source_infos_item",
    "DatasetRegisterBodySegyV1DataEndian": ".dataset_register_body_segy_v1data_endian",
    "DatasetRegisterBodySegyV1DataVectorHeaderMappingItem": ".dataset_register_body_segy_v1data_vector_header_mapping_item",
    "DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator": ".dataset_register_body_segy_v1data_vector_header_mapping_item_scalar_indicator",
    "DatasetRegisterBodySegyV1Legal": ".dataset_register_body_segy_v1legal",
    "DatasetRegisterBodySegyV1MetaItem": ".dataset_register_body_segy_v1meta_item",
    "DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemId": ".dataset_register_body_segy_v1meta_item_coordinate_reference_system_id",
    "DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_register_body_segy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetRegisterBodySegyV1MetaItemThree": ".dataset_register_body_segy_v1meta_item_three",
    "DatasetRegisterBodySegyV1MetaItemThreeKind": ".dataset_register_body_segy_v1meta_item_three_kind",
    "DatasetRegisterBodySegyV1MetaItemTwo": ".dataset_register_body_segy_v1meta_item_two",
    "DatasetRegisterBodySegyV1MetaItemTwoKind": ".dataset_register_body_segy_v1meta_item_two_kind",
    "DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId": ".dataset_register_body_segy_v1meta_item_unit_of_measure_id",
    "DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind": ".dataset_register_body_segy_v1meta_item_unit_of_measure_id_kind",
    "DatasetRegisterBodySeismicmeta": ".dataset_register_body_seismicmeta",
    "DatasetRegisterBodySeismicmetaData": ".dataset_register_body_seismicmeta_data",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "DatasetPatchAcls",
    "DatasetPatchOpenzgyV1",
    "DatasetPatchOpenzgyV1Acl",
    "DatasetPatchOpenzgyV1Ancestry",
    "DatasetPatchOpenzgyV1Data",
    "DatasetPatchOpenzgyV1DataDatasetProperties",
    "DatasetPatchOpenzgyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetPatchOpenzgyV1DataEndian",
    "DatasetPatchOpenzgyV1Legal",
    "DatasetPatchOpenzgyV1MetaItem",
    "DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemId",
    "DatasetPatchOpenzgyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetPatchOpenzgyV1MetaItemThree",
    "DatasetPatchOpenzgyV1MetaItemThreeKind",
    "DatasetPatchOpenzgyV1MetaItemTwo",
    "DatasetPatchOpenzgyV1MetaItemTwoKind",
    "DatasetPatchOpenzgyV1MetaItemUnitOfMeasureId",
    "DatasetPatchOpenzgyV1MetaItemUnitOfMeasureIdKind",
    "DatasetPatchSegyV1",
    "DatasetPatchSegyV1Acl",
    "DatasetPatchSegyV1Ancestry",
    "DatasetPatchSegyV1Data",
    "DatasetPatchSegyV1DataDatasetProperties",
    "DatasetPatchSegyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetPatchSegyV1DataEndian",
    "DatasetPatchSegyV1DataVectorHeaderMappingItem",
    "DatasetPatchSegyV1DataVectorHeaderMappingItemScalarIndicator",
    "DatasetPatchSegyV1Legal",
    "DatasetPatchSegyV1MetaItem",
    "DatasetPatchSegyV1MetaItemCoordinateReferenceSystemId",
    "DatasetPatchSegyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetPatchSegyV1MetaItemThree",
    "DatasetPatchSegyV1MetaItemThreeKind",
    "DatasetPatchSegyV1MetaItemTwo",
    "DatasetPatchSegyV1MetaItemTwoKind",
    "DatasetPatchSegyV1MetaItemUnitOfMeasureId",
    "DatasetPatchSegyV1MetaItemUnitOfMeasureIdKind",
    "DatasetPatchSeismicmeta",
    "DatasetRegisterBodyAcls",
    "DatasetRegisterBodyOpenzgyV1",
    "DatasetRegisterBodyOpenzgyV1Acl",
    "DatasetRegisterBodyOpenzgyV1Ancestry",
    "DatasetRegisterBodyOpenzgyV1Data",
    "DatasetRegisterBodyOpenzgyV1DataDatasetProperties",
    "DatasetRegisterBodyOpenzgyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetRegisterBodyOpenzgyV1DataEndian",
    "DatasetRegisterBodyOpenzgyV1Legal",
    "DatasetRegisterBodyOpenzgyV1MetaItem",
    "DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemId",
    "DatasetRegisterBodyOpenzgyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetRegisterBodyOpenzgyV1MetaItemThree",
    "DatasetRegisterBodyOpenzgyV1MetaItemThreeKind",
    "DatasetRegisterBodyOpenzgyV1MetaItemTwo",
    "DatasetRegisterBodyOpenzgyV1MetaItemTwoKind",
    "DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureId",
    "DatasetRegisterBodyOpenzgyV1MetaItemUnitOfMeasureIdKind",
    "DatasetRegisterBodySegyV1",
    "DatasetRegisterBodySegyV1Acl",
    "DatasetRegisterBodySegyV1Ancestry",
    "DatasetRegisterBodySegyV1Data",
    "DatasetRegisterBodySegyV1DataDatasetProperties",
    "DatasetRegisterBodySegyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetRegisterBodySegyV1DataEndian",
    "DatasetRegisterBodySegyV1DataVectorHeaderMappingItem",
    "DatasetRegisterBodySegyV1DataVectorHeaderMappingItemScalarIndicator",
    "DatasetRegisterBodySegyV1Legal",
    "DatasetRegisterBodySegyV1MetaItem",
    "DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemId",
    "DatasetRegisterBodySegyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetRegisterBodySegyV1MetaItemThree",
    "DatasetRegisterBodySegyV1MetaItemThreeKind",
    "DatasetRegisterBodySegyV1MetaItemTwo",
    "DatasetRegisterBodySegyV1MetaItemTwoKind",
    "DatasetRegisterBodySegyV1MetaItemUnitOfMeasureId",
    "DatasetRegisterBodySegyV1MetaItemUnitOfMeasureIdKind",
    "DatasetRegisterBodySeismicmeta",
    "DatasetRegisterBodySeismicmetaData",
]
