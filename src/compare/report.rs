//! The `crozier compare` report: the JSON contract (`--json`), derived into
//! `assets/compare-report.schema.json`, and the human report rendered from it.

use schemars::JsonSchema;
use serde::{Deserialize, Serialize};

use super::color::Painter;

/// Mark a required `Option` field's schema as also admitting `null`: the
/// contract states every field, with `null` for an absent value, so a consumer
/// never has to tell a missing key from a null one.
fn nullable(schema: &mut schemars::Schema) {
    let Some(object) = schema.as_object_mut() else {
        return;
    };
    match object.get_mut("type") {
        Some(serde_json::Value::String(kind)) => {
            let kind = kind.clone();
            object.insert("type".to_string(), serde_json::json!([kind, "null"]));
        }
        Some(serde_json::Value::Array(kinds)) => {
            if !kinds.iter().any(|k| k == "null") {
                kinds.push("null".into());
            }
        }
        _ => {
            let description = object.remove("description");
            let inner = serde_json::Value::Object(std::mem::take(object));
            object.insert(
                "anyOf".to_string(),
                serde_json::json!([inner, {"type": "null"}]),
            );
            if let Some(description) = description {
                object.insert("description".to_string(), description);
            }
        }
    }
}

/// The report format's version. Bump it, and regenerate the committed schema, on
/// any change a consumer could notice.
pub const SCHEMA_VERSION: u32 = 1;

/// A run's exit status, serialized as its number. Exit 1 (the command failed)
/// and 2 (usage) write no report, so they are not among its values.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
#[serde(into = "u8", try_from = "u8")]
pub enum ExitStatus {
    /// 0: every checked generator matched, or nothing was checked.
    Matched,
    /// 3: at least one generator mismatched.
    Mismatched,
    /// 4: none mismatched, and at least one could not be checked.
    CouldNotCheck,
}

impl From<ExitStatus> for u8 {
    fn from(status: ExitStatus) -> u8 {
        match status {
            ExitStatus::Matched => 0,
            ExitStatus::Mismatched => 3,
            ExitStatus::CouldNotCheck => 4,
        }
    }
}

impl TryFrom<u8> for ExitStatus {
    type Error = String;

    fn try_from(code: u8) -> Result<Self, String> {
        match code {
            0 => Ok(ExitStatus::Matched),
            3 => Ok(ExitStatus::Mismatched),
            4 => Ok(ExitStatus::CouldNotCheck),
            other => Err(format!("{other} is not a report exit status (0, 3 or 4)")),
        }
    }
}

impl JsonSchema for ExitStatus {
    fn inline_schema() -> bool {
        true
    }

    fn schema_name() -> std::borrow::Cow<'static, str> {
        "ExitStatus".into()
    }

    fn json_schema(generator: &mut schemars::SchemaGenerator) -> schemars::Schema {
        let mut schema = u8::json_schema(generator);
        schema.insert("enum".to_string(), serde_json::json!([0, 3, 4]));
        schema
    }
}

/// One `crozier compare` run.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct Report {
    /// The report format's version.
    #[schemars(extend("const" = 1))]
    pub schema_version: u32,
    /// The version of the `crozier` binary that ran.
    pub crozier_version: String,
    /// The paths searched for crozier configs, as given (the working directory
    /// when none were).
    pub searched_paths: Vec<String>,
    /// The command's exit status: 0 every checked generator matched (or nothing
    /// was checked), 3 at least one mismatched, 4 none mismatched and at least one
    /// could not be checked.
    pub exit_code: ExitStatus,
    /// How many results have each status.
    pub counts: Counts,
    /// Timing summed over the generators where both sides ran.
    pub timing_totals: TimingTotals,
    /// One result per generator, or per config that could not be read.
    pub results: Vec<GeneratorResult>,
}

/// How many results have each status.
#[derive(Debug, Clone, Copy, Default, PartialEq, Eq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct Counts {
    /// Generators whose output matched the reference.
    pub matched: usize,
    /// Generators whose output differed from the reference.
    pub mismatched: usize,
    /// Generators (or configs) that could not be checked.
    pub could_not_check: usize,
}

