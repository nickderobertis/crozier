use proc_macro2::LineColumn;
use std::collections::{BTreeMap, BTreeSet};
use std::path::PathBuf;
use std::process::{Command, Output};
use syn::spanned::Spanned;
use syn::visit::{self, Visit};

const SOURCES: [&str; 4] = [
    "src/emit.rs",
    "src/ir.rs",
    "src/openapi.rs",
    "src/naming.rs",
];
const HELPERS: [&str; 15] = [
    "or_else",
    "and_then",
    "is_some_and",
    "filter",
    "find",
    "find_map",
    "flat_map",
    "map",
    "map_or",
    "map_or_else",
    "any",
    "all",
    "then",
    "then_some",
    "for_each",
];

fn repo() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
}

fn command_output(program: &str, args: &[&str]) -> Output {
    Command::new(program)
        .args(args)
        .current_dir(repo())
        .output()
        .unwrap_or_else(|error| panic!("run {program}: {error}"))
}

fn added_lines(path: &str) -> BTreeSet<usize> {
    let output = command_output(
        "git",
        &["diff", "--unified=0", "origin/main..HEAD", "--", path],
    );
    assert!(output.status.success());
    let diff = String::from_utf8(output.stdout).expect("git diff is UTF-8");
    let mut current = 0;
    let mut lines = BTreeSet::new();
    for line in diff.lines() {
        if let Some(hunk) = line.strip_prefix("@@") {
            let plus = hunk.split_whitespace().find(|part| part.starts_with('+'));
            current = plus
                .and_then(|part| part[1..].split(',').next())
                .and_then(|line| line.parse().ok())
                .expect("zero-context hunk has a destination line");
        } else if line.starts_with("+++") {
            continue;
        } else if line.starts_with('+') {
            lines.insert(current);
            current += 1;
        } else if line.starts_with(' ') {
            current += 1;
        }
    }
    lines
}

fn is_test_cfg(attrs: &[syn::Attribute]) -> bool {
    attrs.iter().any(|attr| {
        attr.path().is_ident("cfg")
            && matches!(&attr.meta, syn::Meta::List(meta) if meta.tokens.to_string().contains("test"))
    })
}

struct Constructs<'a> {
    path: &'a str,
    added: &'a BTreeSet<usize>,
    found: BTreeSet<String>,
}

impl Constructs<'_> {
    fn add(&mut self, position: LineColumn) {
        if self.added.contains(&position.line) {
            self.found
                .insert(format!("{}:{}", self.path, position.line));
        }
    }
}

impl<'ast> Visit<'ast> for Constructs<'_> {
    fn visit_item_mod(&mut self, node: &'ast syn::ItemMod) {
        if !is_test_cfg(&node.attrs) {
            visit::visit_item_mod(self, node);
        }
    }

    fn visit_item_fn(&mut self, node: &'ast syn::ItemFn) {
        if !is_test_cfg(&node.attrs) {
            self.add(node.sig.fn_token.span.start());
            visit::visit_item_fn(self, node);
        }
    }

    fn visit_impl_item_fn(&mut self, node: &'ast syn::ImplItemFn) {
        if !is_test_cfg(&node.attrs) {
            self.add(node.sig.fn_token.span.start());
            visit::visit_impl_item_fn(self, node);
        }
    }

    fn visit_expr(&mut self, node: &'ast syn::Expr) {
        match node {
            syn::Expr::If(expr) => {
                self.add(expr.if_token.span.start());
                if let Some((else_token, _)) = &expr.else_branch {
                    self.add(else_token.span.start());
                }
            }
            syn::Expr::Match(expr) => self.add(expr.match_token.span.start()),
            syn::Expr::ForLoop(expr) => self.add(expr.for_token.span.start()),
            syn::Expr::While(expr) => self.add(expr.while_token.span.start()),
            syn::Expr::Loop(expr) => self.add(expr.loop_token.span.start()),
            syn::Expr::Return(expr) => self.add(expr.return_token.span.start()),
            syn::Expr::Break(expr) => self.add(expr.break_token.span.start()),
            syn::Expr::Continue(expr) => self.add(expr.continue_token.span.start()),
            syn::Expr::Try(expr) => self.add(expr.question_token.span.start()),
            syn::Expr::Closure(expr) => self.add(expr.or1_token.span.start()),
            syn::Expr::MethodCall(expr) if HELPERS.contains(&expr.method.to_string().as_str()) => {
                self.add(expr.method.span().start());
            }
            _ => {}
        }
        visit::visit_expr(self, node);
    }

    fn visit_arm(&mut self, node: &'ast syn::Arm) {
        self.add(node.fat_arrow_token.span().start());
        visit::visit_arm(self, node);
    }
}

fn ast_constructs() -> BTreeSet<String> {
    let mut all = BTreeSet::new();
    for path in SOURCES {
        let before = command_output("git", &["show", &format!("origin/main:{path}")]);
        assert!(
            before.status.success(),
            "reconstruct {path} before batch changes"
        );
        syn::parse_file(&String::from_utf8(before.stdout).expect("before source is UTF-8"))
            .unwrap_or_else(|error| panic!("parse before {path}: {error}"));

        let source = std::fs::read_to_string(repo().join(path)).expect("read current source");
        let syntax =
            syn::parse_file(&source).unwrap_or_else(|error| panic!("parse {path}: {error}"));
        let added = added_lines(path);
        let mut visitor = Constructs {
            path,
            added: &added,
            found: BTreeSet::new(),
        };
        visitor.visit_file(&syntax);
        all.extend(visitor.found);
    }
    all
}

