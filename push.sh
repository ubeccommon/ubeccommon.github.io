#!/bin/bash
# ─────────────────────────────────────────────────────────────────
# Erdpuls OER — Git Push Helper
# Usage:
#   ./push.sh "your commit message"
#   ./push.sh                        ← prompts for message
# ─────────────────────────────────────────────────────────────────

set -e  # exit immediately on any error

# ── Colors ────────────────────────────────────────────────────────
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}🌱 Erdpuls OER — Git Push Helper${NC}"
echo "─────────────────────────────────"

# ── Commit message ────────────────────────────────────────────────
if [ -n "$1" ]; then
  COMMIT_MSG="$1"
else
  echo -e "${YELLOW}Enter commit message:${NC} \c"
  read COMMIT_MSG
  if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="update: content changes"
  fi
fi

# ── Check we're in a git repo ─────────────────────────────────────
if ! git rev-parse --git-dir > /dev/null 2>&1; then
  echo -e "${RED}✗ Not a git repository. Run this from your repo root.${NC}"
  exit 1
fi

# ── Pull latest (includes any bot commits) ────────────────────────
echo -e "\n${CYAN}① Pulling latest changes from remote...${NC}"
git pull origin main --no-rebase

# ── Stage all changes ─────────────────────────────────────────────
echo -e "\n${CYAN}② Staging all changes...${NC}"
git add .

# ── Check if there's anything to commit ──────────────────────────
if git diff --cached --quiet; then
  echo -e "${YELLOW}⚠ Nothing to commit — working tree is clean.${NC}"
  exit 0
fi

# ── Show what's being committed ───────────────────────────────────
echo -e "\n${CYAN}Files being committed:${NC}"
git diff --cached --name-status | while read status file; do
  case $status in
    A) echo -e "  ${GREEN}+ $file${NC}" ;;
    M) echo -e "  ${YELLOW}~ $file${NC}" ;;
    D) echo -e "  ${RED}- $file${NC}" ;;
    *) echo -e "  ? $file" ;;
  esac
done

# ── Commit ────────────────────────────────────────────────────────
echo -e "\n${CYAN}③ Committing: \"${COMMIT_MSG}\"${NC}"
git commit -m "$COMMIT_MSG"

# ── Push ─────────────────────────────────────────────────────────
echo -e "\n${CYAN}④ Pushing to origin/main...${NC}"
git push origin main

# ── Done ─────────────────────────────────────────────────────────
echo -e "\n${GREEN}✅ Done! GitHub Actions will regenerate indexes in ~30 seconds.${NC}"
echo -e "   ${CYAN}https://ubeccommon.github.io/${NC}"