/// Run totals over the generators where both the reference command and crozier
/// ran.
#[derive(Debug, Clone, Copy, Default, PartialEq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct TimingTotals {
    /// How many generators the totals cover.
    pub generators_timed: usize,
    /// Summed wall time of the reference commands, in seconds.
    pub reference_seconds: f64,
    /// Summed wall time of crozier's generation, in seconds.
    pub crozier_seconds: f64,
    /// `reference_seconds / crozier_seconds`; null when nothing was timed.
    #[schemars(required, transform = nullable)]
    pub speedup: Option<f64>,
    /// `reference_seconds - crozier_seconds`.
    pub saved_seconds: f64,
}

/// A result's status.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, JsonSchema)]
#[serde(rename_all = "snake_case")]
pub enum Status {
    /// crozier's whole output tree matched the whole reference tree.
    Matched,
    /// At least one file differed or was on only one side.
    Mismatched,
    /// The comparison could not be made; `reason` says why.
    CouldNotCheck,
}

impl Status {
    /// The status as the report and the JSON spell it.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            Status::Matched => "matched",
            Status::Mismatched => "mismatched",
            Status::CouldNotCheck => "could_not_check",
        }
    }
}

/// The layout a comparison generated crozier's side with.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Serialize, Deserialize, JsonSchema)]
#[serde(rename_all = "lowercase")]
pub enum ComparedLayout {
    /// The packaged layout.
    Packaged,
    /// The flat layout.
    Flat,
}

impl From<crate::settings::Layout> for ComparedLayout {
    fn from(layout: crate::settings::Layout) -> Self {
        match layout {
            crate::settings::Layout::Packaged => ComparedLayout::Packaged,
            crate::settings::Layout::Flat => ComparedLayout::Flat,
        }
    }
}

impl ComparedLayout {
    /// The layout as the report and the JSON spell it.
    #[must_use]
    pub fn as_str(self) -> &'static str {
        match self {
            ComparedLayout::Packaged => "packaged",
            ComparedLayout::Flat => "flat",
        }
    }
}

/// One generator's result (or one unreadable config's, with `generator` null).
// llmlint: ignore[invalid_states_unrepresentable] This struct is the `--json` contract the GitHub Action consumes, fixed field by field (a flat `status` beside always-present nullable payloads) and derived into the committed schema; a status enum carrying its payload would serialize a different shape. Outside its unit tests, only `could_not_check` and `check_generator` in compare/mod.rs build it.
#[derive(Debug, Clone, PartialEq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct GeneratorResult {
    /// The result's status.
    pub status: Status,
    /// The crozier config file the generator is declared in.
    pub config_file: String,
    /// The generator's name; null when the config itself could not be read.
    #[schemars(required, transform = nullable)]
    pub generator: Option<String>,
    /// The resolved OpenAPI document; null when it could not be resolved.
    #[schemars(required, transform = nullable)]
    pub spec: Option<String>,
    /// The reference command and how it ended; null when none was resolved.
    #[schemars(required, transform = nullable)]
    pub reference: Option<ReferenceRun>,
    /// The comparison of the two trees; null when no comparison was made.
    #[schemars(required, transform = nullable)]
    pub comparison: Option<Comparison>,
    /// The two measurements and the figures derived from them; null when
    /// nothing ran.
    #[schemars(required, transform = nullable)]
    pub timing: Option<Timing>,
    /// Why the generator could not be checked, or, for a mismatch with no
    /// comparison, why crozier could not generate it; null otherwise.
    #[schemars(required, transform = nullable)]
    pub reason: Option<String>,
}

/// The reference command one generator ran.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct ReferenceRun {
    /// The command, exactly as configured.
    pub command: String,
    /// Its exit status; null when it did not run or ended without one.
    #[schemars(required, transform = nullable)]
    pub exit_code: Option<i32>,
    /// The command's own diagnostic (the tail of its stderr) when it failed or
    /// left no usable reference; null otherwise.
    #[schemars(required, transform = nullable)]
    pub diagnostic: Option<String>,
}

/// The comparison of crozier's whole output tree with the whole reference tree.
#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct Comparison {
    /// The layout crozier generated its side with.
    pub layout: ComparedLayout,
    /// How many distinct paths the two trees hold between them.
    pub files_compared: usize,
    /// Paths on both sides whose normalized contents differ.
    pub differing: Vec<String>,
    /// Paths only the reference has.
    pub only_in_reference: Vec<String>,
    /// Paths only crozier emitted.
    pub only_in_crozier: Vec<String>,
    /// The `--diff-dir` file holding this mismatch's normalized diff; null
    /// otherwise.
    #[schemars(required, transform = nullable)]
    pub diff_file: Option<String>,
}

