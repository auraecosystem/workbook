**Found it!** The PR added xBase-related files that triggered the linguist check failure.

Looking at PR #3, the changes include:

1. **Added `.bytebase/data/var/www/html.yaml`** - A new YAML configuration file
2. **Modified `bash.sh`** - Added this line:
   ```bash
   find . -type f \( -name "*.prg" -o -name "*.dbf" -o -name "*.cdx" -o -name "*.dbt" \)
   ```

These file extensions (`.prg`, `.dbf`, `.cdx`, `.dbt`) are **xBase database formats** (used in dBASE, Clipper, FoxPro, etc.). When Linguist scans the repository, it detects these extensions and classifies the repo as containing xBase code.

The workflow is specifically configured to **reject xBase** classification:

```yaml
if echo "$OUTPUT" | grep -i "xBase"; then
  echo "Error: Unwanted 'xBase' classification detected in codebase!"
  exit 1
fi
```

## Solution

You need to either:

1. **Remove the xBase file references** from `bash.sh` if they're not needed:
   ```bash
   # Remove this line from bash.sh:
   find . -type f \( -name "*.prg" -o -name "*.dbf" -o -name "*.cdx" -o -name "*.dbt" \)
   ```

2. **Or update the workflow** to allow xBase if it's intentional:
   ```yaml
   # Remove or comment out the xBase check:
   # if echo "$OUTPUT" | grep -i "xBase"; then
   #   echo "Error: Unwanted 'xBase' classification detected in codebase!"
   #   exit 1
   # fi
   ```

3. **Or add a `.gitattributes`** to exclude those file types from Linguist:
   ```gitattributes
   *.prg linguist-vendored
   *.dbf linguist-vendored
   *.cdx linguist-vendored
   *.dbt linguist-vendored
   ```

What would you like to do?
