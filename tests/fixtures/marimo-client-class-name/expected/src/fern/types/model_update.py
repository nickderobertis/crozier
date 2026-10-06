

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base64string import Base64String
from .esm_spec import EsmSpec
from .model_update_buffer_paths_item_item import ModelUpdateBufferPathsItemItem
from .model_update_method import ModelUpdateMethod


class ModelUpdate(UniversalBaseModel):
    """
    State sync - changed traits only.

        Attributes:
            state: Changed trait values, minus `_esm` (see `ModelOpen`).
            buffer_paths: Paths into `state` whose binary values were
                extracted into `buffers`.
            buffers: Binary payloads, parallel to `buffer_paths`.
            esm_spec: Present only when the widget's `_esm` changed on a
                live model (hot reload, edit mode only). A spec whose
                `hash` differs from the current one tells the frontend the
                widget's code changed and views must be rebuilt.
    """

    buffer_paths: typing.List[typing.List[ModelUpdateBufferPathsItemItem]]
    buffers: typing.List[Base64String]
    esm_spec: typing.Optional[EsmSpec] = None
    method: ModelUpdateMethod
    state: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