/// One generator's two wall-time measurements and the figures derived from them.
// llmlint: ignore[invalid_states_unrepresentable] This struct is the `--json` contract's `timing` object, fixed as four nullable numbers and derived into the committed schema; it is built only by `from_measurements` (which derives `speedup` and `saved_seconds` from the two measurements, and leaves both null unless both sides ran), and its unit tests hold that rule.
#[derive(Debug, Clone, Copy, Default, PartialEq, Serialize, Deserialize, JsonSchema)]
#[serde(deny_unknown_fields)]
pub struct Timing {
    /// Wall time of the generator's one reference-command invocation, in seconds.
    #[schemars(required, transform = nullable)]
    pub reference_seconds: Option<f64>,
    /// Wall time of crozier's generation for the generator, in seconds (the
    /// comparison excluded).
    #[schemars(required, transform = nullable)]
    pub crozier_seconds: Option<f64>,
    /// `reference_seconds / crozier_seconds`; null unless both sides ran.
    #[schemars(required, transform = nullable)]
    pub speedup: Option<f64>,
    /// `reference_seconds - crozier_seconds`; null unless both sides ran.
    #[schemars(required, transform = nullable)]
    pub saved_seconds: Option<f64>,
}

impl Timing {
    /// The figures for one generator, derived from its two measurements alone.
    #[must_use]
    pub fn from_measurements(reference: Option<f64>, crozier: Option<f64>) -> Self {
        let (speedup, saved) = match (reference, crozier) {
            (Some(r), Some(c)) => (ratio(r, c), Some(r - c)),
            _ => (None, None),
        };
        Timing {
            reference_seconds: reference,
            crozier_seconds: crozier,
            speedup,
            saved_seconds: saved,
        }
    }
}

/// `numerator / denominator`, or `None` when the denominator is not positive.
fn ratio(numerator: f64, denominator: f64) -> Option<f64> {
    (denominator > 0.0).then(|| numerator / denominator)
}

impl Report {
    /// Assemble a report from its results, deriving the counts, the totals and
    /// the exit status.
    #[must_use]
    pub fn new(searched_paths: Vec<String>, results: Vec<GeneratorResult>) -> Self {
        let mut counts = Counts::default();
        let mut totals = TimingTotals::default();
        for result in &results {
            match result.status {
                Status::Matched => counts.matched += 1,
                Status::Mismatched => counts.mismatched += 1,
                Status::CouldNotCheck => counts.could_not_check += 1,
            }
            if let Some(Timing {
                reference_seconds: Some(r),
                crozier_seconds: Some(c),
                ..
            }) = result.timing
            {
                totals.generators_timed += 1;
                totals.reference_seconds += r;
                totals.crozier_seconds += c;
            }
        }
        totals.saved_seconds = totals.reference_seconds - totals.crozier_seconds;
        totals.speedup = if totals.generators_timed == 0 {
            None
        } else {
            ratio(totals.reference_seconds, totals.crozier_seconds)
        };
        let exit_code = if counts.mismatched > 0 {
            ExitStatus::Mismatched
        } else if counts.could_not_check > 0 {
            ExitStatus::CouldNotCheck
        } else {
            ExitStatus::Matched
        };
        Report {
            schema_version: SCHEMA_VERSION,
            crozier_version: env!("CARGO_PKG_VERSION").to_string(),
            searched_paths,
            exit_code,
            counts,
            timing_totals: totals,
            results,
        }
    }

