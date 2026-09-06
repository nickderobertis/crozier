

import typing

from .default_keyword_list_upsert_request import DefaultKeywordListUpsertRequest
from .keyword_upsert_request import KeywordUpsertRequest
from .mention_spam_upsert_request import MentionSpamUpsertRequest
from .ml_spam_upsert_request import MlSpamUpsertRequest

CreateAutoModerationRuleRequestBody = typing.Union[
    DefaultKeywordListUpsertRequest, KeywordUpsertRequest, MlSpamUpsertRequest, MentionSpamUpsertRequest
]
