#!/usr/bin/env bash
#
# install-bmad-marketing.sh
#
# Install the BMad Marketing Growth Suite into the current project.
# Pulls https://github.com/bluecoral-vn/bmad-performance-marketing and registers
# it as a custom source with the BMAD-METHOD installer.
#
# Usage:
#   ./install-bmad-marketing.sh                # interactive install in current dir
#   ./install-bmad-marketing.sh --yes          # non-interactive (auto-select performance-marketing)
#   ./install-bmad-marketing.sh --ref <tag>    # pin to a specific git tag/branch
#   ./install-bmad-marketing.sh --help         # show this help
#
# Exit codes:
#   0  success
#   1  prerequisite missing (node/npm)
#   2  BMAD-METHOD not yet installed in this project
#   3  user aborted
#   4  installer failed

set -euo pipefail

# ---- Configuration --------------------------------------------------------

readonly MARKETING_REPO="https://github.com/bluecoral-vn/bmad-performance-marketing"
readonly MARKETING_MODULE_CODE="performance-marketing"
readonly BMAD_DIR="_bmad"
readonly BMAD_MANIFEST="${BMAD_DIR}/_config/manifest.yaml"

# ---- Pretty output --------------------------------------------------------

if [[ -t 1 ]]; then
  readonly C_RESET=$'\033[0m'
  readonly C_BOLD=$'\033[1m'
  readonly C_DIM=$'\033[2m'
  readonly C_RED=$'\033[31m'
  readonly C_GREEN=$'\033[32m'
  readonly C_YELLOW=$'\033[33m'
  readonly C_BLUE=$'\033[34m'
  readonly C_CYAN=$'\033[36m'
else
  readonly C_RESET="" C_BOLD="" C_DIM="" C_RED="" C_GREEN="" C_YELLOW="" C_BLUE="" C_CYAN=""
fi

info()    { printf "%s[i]%s %s\n" "$C_CYAN" "$C_RESET" "$*"; }
ok()      { printf "%s[✓]%s %s\n" "$C_GREEN" "$C_RESET" "$*"; }
warn()    { printf "%s[!]%s %s\n" "$C_YELLOW" "$C_RESET" "$*"; }
err()     { printf "%s[✗]%s %s\n" "$C_RED" "$C_RESET" "$*" >&2; }
heading() { printf "\n%s%s%s\n" "$C_BOLD$C_BLUE" "$*" "$C_RESET"; }

# ---- CLI arg parsing ------------------------------------------------------

ASSUME_YES=0
PIN_REF=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    -y|--yes)
      ASSUME_YES=1
      shift
      ;;
    --ref)
      [[ $# -ge 2 ]] || { err "--ref requires a value"; exit 1; }
      PIN_REF="$2"
      shift 2
      ;;
    -h|--help)
      sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'
      exit 0
      ;;
    *)
      err "Unknown argument: $1"
      err "Run with --help for usage."
      exit 1
      ;;
  esac
done

# ---- Step 1: Prerequisite check ------------------------------------------

heading "BMad Marketing Growth Suite — installer"
info "Target project: $(pwd)"

if ! command -v node >/dev/null 2>&1; then
  err "node is not installed. Install Node.js 18+ from https://nodejs.org"
  exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
  err "npm is not installed (it ships with Node.js)."
  exit 1
fi

if ! command -v npx >/dev/null 2>&1; then
  err "npx is not installed (it ships with npm 5.2+)."
  exit 1
fi

ok "Node $(node --version) / npm $(npm --version) detected"

# ---- Step 2: Sanity check on cwd -----------------------------------------

if [[ ! -d .git ]]; then
  warn "Current directory is not a git repository."
  warn "BMad installs into the current working directory ($(pwd))."
  if [[ $ASSUME_YES -eq 0 ]]; then
    read -r -p "Continue installing here? [y/N] " reply
    case "$reply" in
      [yY]|[yY][eE][sS]) ;;
      *) info "Aborted."; exit 3 ;;
    esac
  fi
fi

# ---- Step 3: Check BMAD-METHOD is installed ------------------------------

if [[ ! -f "$BMAD_MANIFEST" ]]; then
  heading "BMAD-METHOD is not installed in this project"
  warn "Looked for: $BMAD_MANIFEST"
  cat <<EOF

The BMad Marketing Growth Suite is a module that runs on top of BMAD-METHOD.
You must install BMAD-METHOD first.

  ${C_BOLD}Run this command in $(pwd):${C_RESET}

      ${C_GREEN}npx bmad-method install${C_RESET}

  Then re-run this script:

      ${C_GREEN}$(basename "$0")${C_RESET}

