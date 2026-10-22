

import typing

from .dataset_segy_v1meta_item_coordinate_reference_system_id import DatasetSegyV1MetaItemCoordinateReferenceSystemId
from .dataset_segy_v1meta_item_three import DatasetSegyV1MetaItemThree
from .dataset_segy_v1meta_item_two import DatasetSegyV1MetaItemTwo
from .dataset_segy_v1meta_item_unit_of_measure_id import DatasetSegyV1MetaItemUnitOfMeasureId

DatasetSegyV1MetaItem = typing.Union[
    DatasetSegyV1MetaItemUnitOfMeasureId,
    DatasetSegyV1MetaItemCoordinateReferenceSystemId,
    DatasetSegyV1MetaItemTwo,
    DatasetSegyV1MetaItemThree,
]
