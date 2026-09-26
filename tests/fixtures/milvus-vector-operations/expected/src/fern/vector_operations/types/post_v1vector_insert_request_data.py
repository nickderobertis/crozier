

import typing

from .post_v1vector_insert_request_data_one_item import PostV1VectorInsertRequestDataOneItem
from .post_v1vector_insert_request_data_zero import PostV1VectorInsertRequestDataZero

PostV1VectorInsertRequestData = typing.Union[
    PostV1VectorInsertRequestDataZero, typing.List[PostV1VectorInsertRequestDataOneItem]
]
