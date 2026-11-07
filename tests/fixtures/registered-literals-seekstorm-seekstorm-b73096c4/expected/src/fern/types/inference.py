

import typing

from .inference_external import InferenceExternal
from .inference_model2vec import InferenceModel2Vec
from .inference_model2vec_custom import InferenceModel2VecCustom
from .inference_three import InferenceThree

Inference = typing.Union[InferenceModel2Vec, InferenceModel2VecCustom, InferenceExternal, InferenceThree]
