

import typing

from .query_rewriting_search_rewrite import QueryRewritingSearchRewrite
from .query_rewriting_search_suggest import QueryRewritingSearchSuggest
from .query_rewriting_suggest_only import QueryRewritingSuggestOnly
from .query_rewriting_zero import QueryRewritingZero

QueryRewriting = typing.Union[
    QueryRewritingZero, QueryRewritingSearchSuggest, QueryRewritingSearchRewrite, QueryRewritingSuggestOnly
]
