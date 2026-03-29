# ClawIntel

AI-Powered Insights, Delivered Daily

## Features

- **Automated Content Generation**: Daily news updates across multiple categories
- **Beautiful Design**: Clean, responsive website
- **Self-Updating**: No manual intervention required
- **Multi-Topic Coverage**: AI, Fintech, Geopolitics, Startups, Sports, Politics

## Setup

### Prerequisites

- Python 3.x
- Git
- GitHub account

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/clawintel.git
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

1. Create a new repository on GitHub
2. Push your code:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/clawintel.git
   git push -u origin main
   ```

3. Enable GitHub Pages in repository settings

## Automation

Set up a cron job to run daily:

```bash
0 8 * * * /usr/bin/python3 /path/to/clawintel/generate_content.py
```

## License

MIT