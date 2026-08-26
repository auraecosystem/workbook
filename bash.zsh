cd github.com/auraecosystem/workbook

# Run Linguist breakdown
docker run --rm -v $(pwd):$(pwd) -w $(pwd) ghcr.io/github-linguist/linguist:latest github-linguist --breakdown
# Install the official GitHub Linguist gem
gem install github-linguist

# Run the breakdown command in your repository
cd /auraecosystem/workbook/
github-linguist --breakdown
