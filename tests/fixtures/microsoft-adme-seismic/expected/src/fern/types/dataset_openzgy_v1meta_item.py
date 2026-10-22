

import typing

from .dataset_openzgy_v1meta_item_coordinate_reference_system_id import (
    DatasetOpenzgyV1MetaItemCoordinateReferenceSystemId,
)
from .dataset_openzgy_v1meta_item_three import DatasetOpenzgyV1MetaItemThree
from .dataset_openzgy_v1meta_item_two import DatasetOpenzgyV1MetaItemTwo
from .dataset_openzgy_v1meta_item_unit_of_measure_id import DatasetOpenzgyV1MetaItemUnitOfMeasureId

DatasetOpenzgyV1MetaItem = typing.Union[
    DatasetOpenzgyV1MetaItemUnitOfMeasureId,
    DatasetOpenzgyV1MetaItemCoordinateReferenceSystemId,
    DatasetOpenzgyV1MetaItemTwo,
    DatasetOpenzgyV1MetaItemThree,
]
