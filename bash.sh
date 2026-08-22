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
