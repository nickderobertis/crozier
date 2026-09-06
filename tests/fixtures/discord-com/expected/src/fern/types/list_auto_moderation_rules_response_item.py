

import typing

from .default_keyword_rule_response import DefaultKeywordRuleResponse
from .keyword_rule_response import KeywordRuleResponse
from .mention_spam_rule_response import MentionSpamRuleResponse
from .ml_spam_rule_response import MlSpamRuleResponse
from .spam_link_rule_response import SpamLinkRuleResponse

ListAutoModerationRulesResponseItem = typing.Union[
    DefaultKeywordRuleResponse, KeywordRuleResponse, MlSpamRuleResponse, MentionSpamRuleResponse, SpamLinkRuleResponse
]
