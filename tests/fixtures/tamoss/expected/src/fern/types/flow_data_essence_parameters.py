

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FlowDataEssenceParameters(UniversalBaseModel):
    """
    Describes the parameters of the essence inside this data Flow
    """

    data_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of information encoded in the Flow, identified using a URN. e.g. The data_type may be urn:x-tams:data:bounding-box, and the codec `application/json`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
