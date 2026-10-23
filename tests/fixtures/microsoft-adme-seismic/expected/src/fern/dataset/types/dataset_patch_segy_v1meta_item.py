

import typing

from .dataset_patch_segy_v1meta_item_coordinate_reference_system_id import (
    DatasetPatchSegyV1MetaItemCoordinateReferenceSystemId,
)
from .dataset_patch_segy_v1meta_item_three import DatasetPatchSegyV1MetaItemThree
from .dataset_patch_segy_v1meta_item_two import DatasetPatchSegyV1MetaItemTwo
from .dataset_patch_segy_v1meta_item_unit_of_measure_id import DatasetPatchSegyV1MetaItemUnitOfMeasureId

DatasetPatchSegyV1MetaItem = typing.Union[
    DatasetPatchSegyV1MetaItemUnitOfMeasureId,
    DatasetPatchSegyV1MetaItemCoordinateReferenceSystemId,
    DatasetPatchSegyV1MetaItemTwo,
    DatasetPatchSegyV1MetaItemThree,
]
