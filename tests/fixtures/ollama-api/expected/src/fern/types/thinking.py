

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thinking_default import ThinkingDefault
from .thinking_values_item import ThinkingValuesItem


class Thinking(UniversalBaseModel):
    """
    Thinking controls advertised by a model. Models without thinking metadata omit this field.
    """

    values: typing.List[ThinkingValuesItem] = pydantic.Field()
    """
    Values explicitly supported by the model's `think` request field. Booleans represent on/off controls and strings represent model-defined levels. An array containing only `false` identifies a model without thinking support.
    """

    default: ThinkingDefault = pydantic.Field()
    """
    Value used when `think` is not set. For models that use this metadata for named thinking levels, unsupported names resolve to this default.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
