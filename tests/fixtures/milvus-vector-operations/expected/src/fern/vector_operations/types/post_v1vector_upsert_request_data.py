

import typing

from .post_v1vector_upsert_request_data_one_item import PostV1VectorUpsertRequestDataOneItem
from .post_v1vector_upsert_request_data_zero import PostV1VectorUpsertRequestDataZero

PostV1VectorUpsertRequestData = typing.Union[
    PostV1VectorUpsertRequestDataZero, typing.List[PostV1VectorUpsertRequestDataOneItem]
]
