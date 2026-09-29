



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apple_session_request import AppleSessionRequest
    from .apple_session_request_user import AppleSessionRequestUser
    from .apple_session_request_user_name import AppleSessionRequestUserName
    from .apple_subscription_response import AppleSubscriptionResponse
    from .catalog_search_response import CatalogSearchResponse
    from .catalog_search_response_chapters_item import CatalogSearchResponseChaptersItem
    from .catalog_search_response_courses_item import CatalogSearchResponseCoursesItem
    from .chapter_completion_response import ChapterCompletionResponse
    from .chapter_completion_response_lessons_item import ChapterCompletionResponseLessonsItem
    from .chapter_lesson_list_response import ChapterLessonListResponse
    from .chapter_resource import ChapterResource
    from .chapter_resource_generation_status import ChapterResourceGenerationStatus
    from .course_chapter import CourseChapter
    from .course_chapter_generation_status import CourseChapterGenerationStatus
    from .course_chapter_list_response import CourseChapterListResponse
    from .course_completion_response import CourseCompletionResponse
    from .course_completion_response_chapters_item import CourseCompletionResponseChaptersItem
    from .course_continuation import CourseContinuation, CourseContinuation_Pending, CourseContinuation_Ready
    from .course_continuation_list_response import CourseContinuationListResponse
    from .course_continuation_pending import CourseContinuationPending
    from .course_continuation_pending_chapter import CourseContinuationPendingChapter
    from .course_continuation_pending_course import CourseContinuationPendingCourse
    from .course_continuation_pending_course_organization import CourseContinuationPendingCourseOrganization
    from .course_continuation_pending_lesson import CourseContinuationPendingLesson
    from .course_continuation_pending_lesson_kind import CourseContinuationPendingLessonKind
    from .course_continuation_ready import CourseContinuationReady
    from .course_continuation_ready_chapter import CourseContinuationReadyChapter
    from .course_continuation_ready_course import CourseContinuationReadyCourse
    from .course_continuation_ready_course_organization import CourseContinuationReadyCourseOrganization
    from .course_continuation_ready_lesson import CourseContinuationReadyLesson
    from .course_continuation_ready_lesson_kind import CourseContinuationReadyLessonKind
    from .course_edition_response import (
        CourseEditionResponse,
        CourseEditionResponse_Course,
        CourseEditionResponse_Generation,
        CourseEditionResponse_Missing,
        CourseEditionResponse_Unsupported,
    )
    from .course_edition_response_course import CourseEditionResponseCourse
    from .course_edition_response_generation import CourseEditionResponseGeneration
    from .course_edition_response_generation_generation_status import CourseEditionResponseGenerationGenerationStatus
    from .course_edition_response_missing import CourseEditionResponseMissing
    from .course_edition_response_unsupported import CourseEditionResponseUnsupported
    from .course_edition_response_unsupported_reason import CourseEditionResponseUnsupportedReason
    from .course_prompt_generation_response import (
        CoursePromptGenerationResponse,
        CoursePromptGenerationResponse_Pending,
        CoursePromptGenerationResponse_Ready,
    )
    from .course_prompt_generation_response_pending import CoursePromptGenerationResponsePending
    from .course_prompt_generation_response_pending_completion_kind import (
        CoursePromptGenerationResponsePendingCompletionKind,
    )
    from .course_prompt_generation_response_pending_course_format import (
        CoursePromptGenerationResponsePendingCourseFormat,
    )
    from .course_prompt_generation_response_pending_generation_status import (
        CoursePromptGenerationResponsePendingGenerationStatus,
    )
    from .course_prompt_generation_response_ready import CoursePromptGenerationResponseReady
    from .course_prompt_generation_response_ready_target import (
        CoursePromptGenerationResponseReadyTarget,
        CoursePromptGenerationResponseReadyTarget_Course,
        CoursePromptGenerationResponseReadyTarget_Lesson,
    )
    from .course_prompt_generation_response_ready_target_course import CoursePromptGenerationResponseReadyTargetCourse
    from .course_prompt_generation_response_ready_target_lesson import CoursePromptGenerationResponseReadyTargetLesson
    from .course_resource import CourseResource
    from .course_resource_categories_item import CourseResourceCategoriesItem
    from .course_resource_format import CourseResourceFormat
    from .course_resource_generation_status import CourseResourceGenerationStatus
    from .course_result import CourseResult
    from .current_user_activity_response import CurrentUserActivityResponse
    from .current_user_activity_response_activity import CurrentUserActivityResponseActivity
    from .current_user_activity_response_activity_days_item import CurrentUserActivityResponseActivityDaysItem
    from .current_user_course import CurrentUserCourse
    from .current_user_course_list_response import CurrentUserCourseListResponse
    from .current_user_energy_response import CurrentUserEnergyResponse
    from .current_user_energy_response_energy import CurrentUserEnergyResponseEnergy
    from .current_user_energy_response_energy_days_item import CurrentUserEnergyResponseEnergyDaysItem
    from .current_user_energy_response_energy_insights import CurrentUserEnergyResponseEnergyInsights
    from .current_user_level_response import CurrentUserLevelResponse
    from .current_user_level_response_level import CurrentUserLevelResponseLevel
    from .current_user_level_response_level_belt import CurrentUserLevelResponseLevelBelt
    from .current_user_progress_response import CurrentUserProgressResponse
    from .current_user_progress_response_activity import CurrentUserProgressResponseActivity
    from .current_user_progress_response_energy import CurrentUserProgressResponseEnergy
    from .current_user_progress_response_level import CurrentUserProgressResponseLevel
    from .current_user_progress_response_level_belt import CurrentUserProgressResponseLevelBelt
    from .current_user_progress_response_score import CurrentUserProgressResponseScore
    from .current_user_progress_response_score_patterns import CurrentUserProgressResponseScorePatterns
    from .current_user_progress_response_score_patterns_strongest_time import (
        CurrentUserProgressResponseScorePatternsStrongestTime,
    )
    from .current_user_progress_response_score_patterns_strongest_time_period import (
        CurrentUserProgressResponseScorePatternsStrongestTimePeriod,
    )
    from .current_user_progress_response_score_patterns_strongest_weekday import (
        CurrentUserProgressResponseScorePatternsStrongestWeekday,
    )
    from .current_user_progress_response_score_patterns_strongest_weekday_day_of_week import (
        CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek,
    )
    from .current_user_progress_snapshot_response import CurrentUserProgressSnapshotResponse
    from .current_user_progress_snapshot_response_snapshot import CurrentUserProgressSnapshotResponseSnapshot
    from .current_user_progress_snapshot_response_snapshot_progress_snapshot import (
        CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot,
    )
    from .current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item import (
        CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem,
    )
    from .current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item_day_of_week import (
        CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek,
    )
    from .current_user_score_patterns_response import CurrentUserScorePatternsResponse
    from .current_user_score_patterns_response_patterns import CurrentUserScorePatternsResponsePatterns
    from .current_user_score_patterns_response_patterns_strongest_time import (
        CurrentUserScorePatternsResponsePatternsStrongestTime,
    )
    from .current_user_score_patterns_response_patterns_strongest_time_period import (
        CurrentUserScorePatternsResponsePatternsStrongestTimePeriod,
    )
    from .current_user_score_patterns_response_patterns_strongest_weekday import (
        CurrentUserScorePatternsResponsePatternsStrongestWeekday,
    )
    from .current_user_score_patterns_response_patterns_strongest_weekday_day_of_week import (
        CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek,
    )
    from .current_user_score_patterns_response_patterns_times_item import (
        CurrentUserScorePatternsResponsePatternsTimesItem,
    )
    from .current_user_score_patterns_response_patterns_times_item_period import (
        CurrentUserScorePatternsResponsePatternsTimesItemPeriod,
    )
    from .current_user_score_patterns_response_patterns_weekdays_item import (
        CurrentUserScorePatternsResponsePatternsWeekdaysItem,
    )
    from .current_user_score_patterns_response_patterns_weekdays_item_day_of_week import (
        CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek,
    )
    from .current_user_score_response import CurrentUserScoreResponse
    from .current_user_score_response_score import CurrentUserScoreResponseScore
    from .current_user_score_response_score_data_points_item import CurrentUserScoreResponseScoreDataPointsItem
    from .email_account_deletion_credentials import EmailAccountDeletionCredentials
    from .error import Error
    from .error_error import ErrorError
    from .feedback_response import FeedbackResponse
    from .generation import Generation
    from .generation_status import GenerationStatus
    from .generation_target import GenerationTarget
    from .generation_target_type import GenerationTargetType
    from .language_course import LanguageCourse
    from .language_course_list_response import LanguageCourseListResponse
    from .language_course_target_language import LanguageCourseTargetLanguage
    from .lesson_completion_response import LessonCompletionResponse
    from .lesson_completion_response_belt import LessonCompletionResponseBelt
    from .lesson_content_response import (
        LessonContentResponse,
        LessonContentResponse_NotGenerated,
        LessonContentResponse_Ready,
        LessonContentResponse_ReviewEmpty,
    )
    from .lesson_content_response_not_generated import LessonContentResponseNotGenerated
    from .lesson_content_response_ready import LessonContentResponseReady
    from .lesson_content_response_ready_lesson import LessonContentResponseReadyLesson
    from .lesson_content_response_ready_lesson_kind import LessonContentResponseReadyLessonKind
    from .lesson_content_response_ready_lesson_lesson_sentences_item import (
        LessonContentResponseReadyLessonLessonSentencesItem,
    )
    from .lesson_content_response_ready_lesson_lesson_words_item import LessonContentResponseReadyLessonLessonWordsItem
    from .lesson_content_response_ready_lesson_steps_item import LessonContentResponseReadyLessonStepsItem
    from .lesson_content_response_ready_lesson_steps_item_fill_blank_options_item import (
        LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem,
    )
    from .lesson_content_response_ready_lesson_steps_item_sentence import (
        LessonContentResponseReadyLessonStepsItemSentence,
    )
    from .lesson_content_response_ready_lesson_steps_item_sentence_word_options_item import (
        LessonContentResponseReadyLessonStepsItemSentenceWordOptionsItem,
    )
    from .lesson_content_response_ready_lesson_steps_item_translation_options_item import (
        LessonContentResponseReadyLessonStepsItemTranslationOptionsItem,
    )
    from .lesson_content_response_ready_lesson_steps_item_vocabulary_options_item import (
        LessonContentResponseReadyLessonStepsItemVocabularyOptionsItem,
    )
    from .lesson_content_response_ready_lesson_steps_item_word import LessonContentResponseReadyLessonStepsItemWord
    from .lesson_content_response_ready_lesson_steps_item_word_bank_options_item import (
        LessonContentResponseReadyLessonStepsItemWordBankOptionsItem,
    )
    from .lesson_content_response_review_empty import LessonContentResponseReviewEmpty
    from .lesson_generation_target import LessonGenerationTarget
    from .lesson_generation_target_kind import LessonGenerationTargetKind
    from .lesson_preload_response import LessonPreloadResponse
    from .lesson_preload_response_generations_item import (
        LessonPreloadResponseGenerationsItem,
        LessonPreloadResponseGenerationsItem_Chapter,
        LessonPreloadResponseGenerationsItem_Lesson,
    )
    from .lesson_preload_response_generations_item_chapter import LessonPreloadResponseGenerationsItemChapter
    from .lesson_preload_response_generations_item_lesson import LessonPreloadResponseGenerationsItemLesson
    from .lesson_question import LessonQuestion
    from .lesson_question_context import (
        LessonQuestionContext,
        LessonQuestionContext_Answer,
        LessonQuestionContext_Lesson,
        LessonQuestionContext_Step,
    )
    from .lesson_question_context_answer import LessonQuestionContextAnswer
    from .lesson_question_context_input import (
        LessonQuestionContextInput,
        LessonQuestionContextInput_Answer,
        LessonQuestionContextInput_Lesson,
        LessonQuestionContextInput_Step,
    )
    from .lesson_question_context_input_answer import LessonQuestionContextInputAnswer
    from .lesson_question_context_input_answer_answer import (
        LessonQuestionContextInputAnswerAnswer,
        LessonQuestionContextInputAnswerAnswer_FillBlank,
        LessonQuestionContextInputAnswerAnswer_Listening,
        LessonQuestionContextInputAnswerAnswer_MatchColumns,
        LessonQuestionContextInputAnswerAnswer_MultipleChoice,
        LessonQuestionContextInputAnswerAnswer_Reading,
        LessonQuestionContextInputAnswerAnswer_SelectImage,
        LessonQuestionContextInputAnswerAnswer_SortOrder,
        LessonQuestionContextInputAnswerAnswer_Translation,
    )
    from .lesson_question_context_input_answer_answer_fill_blank import LessonQuestionContextInputAnswerAnswerFillBlank
    from .lesson_question_context_input_answer_answer_listening import LessonQuestionContextInputAnswerAnswerListening
    from .lesson_question_context_input_answer_answer_match_columns import (
        LessonQuestionContextInputAnswerAnswerMatchColumns,
    )
    from .lesson_question_context_input_answer_answer_match_columns_user_pairs_item import (
        LessonQuestionContextInputAnswerAnswerMatchColumnsUserPairsItem,
    )
    from .lesson_question_context_input_answer_answer_multiple_choice import (
        LessonQuestionContextInputAnswerAnswerMultipleChoice,
    )
    from .lesson_question_context_input_answer_answer_reading import LessonQuestionContextInputAnswerAnswerReading
    from .lesson_question_context_input_answer_answer_select_image import (
        LessonQuestionContextInputAnswerAnswerSelectImage,
    )
    from .lesson_question_context_input_answer_answer_sort_order import LessonQuestionContextInputAnswerAnswerSortOrder
    from .lesson_question_context_input_answer_answer_translation import (
        LessonQuestionContextInputAnswerAnswerTranslation,
    )
    from .lesson_question_context_input_lesson import LessonQuestionContextInputLesson
    from .lesson_question_context_input_step import LessonQuestionContextInputStep
    from .lesson_question_context_lesson import LessonQuestionContextLesson
    from .lesson_question_context_step import LessonQuestionContextStep
    from .lesson_question_status import LessonQuestionStatus
    from .lesson_question_thread import LessonQuestionThread
    from .lesson_resource import LessonResource
    from .lesson_resource_generation_status import LessonResourceGenerationStatus
    from .lesson_resource_kind import LessonResourceKind
    from .lesson_successor_response import LessonSuccessorResponse
    from .lesson_successor_response_lesson import LessonSuccessorResponseLesson
    from .lesson_successor_response_lesson_lesson_generation_status import (
        LessonSuccessorResponseLessonLessonGenerationStatus,
    )
    from .lesson_successor_response_lesson_lesson_kind import LessonSuccessorResponseLessonLessonKind
    from .lesson_visibility import LessonVisibility
    from .lesson_visibility_hidden_lesson_kinds_item import LessonVisibilityHiddenLessonKindsItem
    from .lesson_visibility_output import LessonVisibilityOutput
    from .lesson_visibility_output_hidden_lesson_kinds_item import LessonVisibilityOutputHiddenLessonKindsItem
    from .lesson_visibility_update import LessonVisibilityUpdate
    from .me_deletion import MeDeletion
    from .me_deletion_apple_credentials import MeDeletionAppleCredentials
    from .me_deletion_email_credentials import MeDeletionEmailCredentials
    from .me_deletion_response import MeDeletionResponse
    from .me_deletion_zero import MeDeletionZero
    from .me_response import MeResponse
    from .me_response_account import MeResponseAccount
    from .me_response_account_deletion import MeResponseAccountDeletion
    from .me_subscription import MeSubscription
    from .me_user import MeUser
    from .next_lesson_chapter_response import NextLessonChapterResponse
    from .next_lesson_empty_response import NextLessonEmptyResponse
    from .next_lesson_lesson_response import NextLessonLessonResponse
    from .next_lesson_response import (
        NextLessonResponse,
        NextLessonResponse_Chapter,
        NextLessonResponse_Empty,
        NextLessonResponse_Lesson,
    )
    from .organization_summary import OrganizationSummary
    from .pagination import Pagination
    from .resolve_course_prompt_request import (
        ResolveCoursePromptRequest,
        ResolveCoursePromptRequest_Language,
        ResolveCoursePromptRequest_Topic,
    )
    from .resolve_course_prompt_request_language import ResolveCoursePromptRequestLanguage
    from .resolve_course_prompt_request_language_target_language import ResolveCoursePromptRequestLanguageTargetLanguage
    from .resolve_course_prompt_request_topic import ResolveCoursePromptRequestTopic
    from .resolve_course_prompt_response import (
        ResolveCoursePromptResponse,
        ResolveCoursePromptResponse_Course,
        ResolveCoursePromptResponse_Exam,
        ResolveCoursePromptResponse_Generation,
        ResolveCoursePromptResponse_Language,
        ResolveCoursePromptResponse_Unsafe,
        ResolveCoursePromptResponse_Unsupported,
    )
    from .resolve_course_prompt_response_course import ResolveCoursePromptResponseCourse
    from .resolve_course_prompt_response_exam import ResolveCoursePromptResponseExam
    from .resolve_course_prompt_response_generation import ResolveCoursePromptResponseGeneration
    from .resolve_course_prompt_response_language import ResolveCoursePromptResponseLanguage
    from .resolve_course_prompt_response_unsafe import ResolveCoursePromptResponseUnsafe
    from .resolve_course_prompt_response_unsupported import ResolveCoursePromptResponseUnsupported
    from .resolve_course_prompt_response_unsupported_course_format import (
        ResolveCoursePromptResponseUnsupportedCourseFormat,
    )
    from .resolve_course_prompt_response_unsupported_intent import ResolveCoursePromptResponseUnsupportedIntent
    from .session_token_response import SessionTokenResponse
    from .username_availability_response import UsernameAvailabilityResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AppleSessionRequest": ".apple_session_request",
    "AppleSessionRequestUser": ".apple_session_request_user",
    "AppleSessionRequestUserName": ".apple_session_request_user_name",
    "AppleSubscriptionResponse": ".apple_subscription_response",
    "CatalogSearchResponse": ".catalog_search_response",
    "CatalogSearchResponseChaptersItem": ".catalog_search_response_chapters_item",
    "CatalogSearchResponseCoursesItem": ".catalog_search_response_courses_item",
    "ChapterCompletionResponse": ".chapter_completion_response",
    "ChapterCompletionResponseLessonsItem": ".chapter_completion_response_lessons_item",
    "ChapterLessonListResponse": ".chapter_lesson_list_response",
    "ChapterResource": ".chapter_resource",
    "ChapterResourceGenerationStatus": ".chapter_resource_generation_status",
    "CourseChapter": ".course_chapter",
    "CourseChapterGenerationStatus": ".course_chapter_generation_status",
    "CourseChapterListResponse": ".course_chapter_list_response",
    "CourseCompletionResponse": ".course_completion_response",
    "CourseCompletionResponseChaptersItem": ".course_completion_response_chapters_item",
    "CourseContinuation": ".course_continuation",
    "CourseContinuationListResponse": ".course_continuation_list_response",
    "CourseContinuationPending": ".course_continuation_pending",
    "CourseContinuationPendingChapter": ".course_continuation_pending_chapter",
    "CourseContinuationPendingCourse": ".course_continuation_pending_course",
    "CourseContinuationPendingCourseOrganization": ".course_continuation_pending_course_organization",
    "CourseContinuationPendingLesson": ".course_continuation_pending_lesson",
    "CourseContinuationPendingLessonKind": ".course_continuation_pending_lesson_kind",
    "CourseContinuationReady": ".course_continuation_ready",
    "CourseContinuationReadyChapter": ".course_continuation_ready_chapter",
    "CourseContinuationReadyCourse": ".course_continuation_ready_course",
    "CourseContinuationReadyCourseOrganization": ".course_continuation_ready_course_organization",
    "CourseContinuationReadyLesson": ".course_continuation_ready_lesson",
    "CourseContinuationReadyLessonKind": ".course_continuation_ready_lesson_kind",
    "CourseContinuation_Pending": ".course_continuation",
    "CourseContinuation_Ready": ".course_continuation",
    "CourseEditionResponse": ".course_edition_response",
    "CourseEditionResponseCourse": ".course_edition_response_course",
    "CourseEditionResponseGeneration": ".course_edition_response_generation",
    "CourseEditionResponseGenerationGenerationStatus": ".course_edition_response_generation_generation_status",
    "CourseEditionResponseMissing": ".course_edition_response_missing",
    "CourseEditionResponseUnsupported": ".course_edition_response_unsupported",
    "CourseEditionResponseUnsupportedReason": ".course_edition_response_unsupported_reason",
    "CourseEditionResponse_Course": ".course_edition_response",
    "CourseEditionResponse_Generation": ".course_edition_response",
    "CourseEditionResponse_Missing": ".course_edition_response",
    "CourseEditionResponse_Unsupported": ".course_edition_response",
    "CoursePromptGenerationResponse": ".course_prompt_generation_response",
    "CoursePromptGenerationResponsePending": ".course_prompt_generation_response_pending",
    "CoursePromptGenerationResponsePendingCompletionKind": ".course_prompt_generation_response_pending_completion_kind",
    "CoursePromptGenerationResponsePendingCourseFormat": ".course_prompt_generation_response_pending_course_format",
    "CoursePromptGenerationResponsePendingGenerationStatus": ".course_prompt_generation_response_pending_generation_status",
    "CoursePromptGenerationResponseReady": ".course_prompt_generation_response_ready",
    "CoursePromptGenerationResponseReadyTarget": ".course_prompt_generation_response_ready_target",
    "CoursePromptGenerationResponseReadyTargetCourse": ".course_prompt_generation_response_ready_target_course",
    "CoursePromptGenerationResponseReadyTargetLesson": ".course_prompt_generation_response_ready_target_lesson",
    "CoursePromptGenerationResponseReadyTarget_Course": ".course_prompt_generation_response_ready_target",
    "CoursePromptGenerationResponseReadyTarget_Lesson": ".course_prompt_generation_response_ready_target",
    "CoursePromptGenerationResponse_Pending": ".course_prompt_generation_response",
    "CoursePromptGenerationResponse_Ready": ".course_prompt_generation_response",
    "CourseResource": ".course_resource",
    "CourseResourceCategoriesItem": ".course_resource_categories_item",
    "CourseResourceFormat": ".course_resource_format",
    "CourseResourceGenerationStatus": ".course_resource_generation_status",
    "CourseResult": ".course_result",
    "CurrentUserActivityResponse": ".current_user_activity_response",
    "CurrentUserActivityResponseActivity": ".current_user_activity_response_activity",
    "CurrentUserActivityResponseActivityDaysItem": ".current_user_activity_response_activity_days_item",
    "CurrentUserCourse": ".current_user_course",
    "CurrentUserCourseListResponse": ".current_user_course_list_response",
    "CurrentUserEnergyResponse": ".current_user_energy_response",
    "CurrentUserEnergyResponseEnergy": ".current_user_energy_response_energy",
    "CurrentUserEnergyResponseEnergyDaysItem": ".current_user_energy_response_energy_days_item",
    "CurrentUserEnergyResponseEnergyInsights": ".current_user_energy_response_energy_insights",
    "CurrentUserLevelResponse": ".current_user_level_response",
    "CurrentUserLevelResponseLevel": ".current_user_level_response_level",
    "CurrentUserLevelResponseLevelBelt": ".current_user_level_response_level_belt",
    "CurrentUserProgressResponse": ".current_user_progress_response",
    "CurrentUserProgressResponseActivity": ".current_user_progress_response_activity",
    "CurrentUserProgressResponseEnergy": ".current_user_progress_response_energy",
    "CurrentUserProgressResponseLevel": ".current_user_progress_response_level",
    "CurrentUserProgressResponseLevelBelt": ".current_user_progress_response_level_belt",
    "CurrentUserProgressResponseScore": ".current_user_progress_response_score",
    "CurrentUserProgressResponseScorePatterns": ".current_user_progress_response_score_patterns",
    "CurrentUserProgressResponseScorePatternsStrongestTime": ".current_user_progress_response_score_patterns_strongest_time",
    "CurrentUserProgressResponseScorePatternsStrongestTimePeriod": ".current_user_progress_response_score_patterns_strongest_time_period",
    "CurrentUserProgressResponseScorePatternsStrongestWeekday": ".current_user_progress_response_score_patterns_strongest_weekday",
    "CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek": ".current_user_progress_response_score_patterns_strongest_weekday_day_of_week",
    "CurrentUserProgressSnapshotResponse": ".current_user_progress_snapshot_response",
    "CurrentUserProgressSnapshotResponseSnapshot": ".current_user_progress_snapshot_response_snapshot",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot": ".current_user_progress_snapshot_response_snapshot_progress_snapshot",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem": ".current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek": ".current_user_progress_snapshot_response_snapshot_progress_snapshot_best_day_scores_item_day_of_week",
    "CurrentUserScorePatternsResponse": ".current_user_score_patterns_response",
    "CurrentUserScorePatternsResponsePatterns": ".current_user_score_patterns_response_patterns",
    "CurrentUserScorePatternsResponsePatternsStrongestTime": ".current_user_score_patterns_response_patterns_strongest_time",
    "CurrentUserScorePatternsResponsePatternsStrongestTimePeriod": ".current_user_score_patterns_response_patterns_strongest_time_period",
    "CurrentUserScorePatternsResponsePatternsStrongestWeekday": ".current_user_score_patterns_response_patterns_strongest_weekday",
    "CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek": ".current_user_score_patterns_response_patterns_strongest_weekday_day_of_week",
    "CurrentUserScorePatternsResponsePatternsTimesItem": ".current_user_score_patterns_response_patterns_times_item",
    "CurrentUserScorePatternsResponsePatternsTimesItemPeriod": ".current_user_score_patterns_response_patterns_times_item_period",
    "CurrentUserScorePatternsResponsePatternsWeekdaysItem": ".current_user_score_patterns_response_patterns_weekdays_item",
    "CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek": ".current_user_score_patterns_response_patterns_weekdays_item_day_of_week",
    "CurrentUserScoreResponse": ".current_user_score_response",
    "CurrentUserScoreResponseScore": ".current_user_score_response_score",
    "CurrentUserScoreResponseScoreDataPointsItem": ".current_user_score_response_score_data_points_item",
    "EmailAccountDeletionCredentials": ".email_account_deletion_credentials",
    "Error": ".error",
    "ErrorError": ".error_error",
    "FeedbackResponse": ".feedback_response",
    "Generation": ".generation",
    "GenerationStatus": ".generation_status",
    "GenerationTarget": ".generation_target",
    "GenerationTargetType": ".generation_target_type",
    "LanguageCourse": ".language_course",
    "LanguageCourseListResponse": ".language_course_list_response",
    "LanguageCourseTargetLanguage": ".language_course_target_language",
    "LessonCompletionResponse": ".lesson_completion_response",
    "LessonCompletionResponseBelt": ".lesson_completion_response_belt",
    "LessonContentResponse": ".lesson_content_response",
    "LessonContentResponseNotGenerated": ".lesson_content_response_not_generated",
    "LessonContentResponseReady": ".lesson_content_response_ready",
    "LessonContentResponseReadyLesson": ".lesson_content_response_ready_lesson",
    "LessonContentResponseReadyLessonKind": ".lesson_content_response_ready_lesson_kind",
    "LessonContentResponseReadyLessonLessonSentencesItem": ".lesson_content_response_ready_lesson_lesson_sentences_item",
    "LessonContentResponseReadyLessonLessonWordsItem": ".lesson_content_response_ready_lesson_lesson_words_item",
    "LessonContentResponseReadyLessonStepsItem": ".lesson_content_response_ready_lesson_steps_item",
    "LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem": ".lesson_content_response_ready_lesson_steps_item_fill_blank_options_item",
    "LessonContentResponseReadyLessonStepsItemSentence": ".lesson_content_response_ready_lesson_steps_item_sentence",
    "LessonContentResponseReadyLessonStepsItemSentenceWordOptionsItem": ".lesson_content_response_ready_lesson_steps_item_sentence_word_options_item",
    "LessonContentResponseReadyLessonStepsItemTranslationOptionsItem": ".lesson_content_response_ready_lesson_steps_item_translation_options_item",
    "LessonContentResponseReadyLessonStepsItemVocabularyOptionsItem": ".lesson_content_response_ready_lesson_steps_item_vocabulary_options_item",
    "LessonContentResponseReadyLessonStepsItemWord": ".lesson_content_response_ready_lesson_steps_item_word",
    "LessonContentResponseReadyLessonStepsItemWordBankOptionsItem": ".lesson_content_response_ready_lesson_steps_item_word_bank_options_item",
    "LessonContentResponseReviewEmpty": ".lesson_content_response_review_empty",
    "LessonContentResponse_NotGenerated": ".lesson_content_response",
    "LessonContentResponse_Ready": ".lesson_content_response",
    "LessonContentResponse_ReviewEmpty": ".lesson_content_response",
    "LessonGenerationTarget": ".lesson_generation_target",
    "LessonGenerationTargetKind": ".lesson_generation_target_kind",
    "LessonPreloadResponse": ".lesson_preload_response",
    "LessonPreloadResponseGenerationsItem": ".lesson_preload_response_generations_item",
    "LessonPreloadResponseGenerationsItemChapter": ".lesson_preload_response_generations_item_chapter",
    "LessonPreloadResponseGenerationsItemLesson": ".lesson_preload_response_generations_item_lesson",
    "LessonPreloadResponseGenerationsItem_Chapter": ".lesson_preload_response_generations_item",
    "LessonPreloadResponseGenerationsItem_Lesson": ".lesson_preload_response_generations_item",
    "LessonQuestion": ".lesson_question",
    "LessonQuestionContext": ".lesson_question_context",
    "LessonQuestionContextAnswer": ".lesson_question_context_answer",
    "LessonQuestionContextInput": ".lesson_question_context_input",
    "LessonQuestionContextInputAnswer": ".lesson_question_context_input_answer",
    "LessonQuestionContextInputAnswerAnswer": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswerFillBlank": ".lesson_question_context_input_answer_answer_fill_blank",
    "LessonQuestionContextInputAnswerAnswerListening": ".lesson_question_context_input_answer_answer_listening",
    "LessonQuestionContextInputAnswerAnswerMatchColumns": ".lesson_question_context_input_answer_answer_match_columns",
    "LessonQuestionContextInputAnswerAnswerMatchColumnsUserPairsItem": ".lesson_question_context_input_answer_answer_match_columns_user_pairs_item",
    "LessonQuestionContextInputAnswerAnswerMultipleChoice": ".lesson_question_context_input_answer_answer_multiple_choice",
    "LessonQuestionContextInputAnswerAnswerReading": ".lesson_question_context_input_answer_answer_reading",
    "LessonQuestionContextInputAnswerAnswerSelectImage": ".lesson_question_context_input_answer_answer_select_image",
    "LessonQuestionContextInputAnswerAnswerSortOrder": ".lesson_question_context_input_answer_answer_sort_order",
    "LessonQuestionContextInputAnswerAnswerTranslation": ".lesson_question_context_input_answer_answer_translation",
    "LessonQuestionContextInputAnswerAnswer_FillBlank": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_Listening": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_MatchColumns": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_MultipleChoice": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_Reading": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_SelectImage": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_SortOrder": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputAnswerAnswer_Translation": ".lesson_question_context_input_answer_answer",
    "LessonQuestionContextInputLesson": ".lesson_question_context_input_lesson",
    "LessonQuestionContextInputStep": ".lesson_question_context_input_step",
    "LessonQuestionContextInput_Answer": ".lesson_question_context_input",
    "LessonQuestionContextInput_Lesson": ".lesson_question_context_input",
    "LessonQuestionContextInput_Step": ".lesson_question_context_input",
    "LessonQuestionContextLesson": ".lesson_question_context_lesson",
    "LessonQuestionContextStep": ".lesson_question_context_step",
    "LessonQuestionContext_Answer": ".lesson_question_context",
    "LessonQuestionContext_Lesson": ".lesson_question_context",
    "LessonQuestionContext_Step": ".lesson_question_context",
    "LessonQuestionStatus": ".lesson_question_status",
    "LessonQuestionThread": ".lesson_question_thread",
    "LessonResource": ".lesson_resource",
    "LessonResourceGenerationStatus": ".lesson_resource_generation_status",
    "LessonResourceKind": ".lesson_resource_kind",
    "LessonSuccessorResponse": ".lesson_successor_response",
    "LessonSuccessorResponseLesson": ".lesson_successor_response_lesson",
    "LessonSuccessorResponseLessonLessonGenerationStatus": ".lesson_successor_response_lesson_lesson_generation_status",
    "LessonSuccessorResponseLessonLessonKind": ".lesson_successor_response_lesson_lesson_kind",
    "LessonVisibility": ".lesson_visibility",
    "LessonVisibilityHiddenLessonKindsItem": ".lesson_visibility_hidden_lesson_kinds_item",
    "LessonVisibilityOutput": ".lesson_visibility_output",
    "LessonVisibilityOutputHiddenLessonKindsItem": ".lesson_visibility_output_hidden_lesson_kinds_item",
    "LessonVisibilityUpdate": ".lesson_visibility_update",
    "MeDeletion": ".me_deletion",
    "MeDeletionAppleCredentials": ".me_deletion_apple_credentials",
    "MeDeletionEmailCredentials": ".me_deletion_email_credentials",
    "MeDeletionResponse": ".me_deletion_response",
    "MeDeletionZero": ".me_deletion_zero",
    "MeResponse": ".me_response",
    "MeResponseAccount": ".me_response_account",
    "MeResponseAccountDeletion": ".me_response_account_deletion",
    "MeSubscription": ".me_subscription",
    "MeUser": ".me_user",
    "NextLessonChapterResponse": ".next_lesson_chapter_response",
    "NextLessonEmptyResponse": ".next_lesson_empty_response",
    "NextLessonLessonResponse": ".next_lesson_lesson_response",
    "NextLessonResponse": ".next_lesson_response",
    "NextLessonResponse_Chapter": ".next_lesson_response",
    "NextLessonResponse_Empty": ".next_lesson_response",
    "NextLessonResponse_Lesson": ".next_lesson_response",
    "OrganizationSummary": ".organization_summary",
    "Pagination": ".pagination",
    "ResolveCoursePromptRequest": ".resolve_course_prompt_request",
    "ResolveCoursePromptRequestLanguage": ".resolve_course_prompt_request_language",
    "ResolveCoursePromptRequestLanguageTargetLanguage": ".resolve_course_prompt_request_language_target_language",
    "ResolveCoursePromptRequestTopic": ".resolve_course_prompt_request_topic",
    "ResolveCoursePromptRequest_Language": ".resolve_course_prompt_request",
    "ResolveCoursePromptRequest_Topic": ".resolve_course_prompt_request",
    "ResolveCoursePromptResponse": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponseCourse": ".resolve_course_prompt_response_course",
    "ResolveCoursePromptResponseExam": ".resolve_course_prompt_response_exam",
    "ResolveCoursePromptResponseGeneration": ".resolve_course_prompt_response_generation",
    "ResolveCoursePromptResponseLanguage": ".resolve_course_prompt_response_language",
    "ResolveCoursePromptResponseUnsafe": ".resolve_course_prompt_response_unsafe",
    "ResolveCoursePromptResponseUnsupported": ".resolve_course_prompt_response_unsupported",
    "ResolveCoursePromptResponseUnsupportedCourseFormat": ".resolve_course_prompt_response_unsupported_course_format",
    "ResolveCoursePromptResponseUnsupportedIntent": ".resolve_course_prompt_response_unsupported_intent",
    "ResolveCoursePromptResponse_Course": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponse_Exam": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponse_Generation": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponse_Language": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponse_Unsafe": ".resolve_course_prompt_response",
    "ResolveCoursePromptResponse_Unsupported": ".resolve_course_prompt_response",
    "SessionTokenResponse": ".session_token_response",
    "UsernameAvailabilityResponse": ".username_availability_response",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AppleSessionRequest",
    "AppleSessionRequestUser",
    "AppleSessionRequestUserName",
    "AppleSubscriptionResponse",
    "CatalogSearchResponse",
    "CatalogSearchResponseChaptersItem",
    "CatalogSearchResponseCoursesItem",
    "ChapterCompletionResponse",
    "ChapterCompletionResponseLessonsItem",
    "ChapterLessonListResponse",
    "ChapterResource",
    "ChapterResourceGenerationStatus",
    "CourseChapter",
    "CourseChapterGenerationStatus",
    "CourseChapterListResponse",
    "CourseCompletionResponse",
    "CourseCompletionResponseChaptersItem",
    "CourseContinuation",
    "CourseContinuationListResponse",
    "CourseContinuationPending",
    "CourseContinuationPendingChapter",
    "CourseContinuationPendingCourse",
    "CourseContinuationPendingCourseOrganization",
    "CourseContinuationPendingLesson",
    "CourseContinuationPendingLessonKind",
    "CourseContinuationReady",
    "CourseContinuationReadyChapter",
    "CourseContinuationReadyCourse",
    "CourseContinuationReadyCourseOrganization",
    "CourseContinuationReadyLesson",
    "CourseContinuationReadyLessonKind",
    "CourseContinuation_Pending",
    "CourseContinuation_Ready",
    "CourseEditionResponse",
    "CourseEditionResponseCourse",
    "CourseEditionResponseGeneration",
    "CourseEditionResponseGenerationGenerationStatus",
    "CourseEditionResponseMissing",
    "CourseEditionResponseUnsupported",
    "CourseEditionResponseUnsupportedReason",
    "CourseEditionResponse_Course",
    "CourseEditionResponse_Generation",
    "CourseEditionResponse_Missing",
    "CourseEditionResponse_Unsupported",
    "CoursePromptGenerationResponse",
    "CoursePromptGenerationResponsePending",
    "CoursePromptGenerationResponsePendingCompletionKind",
    "CoursePromptGenerationResponsePendingCourseFormat",
    "CoursePromptGenerationResponsePendingGenerationStatus",
    "CoursePromptGenerationResponseReady",
    "CoursePromptGenerationResponseReadyTarget",
    "CoursePromptGenerationResponseReadyTargetCourse",
    "CoursePromptGenerationResponseReadyTargetLesson",
    "CoursePromptGenerationResponseReadyTarget_Course",
    "CoursePromptGenerationResponseReadyTarget_Lesson",
    "CoursePromptGenerationResponse_Pending",
    "CoursePromptGenerationResponse_Ready",
    "CourseResource",
    "CourseResourceCategoriesItem",
    "CourseResourceFormat",
    "CourseResourceGenerationStatus",
    "CourseResult",
    "CurrentUserActivityResponse",
    "CurrentUserActivityResponseActivity",
    "CurrentUserActivityResponseActivityDaysItem",
    "CurrentUserCourse",
    "CurrentUserCourseListResponse",
    "CurrentUserEnergyResponse",
    "CurrentUserEnergyResponseEnergy",
    "CurrentUserEnergyResponseEnergyDaysItem",
    "CurrentUserEnergyResponseEnergyInsights",
    "CurrentUserLevelResponse",
    "CurrentUserLevelResponseLevel",
    "CurrentUserLevelResponseLevelBelt",
    "CurrentUserProgressResponse",
    "CurrentUserProgressResponseActivity",
    "CurrentUserProgressResponseEnergy",
    "CurrentUserProgressResponseLevel",
    "CurrentUserProgressResponseLevelBelt",
    "CurrentUserProgressResponseScore",
    "CurrentUserProgressResponseScorePatterns",
    "CurrentUserProgressResponseScorePatternsStrongestTime",
    "CurrentUserProgressResponseScorePatternsStrongestTimePeriod",
    "CurrentUserProgressResponseScorePatternsStrongestWeekday",
    "CurrentUserProgressResponseScorePatternsStrongestWeekdayDayOfWeek",
    "CurrentUserProgressSnapshotResponse",
    "CurrentUserProgressSnapshotResponseSnapshot",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshot",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItem",
    "CurrentUserProgressSnapshotResponseSnapshotProgressSnapshotBestDayScoresItemDayOfWeek",
    "CurrentUserScorePatternsResponse",
    "CurrentUserScorePatternsResponsePatterns",
    "CurrentUserScorePatternsResponsePatternsStrongestTime",
    "CurrentUserScorePatternsResponsePatternsStrongestTimePeriod",
    "CurrentUserScorePatternsResponsePatternsStrongestWeekday",
    "CurrentUserScorePatternsResponsePatternsStrongestWeekdayDayOfWeek",
    "CurrentUserScorePatternsResponsePatternsTimesItem",
    "CurrentUserScorePatternsResponsePatternsTimesItemPeriod",
    "CurrentUserScorePatternsResponsePatternsWeekdaysItem",
    "CurrentUserScorePatternsResponsePatternsWeekdaysItemDayOfWeek",
    "CurrentUserScoreResponse",
    "CurrentUserScoreResponseScore",
    "CurrentUserScoreResponseScoreDataPointsItem",
    "EmailAccountDeletionCredentials",
    "Error",
    "ErrorError",
    "FeedbackResponse",
    "Generation",
    "GenerationStatus",
    "GenerationTarget",
    "GenerationTargetType",
    "LanguageCourse",
    "LanguageCourseListResponse",
    "LanguageCourseTargetLanguage",
    "LessonCompletionResponse",
    "LessonCompletionResponseBelt",
    "LessonContentResponse",
    "LessonContentResponseNotGenerated",
    "LessonContentResponseReady",
    "LessonContentResponseReadyLesson",
    "LessonContentResponseReadyLessonKind",
    "LessonContentResponseReadyLessonLessonSentencesItem",
    "LessonContentResponseReadyLessonLessonWordsItem",
    "LessonContentResponseReadyLessonStepsItem",
    "LessonContentResponseReadyLessonStepsItemFillBlankOptionsItem",
    "LessonContentResponseReadyLessonStepsItemSentence",
    "LessonContentResponseReadyLessonStepsItemSentenceWordOptionsItem",
    "LessonContentResponseReadyLessonStepsItemTranslationOptionsItem",
    "LessonContentResponseReadyLessonStepsItemVocabularyOptionsItem",
    "LessonContentResponseReadyLessonStepsItemWord",
    "LessonContentResponseReadyLessonStepsItemWordBankOptionsItem",
    "LessonContentResponseReviewEmpty",
    "LessonContentResponse_NotGenerated",
    "LessonContentResponse_Ready",
    "LessonContentResponse_ReviewEmpty",
    "LessonGenerationTarget",
    "LessonGenerationTargetKind",
    "LessonPreloadResponse",
    "LessonPreloadResponseGenerationsItem",
    "LessonPreloadResponseGenerationsItemChapter",
    "LessonPreloadResponseGenerationsItemLesson",
    "LessonPreloadResponseGenerationsItem_Chapter",
    "LessonPreloadResponseGenerationsItem_Lesson",
    "LessonQuestion",
    "LessonQuestionContext",
    "LessonQuestionContextAnswer",
    "LessonQuestionContextInput",
    "LessonQuestionContextInputAnswer",
    "LessonQuestionContextInputAnswerAnswer",
    "LessonQuestionContextInputAnswerAnswerFillBlank",
    "LessonQuestionContextInputAnswerAnswerListening",
    "LessonQuestionContextInputAnswerAnswerMatchColumns",
    "LessonQuestionContextInputAnswerAnswerMatchColumnsUserPairsItem",
    "LessonQuestionContextInputAnswerAnswerMultipleChoice",
    "LessonQuestionContextInputAnswerAnswerReading",
    "LessonQuestionContextInputAnswerAnswerSelectImage",
    "LessonQuestionContextInputAnswerAnswerSortOrder",
    "LessonQuestionContextInputAnswerAnswerTranslation",
    "LessonQuestionContextInputAnswerAnswer_FillBlank",
    "LessonQuestionContextInputAnswerAnswer_Listening",
    "LessonQuestionContextInputAnswerAnswer_MatchColumns",
    "LessonQuestionContextInputAnswerAnswer_MultipleChoice",
    "LessonQuestionContextInputAnswerAnswer_Reading",
    "LessonQuestionContextInputAnswerAnswer_SelectImage",
    "LessonQuestionContextInputAnswerAnswer_SortOrder",
    "LessonQuestionContextInputAnswerAnswer_Translation",
    "LessonQuestionContextInputLesson",
    "LessonQuestionContextInputStep",
    "LessonQuestionContextInput_Answer",
    "LessonQuestionContextInput_Lesson",
    "LessonQuestionContextInput_Step",
    "LessonQuestionContextLesson",
    "LessonQuestionContextStep",
    "LessonQuestionContext_Answer",
    "LessonQuestionContext_Lesson",
    "LessonQuestionContext_Step",
    "LessonQuestionStatus",
    "LessonQuestionThread",
    "LessonResource",
    "LessonResourceGenerationStatus",
    "LessonResourceKind",
    "LessonSuccessorResponse",
    "LessonSuccessorResponseLesson",
    "LessonSuccessorResponseLessonLessonGenerationStatus",
    "LessonSuccessorResponseLessonLessonKind",
    "LessonVisibility",
    "LessonVisibilityHiddenLessonKindsItem",
    "LessonVisibilityOutput",
    "LessonVisibilityOutputHiddenLessonKindsItem",
    "LessonVisibilityUpdate",
    "MeDeletion",
    "MeDeletionAppleCredentials",
    "MeDeletionEmailCredentials",
    "MeDeletionResponse",
    "MeDeletionZero",
    "MeResponse",
    "MeResponseAccount",
    "MeResponseAccountDeletion",
    "MeSubscription",
    "MeUser",
    "NextLessonChapterResponse",
    "NextLessonEmptyResponse",
    "NextLessonLessonResponse",
    "NextLessonResponse",
    "NextLessonResponse_Chapter",
    "NextLessonResponse_Empty",
    "NextLessonResponse_Lesson",
    "OrganizationSummary",
    "Pagination",
    "ResolveCoursePromptRequest",
    "ResolveCoursePromptRequestLanguage",
    "ResolveCoursePromptRequestLanguageTargetLanguage",
    "ResolveCoursePromptRequestTopic",
    "ResolveCoursePromptRequest_Language",
    "ResolveCoursePromptRequest_Topic",
    "ResolveCoursePromptResponse",
    "ResolveCoursePromptResponseCourse",
    "ResolveCoursePromptResponseExam",
    "ResolveCoursePromptResponseGeneration",
    "ResolveCoursePromptResponseLanguage",
    "ResolveCoursePromptResponseUnsafe",
    "ResolveCoursePromptResponseUnsupported",
    "ResolveCoursePromptResponseUnsupportedCourseFormat",
    "ResolveCoursePromptResponseUnsupportedIntent",
    "ResolveCoursePromptResponse_Course",
    "ResolveCoursePromptResponse_Exam",
    "ResolveCoursePromptResponse_Generation",
    "ResolveCoursePromptResponse_Language",
    "ResolveCoursePromptResponse_Unsafe",
    "ResolveCoursePromptResponse_Unsupported",
    "SessionTokenResponse",
    "UsernameAvailabilityResponse",
]