fn shell_constructs() -> BTreeSet<String> {
    let output = command_output(
        "bash",
        &[
            "scripts/check-batch2-coverage-audit.sh",
            "--dump-constructs",
        ],
    );
    assert!(output.status.success(), "shell detector failed");
    String::from_utf8(output.stdout)
        .expect("checker output is UTF-8")
        .lines()
        .map(str::to_owned)
        .collect()
}

#[test]
fn syn_and_shell_detectors_reconcile_the_real_batch_diff() {
    let ast = ast_constructs();
    let shell = shell_constructs();
    for path in SOURCES {
        let ast_file: BTreeSet<_> = ast.iter().filter(|item| item.starts_with(path)).collect();
        let shell_file: BTreeSet<_> = shell.iter().filter(|item| item.starts_with(path)).collect();
        let missing: Vec<_> = ast_file.difference(&shell_file).collect();
        let extra: Vec<_> = shell_file.difference(&ast_file).collect();
        println!(
            "{path}: ast={} shell={} missing={missing:?} extra={extra:?}",
            ast_file.len(),
            shell_file.len()
        );
    }
    let missing: Vec<_> = ast.difference(&shell).collect();
    let extra: Vec<_> = shell.difference(&ast).collect();
    assert!(
        missing.is_empty(),
        "shell misses syn constructs: {missing:#?}"
    );
    assert!(extra.is_empty(), "shell has non-syn constructs: {extra:#?}");
}

fn run_mutation(contents: &str) -> Output {
    let dir = tempfile::tempdir().expect("tempdir");
    let audit = dir.path().join("audit.md");
    std::fs::write(&audit, contents).expect("write mutated audit");
    Command::new("bash")
        .arg("scripts/check-batch2-coverage-audit.sh")
        .env("CROZIER_AUDIT_FILE", &audit)
        .current_dir(repo())
        .output()
        .expect("run checker")
}

#[test]
fn checker_rejects_inventory_and_evidence_mutations() {
    let audit =
        std::fs::read_to_string(repo().join("docs/batch2-coverage-audit.md")).expect("read audit");
    let mutations: BTreeMap<&str, String> = [
        ("missing mapping", audit.replacen("| 574:", "| 575:", 1)),
        (
            "duplicate mapping",
            audit.replacen("| 574:", "| 574, 574:", 1),
        ),
        (
            "nonexistent assertion",
            audit.replacen(
                "tests/generation.rs:2013-2020",
                "tests/generation.rs:999999",
                1,
            ),
        ),
        (
            "assertion outside test",
            audit.replacen("tests/generation.rs:2013-2020", "tests/generation.rs:1", 1),
        ),
        (
            "e2e evidence",
            audit.replacen(
                "`self_referential_model_uses_forward_references`, `tests/generation.rs:2013-2020`",
                "`e2e_probe`, `tests/e2e.rs:1`",
                1,
            ),
        ),
    ]
    .into_iter()
    .collect();
    for (name, mutation) in mutations {
        let output = run_mutation(&mutation);
        assert!(!output.status.success(), "checker accepted {name}");
    }
}

#[test]
fn syn_test_module_classification_preserves_later_production_items() {
    let source = r#"
#[cfg(test)]
mod early_tests {
    #[test]
    fn ignored() { if true {} }
}

fn later_production() -> Option<u8> {
    Some(1).map(|value| value + 1)
}
"#;
    let syntax = syn::parse_file(source).expect("fixture parses");
    let added = (1..=source.lines().count()).collect();
    let mut visitor = Constructs {
        path: "src/sample.rs",
        added: &added,
        found: BTreeSet::new(),
    };
    visitor.visit_file(&syntax);
    assert!(visitor.found.iter().any(|item| item.ends_with(":8")));
    assert!(visitor.found.iter().any(|item| item.ends_with(":9")));
    assert!(!visitor.found.iter().any(|item| item.ends_with(":5")));
}

#[test]
fn syn_detector_ignores_tokens_and_tracks_multiline_rust_syntax() {
    let source = r#"fn production(value: Option<u8>) -> Option<u8> {
    // if match return |comment| => ?
    let text = "if match return |string| => ?";
    fake!(if true { return None; });
    let mapped = value
        .map::<u8>(
            |item| item + 1,
        )?;
    let result = match mapped {
        Some(item)
            => item,
        None => 0,
    };
    Some(result)
}"#;
    let syntax = syn::parse_file(source).expect("fixture parses");
    let added = (1..=source.lines().count()).collect();
    let mut visitor = Constructs {
        path: "src/sample.rs",
        added: &added,
        found: BTreeSet::new(),
    };
    visitor.visit_file(&syntax);
    let expected = [1, 6, 7, 8, 9, 11, 12]
        .into_iter()
        .map(|line| format!("src/sample.rs:{line}"))
        .collect();
    assert_eq!(visitor.found, expected);
}
