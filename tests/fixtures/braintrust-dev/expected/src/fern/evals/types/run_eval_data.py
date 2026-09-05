

import typing

from .run_eval_data_data import RunEvalDataData
from .run_eval_data_dataset_id import RunEvalDataDatasetId
from .run_eval_data_dataset_name import RunEvalDataDatasetName

RunEvalData = typing.Union[RunEvalDataDatasetId, RunEvalDataDatasetName, RunEvalDataData]
