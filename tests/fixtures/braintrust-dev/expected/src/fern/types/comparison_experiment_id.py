

ComparisonExperimentId = str
"""
The experiment to compare against, if summarizing scores and metrics. If omitted, will fall back to the `base_exp_id` stored in the experiment metadata, and then to the most recent experiment run in the same project. Must pass `summarize_scores=true` for this id to be used
"""