    /// The collated human report, coloured by `painter`.
    #[must_use]
    pub fn render(&self, painter: Painter) -> String {
        let mut out = String::from("\ncrozier compare report\n");
        if self.results.is_empty() {
            out.push_str(&format!(
                "\nNo crozier config was found under the searched paths: {}\n",
                self.searched_paths.join(", ")
            ));
        }
        let mut current_config: Option<&str> = None;
        for result in &self.results {
            if current_config != Some(result.config_file.as_str()) {
                out.push_str(&format!("\n{}\n", result.config_file));
                current_config = Some(result.config_file.as_str());
            }
            render_result(&mut out, result, painter);
        }

        let c = self.counts;
        out.push_str(&format!(
            "\nTotals: {} matched, {} mismatched, {} could not check\n",
            painter.status(Status::Matched, &c.matched.to_string()),
            painter.status(Status::Mismatched, &c.mismatched.to_string()),
            painter.status(Status::CouldNotCheck, &c.could_not_check.to_string()),
        ));
        let t = self.timing_totals;
        if t.generators_timed > 0 {
            out.push_str(&format!(
                "Timing totals ({} generator(s) where both sides ran): {}\n",
                t.generators_timed,
                timing_line(
                    t.reference_seconds,
                    t.crozier_seconds,
                    t.speedup,
                    t.saved_seconds
                )
            ));
        } else {
            out.push_str("Timing totals: no generator ran both sides\n");
        }
        let summary = match self.exit_code {
            ExitStatus::Mismatched => format!(
                "Result: {} generator(s) mismatched the reference (exit 3)",
                c.mismatched
            ),
            ExitStatus::CouldNotCheck => format!(
                "Result: no mismatch, but {} could not be checked (exit 4)",
                c.could_not_check
            ),
            ExitStatus::Matched if self.results.is_empty() => {
                "Result: nothing to check (exit 0)".to_string()
            }
            ExitStatus::Matched => format!(
                "Result: every checked generator matched the reference ({} of {}, exit 0)",
                c.matched,
                self.results.len()
            ),
        };
        out.push_str(&painter.exit(self.exit_code, &summary));
        out.push('\n');
        out
    }
}

/// One result's block of the human report.
fn render_result(out: &mut String, result: &GeneratorResult, painter: Painter) {
    let name = result.generator.as_deref().unwrap_or("(config)");
    let mut headline = format!(
        "  {name}: {}",
        painter.status(result.status, result.status.as_str())
    );
    if let Some(comparison) = &result.comparison {
        headline.push_str(&format!(
            " (layout {}, {} file(s) compared)",
            comparison.layout.as_str(),
            comparison.files_compared
        ));
    }
    out.push_str(&headline);
    out.push('\n');
    if let Some(reference) = &result.reference {
        out.push_str(&format!("    reference command: {}\n", reference.command));
    }
    if let Some(reason) = &result.reason {
        out.push_str(&format!("    reason: {}\n", indent_continuation(reason)));
    }
    if let Some(comparison) = &result.comparison {
        for (label, paths) in [
            ("differing", &comparison.differing),
            ("only in reference", &comparison.only_in_reference),
            ("only in crozier", &comparison.only_in_crozier),
        ] {
            if paths.is_empty() {
                continue;
            }
            out.push_str(&format!("    {label} ({}):\n", paths.len()));
            for path in paths {
                out.push_str(&format!("      {path}\n"));
            }
        }
        if let Some(diff) = &comparison.diff_file {
            out.push_str(&format!("    diff: {diff}\n"));
        }
    }
    if let Some(timing) = &result.timing {
        let line = match (timing.reference_seconds, timing.crozier_seconds) {
            (Some(r), Some(c)) => {
                timing_line(r, c, timing.speedup, timing.saved_seconds.unwrap_or(r - c))
            }
            (Some(r), None) => {
                format!("reference {r:.2}s; crozier produced no SDK, so no speed-up")
            }
            (None, Some(c)) => format!("crozier {c:.2}s; the reference did not run"),
            (None, None) => "nothing ran".to_string(),
        };
        out.push_str(&format!("    timing: {line}\n"));
    }
}

/// `reference …s, crozier …s, speed-up …x, saved …s`.
fn timing_line(reference: f64, crozier: f64, speedup: Option<f64>, saved: f64) -> String {
    let multiple = speedup.map_or_else(
        || "speed-up not measurable".to_string(),
        |x| format!("speed-up {x:.2}x"),
    );
    format!("reference {reference:.2}s, crozier {crozier:.2}s, {multiple}, saved {saved:.2}s")
}

/// Indent a multi-line reason so its later lines sit under the first.
fn indent_continuation(text: &str) -> String {
    text.trim_end().replace('\n', "\n            ")
}

