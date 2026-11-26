//! SPIKE ONLY (`spike-windows-lane-breakdown`): temporary phase timers and
//! subprocess accounting, so the spike's CI runs can say where every crozier
//! process the suites start spends its time. This branch never lands; the
//! durable `CROZIER_PROFILE` belongs to the plan's `runtime-profiling` node, and
//! this module writes that node's agreed `schema_version: 1` shape so its figures
//! read the same way.
//!
//! When `CROZIER_PROFILE` names a directory, each process writes one
//! `crozier-profile-<pid>-<unix-nanos>.json` there on exit. Unset or empty, every
//! entry point here is one cached environment read and nothing else.

use std::path::PathBuf;
use std::sync::{Mutex, OnceLock};
use std::time::{Duration, Instant, SystemTime, UNIX_EPOCH};

#[derive(Default)]
struct Totals {
    phases: Vec<(&'static str, Duration, u64)>,
    spawns: Vec<(String, Duration, u64)>,
}

struct State {
    dir: PathBuf,
    start: Instant,
    totals: Mutex<Totals>,
}

fn state() -> Option<&'static State> {
    static STATE: OnceLock<Option<State>> = OnceLock::new();
    STATE
        .get_or_init(|| {
            let dir = std::env::var_os("CROZIER_PROFILE").filter(|value| !value.is_empty())?;
            Some(State {
                dir: PathBuf::from(dir),
                start: Instant::now(),
                totals: Mutex::new(Totals::default()),
            })
        })
        .as_ref()
}

/// Start the process clock (call first thing in `main`).
pub fn start() {
    let _ = state();
}

/// A running phase timer; its time is added to `name` when it drops.
pub struct Phase {
    name: &'static str,
    started: Option<Instant>,
}

/// Time the rest of the enclosing scope as phase `name`.
pub fn phase(name: &'static str) -> Phase {
    Phase {
        name,
        started: state().map(|_| Instant::now()),
    }
}

impl Drop for Phase {
    fn drop(&mut self) {
        if let (Some(state), Some(started)) = (state(), self.started) {
            add_phase(state, self.name, started.elapsed());
        }
    }
}

fn add_phase(state: &State, name: &'static str, elapsed: Duration) {
    let mut totals = state.totals.lock().unwrap_or_else(|e| e.into_inner());
    match totals.phases.iter_mut().find(|(n, _, _)| *n == name) {
        Some(entry) => {
            entry.1 += elapsed;
            entry.2 += 1;
        }
        None => totals.phases.push((name, elapsed, 1)),
    }
}

/// Record one finished child process of `program` that took `elapsed`.
pub fn spawned(program: &str, elapsed: Duration) {
    let Some(state) = state() else { return };
    let mut totals = state.totals.lock().unwrap_or_else(|e| e.into_inner());
    match totals.spawns.iter_mut().find(|(p, _, _)| p == program) {
        Some(entry) => {
            entry.1 += elapsed;
            entry.2 += 1;
        }
        None => totals.spawns.push((program.to_string(), elapsed, 1)),
    }
}

/// Start a timer for a child of `program`; the returned closure records it.
pub fn spawn_timer(program: &'static str) -> impl FnOnce() {
    let started = state().map(|_| Instant::now());
    move || {
        if let Some(started) = started {
            spawned(program, started.elapsed());
        }
    }
}

/// A running child-process timer for `program`, recorded when it drops.
pub struct SpawnGuard {
    program: &'static str,
    started: Option<Instant>,
}

/// Time the rest of the enclosing scope as one child of `program`.
pub fn spawn_guard(program: &'static str) -> SpawnGuard {
    SpawnGuard {
        program,
        started: state().map(|_| Instant::now()),
    }
}

impl Drop for SpawnGuard {
    fn drop(&mut self) {
        if let Some(started) = self.started {
            spawned(self.program, started.elapsed());
        }
    }
}

fn json_string(value: &str) -> String {
    let mut out = String::with_capacity(value.len() + 2);
    out.push('"');
    for c in value.chars() {
        match c {
            '"' => out.push_str("\\\""),
            '\\' => out.push_str("\\\\"),
            c if (c as u32) < 0x20 => out.push_str(&format!("\\u{:04x}", c as u32)),
            c => out.push(c),
        }
    }
    out.push('"');
    out
}

fn env_or_null(name: &str) -> String {
    std::env::var(name).map_or_else(|_| "null".to_string(), |v| json_string(&v))
}

/// Write this process's profile, if profiling is on. Never fails the run: a
/// profile that cannot be written is reported on stderr and dropped.
pub fn write(command: &str, exit_code: u8) {
    let Some(state) = state() else { return };
    let total = state.start.elapsed().as_secs_f64();
    let totals = state.totals.lock().unwrap_or_else(|e| e.into_inner());
    let phases: Vec<String> = totals
        .phases
        .iter()
        .map(|(name, d, n)| {
            format!(
                "{{\"name\":{},\"seconds\":{:.6},\"count\":{n}}}",
                json_string(name),
                d.as_secs_f64()
            )
        })
        .collect();
    let spawns: Vec<String> = totals
        .spawns
        .iter()
        .map(|(program, d, n)| {
            format!(
                "{{\"program\":{},\"spawns\":{n},\"seconds\":{:.6}}}",
                json_string(program),
                d.as_secs_f64()
            )
        })
        .collect();
    let args: Vec<String> = std::env::args_os()
        .skip(1)
        .map(|a| json_string(&a.to_string_lossy()))
        .collect();
    // `spike` carries what only this spike reads: which Nx task and test
    // started the process, so a profile can be attributed to its suite.
    let body = format!(
        "{{\"schema_version\":1,\"command\":{},\"total_seconds\":{total:.6},\"phases\":[{}],\"subprocesses\":[{}],\"spike\":{{\"exit_code\":{exit_code},\"nx_project\":{},\"nx_target\":{},\"pytest_test\":{},\"nextest_test\":{},\"args\":[{}]}}}}\n",
        json_string(command),
        phases.join(","),
        spawns.join(","),
        env_or_null("NX_TASK_TARGET_PROJECT"),
        env_or_null("NX_TASK_TARGET_TARGET"),
        env_or_null("PYTEST_CURRENT_TEST"),
        env_or_null("NEXTEST_TEST_NAME"),
        args.join(","),
    );
    let nanos = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .map_or(0, |d| d.as_nanos());
    let path = state.dir.join(format!(
        "crozier-profile-{}-{nanos}.json",
        std::process::id()
    ));
    if let Err(error) =
        std::fs::create_dir_all(&state.dir).and_then(|()| std::fs::write(&path, body))
    {
        eprintln!(
            "crozier: could not write the profile {}: {error}",
            path.display()
        );
    }
}
