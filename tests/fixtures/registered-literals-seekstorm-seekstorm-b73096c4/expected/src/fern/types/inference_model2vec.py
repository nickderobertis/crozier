

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .inference_model2vec_model2vec import InferenceModel2VecModel2Vec


class InferenceModel2Vec(UniversalBaseModel):
    """
    Predefined model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.
    """

    model2vec: typing_extensions.Annotated[
        InferenceModel2VecModel2Vec,
        FieldMetadata(alias="Model2Vec"),
        pydantic.Field(
            alias="Model2Vec",
            description="Predefined model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.",
        ),
    ]
    """
    Predefined model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