#[cfg(test)]
mod tests {
    use super::*;

    fn result(status: Status, timing: Option<Timing>) -> GeneratorResult {
        GeneratorResult {
            status,
            config_file: "crozier.yml".to_string(),
            generator: Some("python".to_string()),
            spec: Some("/r/openapi.yml".to_string()),
            reference: Some(ReferenceRun {
                command: "./ref.sh".to_string(),
                exit_code: Some(0),
                diagnostic: None,
            }),
            comparison: None,
            timing,
            reason: None,
        }
    }

    #[test]
    fn an_exit_status_is_its_number_and_only_a_report_status_parses() {
        for (status, code) in [
            (ExitStatus::Matched, 0u8),
            (ExitStatus::Mismatched, 3),
            (ExitStatus::CouldNotCheck, 4),
        ] {
            assert_eq!(u8::from(status), code);
            assert_eq!(serde_json::to_string(&status).unwrap(), code.to_string());
            assert_eq!(
                serde_json::from_str::<ExitStatus>(&code.to_string()).unwrap(),
                status
            );
        }
        let error = serde_json::from_str::<ExitStatus>("1").unwrap_err();
        assert!(
            error.to_string().contains("1 is not a report exit status"),
            "{error}"
        );
    }

    #[test]
    fn timing_derives_every_figure_from_the_two_measurements() {
        let t = Timing::from_measurements(Some(3.0), Some(0.5));
        assert_eq!(t.speedup, Some(6.0));
        assert_eq!(t.saved_seconds, Some(2.5));
        // A side that did not run leaves no speed-up.
        let t = Timing::from_measurements(Some(3.0), None);
        assert_eq!((t.speedup, t.saved_seconds), (None, None));
        // A zero crozier time has no finite multiple.
        assert_eq!(
            Timing::from_measurements(Some(1.0), Some(0.0)).speedup,
            None
        );
    }

    #[test]
    fn exit_status_mismatch_dominates_then_could_not_check() {
        let timed = Some(Timing::from_measurements(Some(2.0), Some(1.0)));
        let report = Report::new(
            vec![".".into()],
            vec![
                result(Status::Matched, timed),
                result(Status::CouldNotCheck, None),
                result(Status::Mismatched, timed),
            ],
        );
        assert_eq!(report.exit_code, ExitStatus::Mismatched);
        assert_eq!(
            report.counts,
            Counts {
                matched: 1,
                mismatched: 1,
                could_not_check: 1
            }
        );
        assert_eq!(report.timing_totals.generators_timed, 2);
        assert_eq!(report.timing_totals.reference_seconds, 4.0);
        assert_eq!(report.timing_totals.speedup, Some(2.0));
        assert_eq!(report.timing_totals.saved_seconds, 2.0);

        let report = Report::new(
            vec![],
            vec![
                result(Status::Matched, None),
                result(Status::CouldNotCheck, None),
            ],
        );
        assert_eq!(report.exit_code, ExitStatus::CouldNotCheck);
        assert_eq!(report.timing_totals.speedup, None);
        assert_eq!(Report::new(vec![], vec![]).exit_code, ExitStatus::Matched);
        assert_eq!(
            Report::new(vec![], vec![result(Status::Matched, None)]).exit_code,
            ExitStatus::Matched
        );
    }

