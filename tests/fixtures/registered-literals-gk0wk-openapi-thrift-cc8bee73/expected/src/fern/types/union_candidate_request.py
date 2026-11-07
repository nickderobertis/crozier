

import typing

from .mutation_nullable_response import MutationNullableResponse
from .mutation_union_payload import MutationUnionPayload

UnionCandidateRequest = typing.Union[MutationUnionPayload, MutationNullableResponse]
