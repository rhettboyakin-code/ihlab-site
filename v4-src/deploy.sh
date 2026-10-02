#!/usr/bin/env bash
# Build v4/ and publish it as a noindex Vercel preview (does NOT touch GitHub Pages / main).
set -euo pipefail
cd "$(dirname "$0")/.."
SCOPE="${VERCEL_SCOPE:-beehive-branch}"
python3 v4-src/build.py
[[ -s v4-src/.deploy-slug ]] || echo "ihlab-v4-preview-$(python3 -c 'import secrets,string;a=string.ascii_lowercase+string.digits;print("".join(secrets.choice(a) for _ in range(6)))')" > v4-src/.deploy-slug
PROJECT="$(cat v4-src/.deploy-slug)"
cd v4
if [[ ! -f .vercel/project.json ]]; then
  vercel project add "$PROJECT" --scope "$SCOPE" >/dev/null 2>&1 || true
  vercel link --yes --project "$PROJECT" --scope "$SCOPE"
fi
vercel deploy --prod --yes --scope "$SCOPE" 2>&1 | tee ../v4-src/.last-deploy.log
echo "Preview URL: https://$PROJECT.vercel.app"
