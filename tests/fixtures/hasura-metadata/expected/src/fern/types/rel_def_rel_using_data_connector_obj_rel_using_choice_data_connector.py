

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rel_def_rel_using_data_connector_obj_rel_using_choice_data_connector_using import (
    RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnectorUsing,
)


class RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnector(UniversalBaseModel):
    comment: typing.Optional[str] = None
    name: str
    using: RelDefRelUsingDataConnectorObjRelUsingChoiceDataConnectorUsing

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
