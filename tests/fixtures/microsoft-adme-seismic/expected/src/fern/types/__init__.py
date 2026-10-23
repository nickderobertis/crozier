



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_token import AccessToken
    from .dataset import Dataset
    from .dataset_and_directories import DatasetAndDirectories
    from .dataset_check_list import DatasetCheckList
    from .dataset_openzgy_v1 import DatasetOpenzgyV1
    from .dataset_openzgy_v1acl import DatasetOpenzgyV1Acl
    from .dataset_openzgy_v1ancestry import DatasetOpenzgyV1Ancestry
    from .dataset_openzgy_v1data import DatasetOpenzgyV1Data
    from .dataset_openzgy_v1data_dataset_properties import DatasetOpenzgyV1DataDatasetProperties
    from .dataset_openzgy_v1data_dataset_properties_file_source_infos_item import (
        DatasetOpenzgyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_openzgy_v1data_endian import DatasetOpenzgyV1DataEndian
    from .dataset_openzgy_v1legal import DatasetOpenzgyV1Legal
    from .dataset_openzgy_v1meta_item import DatasetOpenzgyV1MetaItem
    from .dataset_openzgy_v1meta_item_coordinate_reference_system_id import (
        DatasetOpenzgyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_openzgy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetOpenzgyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_openzgy_v1meta_item_three import DatasetOpenzgyV1MetaItemThree
    from .dataset_openzgy_v1meta_item_three_kind import DatasetOpenzgyV1MetaItemThreeKind
    from .dataset_openzgy_v1meta_item_two import DatasetOpenzgyV1MetaItemTwo
    from .dataset_openzgy_v1meta_item_two_kind import DatasetOpenzgyV1MetaItemTwoKind
    from .dataset_openzgy_v1meta_item_unit_of_measure_id import DatasetOpenzgyV1MetaItemUnitOfMeasureId
    from .dataset_openzgy_v1meta_item_unit_of_measure_id_kind import DatasetOpenzgyV1MetaItemUnitOfMeasureIdKind
    from .dataset_permission import DatasetPermission
    from .dataset_segy_v1 import DatasetSegyV1
    from .dataset_segy_v1acl import DatasetSegyV1Acl
    from .dataset_segy_v1ancestry import DatasetSegyV1Ancestry
    from .dataset_segy_v1data import DatasetSegyV1Data
    from .dataset_segy_v1data_dataset_properties import DatasetSegyV1DataDatasetProperties
    from .dataset_segy_v1data_dataset_properties_file_source_infos_item import (
        DatasetSegyV1DataDatasetPropertiesFileSourceInfosItem,
    )
    from .dataset_segy_v1data_endian import DatasetSegyV1DataEndian
    from .dataset_segy_v1data_vector_header_mapping_item import DatasetSegyV1DataVectorHeaderMappingItem
    from .dataset_segy_v1data_vector_header_mapping_item_scalar_indicator import (
        DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator,
    )
    from .dataset_segy_v1legal import DatasetSegyV1Legal
    from .dataset_segy_v1meta_item import DatasetSegyV1MetaItem
    from .dataset_segy_v1meta_item_coordinate_reference_system_id import (
        DatasetSegyV1MetaItemCoordinateReferenceSystemId,
    )
    from .dataset_segy_v1meta_item_coordinate_reference_system_id_kind import (
        DatasetSegyV1MetaItemCoordinateReferenceSystemIdKind,
    )
    from .dataset_segy_v1meta_item_three import DatasetSegyV1MetaItemThree
    from .dataset_segy_v1meta_item_three_kind import DatasetSegyV1MetaItemThreeKind
    from .dataset_segy_v1meta_item_two import DatasetSegyV1MetaItemTwo
    from .dataset_segy_v1meta_item_two_kind import DatasetSegyV1MetaItemTwoKind
    from .dataset_segy_v1meta_item_unit_of_measure_id import DatasetSegyV1MetaItemUnitOfMeasureId
    from .dataset_segy_v1meta_item_unit_of_measure_id_kind import DatasetSegyV1MetaItemUnitOfMeasureIdKind
    from .dataset_seismicmeta import DatasetSeismicmeta
    from .dataset_size import DatasetSize
    from .impersonation_token import ImpersonationToken
    from .ls_datasets import LsDatasets
    from .ls_paginated_datasets import LsPaginatedDatasets
    from .paginated_datasets import PaginatedDatasets
    from .resource import Resource
    from .status import Status
    from .sub_project import SubProject
    from .sub_project_access_policy import SubProjectAccessPolicy
    from .sub_project_acls import SubProjectAcls
    from .tenant import Tenant
    from .user_remove_request import UserRemoveRequest
    from .user_roles import UserRoles
_dynamic_imports: typing.Dict[str, str] = {
    "AccessToken": ".access_token",
    "Dataset": ".dataset",
    "DatasetAndDirectories": ".dataset_and_directories",
    "DatasetCheckList": ".dataset_check_list",
    "DatasetOpenzgyV1": ".dataset_openzgy_v1",
    "DatasetOpenzgyV1Acl": ".dataset_openzgy_v1acl",
    "DatasetOpenzgyV1Ancestry": ".dataset_openzgy_v1ancestry",
    "DatasetOpenzgyV1Data": ".dataset_openzgy_v1data",
    "DatasetOpenzgyV1DataDatasetProperties": ".dataset_openzgy_v1data_dataset_properties",
    "DatasetOpenzgyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_openzgy_v1data_dataset_properties_file_source_infos_item",
    "DatasetOpenzgyV1DataEndian": ".dataset_openzgy_v1data_endian",
    "DatasetOpenzgyV1Legal": ".dataset_openzgy_v1legal",
    "DatasetOpenzgyV1MetaItem": ".dataset_openzgy_v1meta_item",
    "DatasetOpenzgyV1MetaItemCoordinateReferenceSystemId": ".dataset_openzgy_v1meta_item_coordinate_reference_system_id",
    "DatasetOpenzgyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_openzgy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetOpenzgyV1MetaItemThree": ".dataset_openzgy_v1meta_item_three",
    "DatasetOpenzgyV1MetaItemThreeKind": ".dataset_openzgy_v1meta_item_three_kind",
    "DatasetOpenzgyV1MetaItemTwo": ".dataset_openzgy_v1meta_item_two",
    "DatasetOpenzgyV1MetaItemTwoKind": ".dataset_openzgy_v1meta_item_two_kind",
    "DatasetOpenzgyV1MetaItemUnitOfMeasureId": ".dataset_openzgy_v1meta_item_unit_of_measure_id",
    "DatasetOpenzgyV1MetaItemUnitOfMeasureIdKind": ".dataset_openzgy_v1meta_item_unit_of_measure_id_kind",
    "DatasetPermission": ".dataset_permission",
    "DatasetSegyV1": ".dataset_segy_v1",
    "DatasetSegyV1Acl": ".dataset_segy_v1acl",
    "DatasetSegyV1Ancestry": ".dataset_segy_v1ancestry",
    "DatasetSegyV1Data": ".dataset_segy_v1data",
    "DatasetSegyV1DataDatasetProperties": ".dataset_segy_v1data_dataset_properties",
    "DatasetSegyV1DataDatasetPropertiesFileSourceInfosItem": ".dataset_segy_v1data_dataset_properties_file_source_infos_item",
    "DatasetSegyV1DataEndian": ".dataset_segy_v1data_endian",
    "DatasetSegyV1DataVectorHeaderMappingItem": ".dataset_segy_v1data_vector_header_mapping_item",
    "DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator": ".dataset_segy_v1data_vector_header_mapping_item_scalar_indicator",
    "DatasetSegyV1Legal": ".dataset_segy_v1legal",
    "DatasetSegyV1MetaItem": ".dataset_segy_v1meta_item",
    "DatasetSegyV1MetaItemCoordinateReferenceSystemId": ".dataset_segy_v1meta_item_coordinate_reference_system_id",
    "DatasetSegyV1MetaItemCoordinateReferenceSystemIdKind": ".dataset_segy_v1meta_item_coordinate_reference_system_id_kind",
    "DatasetSegyV1MetaItemThree": ".dataset_segy_v1meta_item_three",
    "DatasetSegyV1MetaItemThreeKind": ".dataset_segy_v1meta_item_three_kind",
    "DatasetSegyV1MetaItemTwo": ".dataset_segy_v1meta_item_two",
    "DatasetSegyV1MetaItemTwoKind": ".dataset_segy_v1meta_item_two_kind",
    "DatasetSegyV1MetaItemUnitOfMeasureId": ".dataset_segy_v1meta_item_unit_of_measure_id",
    "DatasetSegyV1MetaItemUnitOfMeasureIdKind": ".dataset_segy_v1meta_item_unit_of_measure_id_kind",
    "DatasetSeismicmeta": ".dataset_seismicmeta",
    "DatasetSize": ".dataset_size",
    "ImpersonationToken": ".impersonation_token",
    "LsDatasets": ".ls_datasets",
    "LsPaginatedDatasets": ".ls_paginated_datasets",
    "PaginatedDatasets": ".paginated_datasets",
    "Resource": ".resource",
    "Status": ".status",
    "SubProject": ".sub_project",
    "SubProjectAccessPolicy": ".sub_project_access_policy",
    "SubProjectAcls": ".sub_project_acls",
    "Tenant": ".tenant",
    "UserRemoveRequest": ".user_remove_request",
    "UserRoles": ".user_roles",
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
    "AccessToken",
    "Dataset",
    "DatasetAndDirectories",
    "DatasetCheckList",
    "DatasetOpenzgyV1",
    "DatasetOpenzgyV1Acl",
    "DatasetOpenzgyV1Ancestry",
    "DatasetOpenzgyV1Data",
    "DatasetOpenzgyV1DataDatasetProperties",
    "DatasetOpenzgyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetOpenzgyV1DataEndian",
    "DatasetOpenzgyV1Legal",
    "DatasetOpenzgyV1MetaItem",
    "DatasetOpenzgyV1MetaItemCoordinateReferenceSystemId",
    "DatasetOpenzgyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetOpenzgyV1MetaItemThree",
    "DatasetOpenzgyV1MetaItemThreeKind",
    "DatasetOpenzgyV1MetaItemTwo",
    "DatasetOpenzgyV1MetaItemTwoKind",
    "DatasetOpenzgyV1MetaItemUnitOfMeasureId",
    "DatasetOpenzgyV1MetaItemUnitOfMeasureIdKind",
    "DatasetPermission",
    "DatasetSegyV1",
    "DatasetSegyV1Acl",
    "DatasetSegyV1Ancestry",
    "DatasetSegyV1Data",
    "DatasetSegyV1DataDatasetProperties",
    "DatasetSegyV1DataDatasetPropertiesFileSourceInfosItem",
    "DatasetSegyV1DataEndian",
    "DatasetSegyV1DataVectorHeaderMappingItem",
    "DatasetSegyV1DataVectorHeaderMappingItemScalarIndicator",
    "DatasetSegyV1Legal",
    "DatasetSegyV1MetaItem",
    "DatasetSegyV1MetaItemCoordinateReferenceSystemId",
    "DatasetSegyV1MetaItemCoordinateReferenceSystemIdKind",
    "DatasetSegyV1MetaItemThree",
    "DatasetSegyV1MetaItemThreeKind",
    "DatasetSegyV1MetaItemTwo",
    "DatasetSegyV1MetaItemTwoKind",
    "DatasetSegyV1MetaItemUnitOfMeasureId",
    "DatasetSegyV1MetaItemUnitOfMeasureIdKind",
    "DatasetSeismicmeta",
    "DatasetSize",
    "ImpersonationToken",
    "LsDatasets",
    "LsPaginatedDatasets",
    "PaginatedDatasets",
    "Resource",
    "Status",
    "SubProject",
    "SubProjectAccessPolicy",
    "SubProjectAcls",
    "Tenant",
    "UserRemoveRequest",
    "UserRoles",
]