EOF
  if [[ $ASSUME_YES -eq 1 ]]; then
    err "Cannot proceed in --yes mode without BMAD-METHOD installed."
    exit 2
  fi
  read -r -p "Run 'npx bmad-method install' now? [y/N] " reply
  case "$reply" in
    [yY]|[yY][eE][sS])
      info "Launching BMAD-METHOD installer..."
      if ! npx --yes bmad-method install; then
        err "BMAD-METHOD installer failed. Aborting."
        exit 2
      fi
      ok "BMAD-METHOD installed."
      ;;
    *)
      info "Install BMAD-METHOD first, then re-run this script."
      exit 2
      ;;
  esac
fi

ok "BMAD-METHOD detected at $BMAD_DIR/"

# ---- Step 4: Read existing modules (additive install) --------------------
#
# IMPORTANT: passing `--modules performance-marketing --yes` to bmad-method
# wipes every other installed module's payload (core/bmm/cis). We always pass
# the union of existing modules + performance-marketing so nothing is removed.

command -v python3 >/dev/null 2>&1 || { err "python3 is required to parse the BMad manifest."; exit 1; }

existing_modules=$(python3 - "$BMAD_MANIFEST" <<'PY'
import sys, yaml
with open(sys.argv[1]) as f:
    m = yaml.safe_load(f) or {}
print(",".join(e.get("name","") for e in (m.get("modules") or []) if e.get("name")))
PY
)

if [[ -z "$existing_modules" ]]; then
  merged_modules="$MARKETING_MODULE_CODE"
elif [[ ",${existing_modules}," == *",${MARKETING_MODULE_CODE},"* ]]; then
  warn "Module '${MARKETING_MODULE_CODE}' already listed in manifest — this will reinstall/refresh it."
  if [[ $ASSUME_YES -eq 0 ]]; then
    read -r -p "Reinstall / update from $MARKETING_REPO? [y/N] " reply
    case "$reply" in
      [yY]|[yY][eE][sS]) info "Proceeding with reinstall." ;;
      *) info "Aborted."; exit 3 ;;
    esac
  fi
  merged_modules="$existing_modules"
else
  merged_modules="${existing_modules},${MARKETING_MODULE_CODE}"
fi

info "Existing modules: ${existing_modules:-<none>}"
info "Modules to install (additive): $merged_modules"

# ---- Step 5: Build the install command -----------------------------------

source_arg="$MARKETING_REPO"
if [[ -n "$PIN_REF" ]]; then
  source_arg="${MARKETING_REPO}@${PIN_REF}"
  info "Pinning to ref: $PIN_REF"
fi

install_args=(--custom-source "$source_arg" --modules "$merged_modules")

if [[ $ASSUME_YES -eq 1 ]]; then
  install_args+=(--yes)
fi

# ---- Step 6: Run the installer -------------------------------------------

heading "Installing $MARKETING_MODULE_CODE from $source_arg"
info "Command: npx bmad-method install ${install_args[*]}"

if ! npx --yes bmad-method install "${install_args[@]}"; then
  err "Installer failed. Inspect output above for details."
  exit 4
fi

# ---- Step 7: Verify ------------------------------------------------------

if [[ -d "${BMAD_DIR}/${MARKETING_MODULE_CODE}" ]]; then
  ok "Installed: ${BMAD_DIR}/${MARKETING_MODULE_CODE}/"
else
  warn "Expected ${BMAD_DIR}/${MARKETING_MODULE_CODE}/ but did not find it."
  warn "Check the installer output — the module may have been installed under a different code."
fi

heading "Done"
cat <<EOF
${C_GREEN}✓ BMad Marketing Growth Suite installed.${C_RESET}

Next steps:
  • Open Claude Code (or your IDE with the BMad integration) in this directory.
  • Run the orchestrator:  ${C_BOLD}/bmad-marketing-orchestrator${C_RESET}
  • Or jump straight to a workflow: ${C_BOLD}/bmad-marketing-strategy${C_RESET}, ${C_BOLD}/bmad-content-pipeline${C_RESET}, ${C_BOLD}/bmad-seo-sprint${C_RESET}, etc.
  • List all skills in this module: ${C_BOLD}npx bmad-method list${C_RESET}
  • Update later:                 ${C_BOLD}npx bmad-method update${C_RESET}

Repo:    $MARKETING_REPO
Module:  $MARKETING_MODULE_CODE
EOF