    #[test]
    fn render_lists_paths_reasons_timings_and_the_result_line() {
        let mut mismatched = result(
            Status::Mismatched,
            Some(Timing::from_measurements(Some(2.0), Some(0.5))),
        );
        mismatched.comparison = Some(Comparison {
            layout: ComparedLayout::Flat,
            files_compared: 4,
            differing: vec!["a.py".into()],
            only_in_reference: vec!["b.py".into()],
            only_in_crozier: vec!["c.py".into()],
            diff_file: Some("diffs/001.diff".into()),
        });
        let mut failed = result(
            Status::CouldNotCheck,
            Some(Timing::from_measurements(Some(1.0), None)),
        );
        failed.reason = Some("the reference command failed\nline two".into());
        let mut unreadable = result(Status::CouldNotCheck, None);
        unreadable.config_file = "other/crozier.yml".into();
        unreadable.generator = None;
        unreadable.reference = None;
        unreadable.reason = Some("invalid config".into());
        let text = Report::new(vec![".".into()], vec![mismatched, failed, unreadable])
            .render(Painter::new(false));
        for want in [
            "crozier.yml\n",
            "  python: mismatched (layout flat, 4 file(s) compared)",
            "    reference command: ./ref.sh",
            "    differing (1):\n      a.py",
            "    only in reference (1):\n      b.py",
            "    only in crozier (1):\n      c.py",
            "    diff: diffs/001.diff",
            "reference 2.00s, crozier 0.50s, speed-up 4.00x, saved 1.50s",
            "reference 1.00s; crozier produced no SDK, so no speed-up",
            "    reason: the reference command failed\n            line two",
            "other/crozier.yml\n  (config): could_not_check",
            "Totals: 0 matched, 1 mismatched, 2 could not check",
            "Timing totals (1 generator(s) where both sides ran)",
            "Result: 1 generator(s) mismatched the reference (exit 3)",
        ] {
            assert!(text.contains(want), "missing {want:?} in:\n{text}");
        }
        assert!(!text.contains('\u{1b}'), "{text}");
    }

    #[test]
    fn render_says_when_nothing_was_found_and_covers_each_result_line() {
        let text = Report::new(vec!["repo".into()], vec![]).render(Painter::new(false));
        assert!(text.contains("No crozier config was found under the searched paths: repo"));
        assert!(text.contains("Timing totals: no generator ran both sides"));
        assert!(text.contains("Result: nothing to check (exit 0)"));

        let matched = Report::new(
            vec![],
            vec![result(
                Status::Matched,
                Some(Timing::from_measurements(Some(1.0), Some(0.0))),
            )],
        );
        let text = matched.render(Painter::new(false));
        assert!(text.contains("speed-up not measurable"), "{text}");
        assert!(text.contains("every checked generator matched the reference (1 of 1, exit 0)"));

        let mut odd = result(Status::CouldNotCheck, Some(Timing::default()));
        odd.reference = None;
        let mut crozier_only = result(
            Status::CouldNotCheck,
            Some(Timing::from_measurements(None, Some(0.25))),
        );
        crozier_only.reference = None;
        let text = Report::new(vec![], vec![odd, crozier_only]).render(Painter::new(false));
        assert!(text.contains("timing: nothing ran"), "{text}");
        assert!(
            text.contains("crozier 0.25s; the reference did not run"),
            "{text}"
        );
        assert!(text.contains("no mismatch, but 2 could not be checked (exit 4)"));
    }

    #[test]
    fn nullable_admits_null_for_every_schema_shape() {
        let check = |before: serde_json::Value, after: serde_json::Value| {
            let mut schema = schemars::Schema::try_from(before).unwrap();
            nullable(&mut schema);
            assert_eq!(schema.as_value(), &after);
        };
        check(
            serde_json::json!({"type": "string"}),
            serde_json::json!({"type": ["string", "null"]}),
        );
        check(
            serde_json::json!({"type": ["string", "null"]}),
            serde_json::json!({"type": ["string", "null"]}),
        );
        check(
            serde_json::json!({"type": ["string"]}),
            serde_json::json!({"type": ["string", "null"]}),
        );
        check(
            serde_json::json!({"$ref": "#/$defs/X", "description": "d"}),
            serde_json::json!({"anyOf": [{"$ref": "#/$defs/X"}, {"type": "null"}], "description": "d"}),
        );
        check(
            serde_json::json!({"$ref": "#/$defs/X"}),
            serde_json::json!({"anyOf": [{"$ref": "#/$defs/X"}, {"type": "null"}]}),
        );
        let mut always = schemars::Schema::from(true);
        nullable(&mut always);
        assert_eq!(always.as_value(), &serde_json::Value::Bool(true));
    }

    #[test]
    fn spellings_match_the_contract() {
        assert_eq!(Status::CouldNotCheck.as_str(), "could_not_check");
        assert_eq!(
            serde_json::to_value(Status::CouldNotCheck).unwrap(),
            "could_not_check"
        );
        assert_eq!(
            ComparedLayout::from(crate::settings::Layout::Flat).as_str(),
            "flat"
        );
        assert_eq!(
            serde_json::to_value(ComparedLayout::from(crate::settings::Layout::Packaged)).unwrap(),
            "packaged"
        );
    }
}
