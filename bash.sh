docker run --init \
  --name bytebase \
  --publish 8080:8080 \
  --volume ~/.bytebase/data:/var/opt/bytebase \
  bytebase/bytebase:latest
  # Setup a postgres database with user bbdev and database bbdev
export PG_URL=postgresql://bbdev@localhost/bbdev

# Start backend
alias r='go build -ldflags "-w -s" -p=16 -o ./bytebase-build/bytebase ./backend/bin/server/main.go && ./bytebase-build/bytebase --port 8080 --data . --debug'

# Start frontend
alias y="pnpm --dir frontend i && pnpm --dir frontend dev"
╭──────────────────────────────────────────────────╮
│ >_ OpenAI Codex                                  │
│                                                  │
│ model:     gpt-5.6-sol medium/model to change │
│ directory: ~/code                                │
╰──────────────────────────────────────────────────╯

  To get started, describe a task or try one of these commands:

  /init - create an AGENTS.md file with instructions for Codex
  /status - show current session configuration
  /permissions - choose what Codex is allowed to do
  /model - choose what model and reasoning effort to use
  /review - review any changes and find issues
      
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "feature_1": 0.45,
    "feature_2": 1.28
  }'
