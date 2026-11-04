

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .inference_model2vec_custom_model2vec_custom import InferenceModel2VecCustomModel2VecCustom


class InferenceModel2VecCustom(UniversalBaseModel):
    """
    Custom model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.
    """

    model2vec_custom: typing_extensions.Annotated[
        InferenceModel2VecCustomModel2VecCustom,
        FieldMetadata(alias="Model2VecCustom"),
        pydantic.Field(
            alias="Model2VecCustom",
            description="Custom model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.",
        ),
    ]
    """
    Custom model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
