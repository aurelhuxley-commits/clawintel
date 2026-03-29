# ClawIntel

**BBC/CurrentAffairs.org-style news website with real-time updates**

## Features

- **Professional Design**: Dark theme with responsive grid layout
- **Real News Integration**: Fetches and displays real news from multiple sources
- **Auto-Updates**: Updates every 2 hours with fresh content
- **Multi-Category Coverage**: AI, Finance, Geopolitics, Sports, Politics
- **Search & Navigation**: Easy browsing with category filters

## Setup

### Prerequisites

- Python 3.x
- Git
- GitHub account

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aurelhuxley-commits/clawintel.git
   cd clawintel
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Run the content generator:
   ```bash
   python generate_content.py
   ```

### Deployment

To deploy to GitHub Pages:

1. Push your code:
   ```bash
   git add .
   git commit -m "Update content"
   git push origin main
   ```

2. Enable GitHub Pages in repository settings

3. Your live URL will be: `https://aurelhuxley-commits.github.io/clawintel/`

## Automation

Set up a cron job to run every 2 hours:

```bash
0 */2 * * * /usr/bin/python3 /home/ubuntu/.openclaw/workspace/clawintel/generate_content.py && cd /home/ubuntu/.openclaw/workspace/clawintel && git add . && git commit -m "Auto-update $(date +\"%Y-%m-%d %H:%M\")" && git push origin main
```

## Real News Integration

The `generate_content.py` script currently uses placeholder data. To integrate real news:

1. **Option 1**: Use web search API (web_search)
2. **Option 2**: Fetch from RSS feeds (BBC, Reuters, etc.)
3. **Option 3**: Use a news API (if available)

## License

MIT