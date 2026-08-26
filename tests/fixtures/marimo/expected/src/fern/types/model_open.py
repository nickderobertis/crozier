

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base64string import Base64String
from .esm_spec import EsmSpec
from .model_open_buffer_paths_item_item import ModelOpenBufferPathsItemItem
from .model_open_method import ModelOpenMethod


class ModelOpen(UniversalBaseModel):
    """
    Initial widget state on creation.

        For anywidgets, the widget's ESM does not travel in `state`: the
        comm strips `_esm` and sends an `EsmSpec` instead. `None` for
        models with no ESM (e.g. traditional ipywidgets).

        Attributes:
            state: Initial trait values, minus `_esm`.
            buffer_paths: Paths into `state` whose binary values were
                extracted into `buffers`.
            buffers: Binary payloads, parallel to `buffer_paths`.
            esm_spec: Where to import this widget's ESM from.
    """

    buffer_paths: typing.List[typing.List[ModelOpenBufferPathsItemItem]]
    buffers: typing.List[Base64String]
    esm_spec: typing.Optional[EsmSpec] = None
    method: ModelOpenMethod
    state: typing.Dict[str, typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
