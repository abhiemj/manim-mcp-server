# Manim MCP Server

![Manim MCP Demo](Demo-manim-mcp.gif)


## Overview

This is an MCP (Model Context Protocol) server that executes Manim animation code and returns the generated video. It allows users to send Manim scripts and receive the rendered animation.

## Features

- Executes Manim Python scripts.
- Saves animation output in a visible media folder.
- Allows users to clean up temporary files after execution.
- Portable and configurable via environment variables.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Manim (Community Version)
- MCP

### Install Manim

```sh
pip install manim
```

### Install MCP

```sh
pip install mcp
```

### Clone the Repository

```sh
git clone https://github.com/abhiemj/manim-mcp-server.git
cd manim-mcp-server
```

## Integration with Claude

To integrate the Manim MCP server with Claude, add the following to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
     "manim-server": {
      "command": "/absolute/path/to/python",
      "args": [
        "/absolute/path/to/manim-mcp-server/src/manim_server.py"
      ],
      "env": {
        "MANIM_EXECUTABLE": "/Users/[Your_username]/anaconda3/envs/manim2/Scripts/manim.exe"
      }
    }
  }
}
```

### Finding Your Python Path

To find your Python executable path, use the following command:

#### Windows (PowerShell):
```sh
(Get-Command python).Source
```

#### Windows (Command Prompt/Terminal):
```sh
where python
```

#### Linux/macOS (Terminal):
```sh
which python
```

This ensures that Claude can communicate with the Manim MCP server to generate animations dynamically.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b add-feature
   ```
3. Make changes and commit:
   ```sh
   git commit -m "Added a new feature"
   ```
4. Push to your fork:
   ```sh
   git push origin add-feature
   ```
5. Open a pull request.

## License

This MCP server is licensed under the MIT License. This means you are free to use, modify, and distribute the software, subject to the terms and conditions of the MIT License. For more details, please see the LICENSE file in the project repository.

## Author

Created by **[abhiemj](https://github.com/abhiemj)**. Contributions welcome! 🚀

### **Listed in Awesome MCP Servers**  
This repository is featured in the [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) repository under the **Animation & Video** category. Check it out along with other great MCP server implementations!


## **Acknowledgments**  
- Thanks to the [Manim Community](https://www.manim.community/) for their amazing animation library.  
- Inspired by the open-source MCP ecosystem.

## Find me at
<a href="https://www.instagram.com/aiburner_official" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="aiburner_official" height="30" width="40" /></a>
@aiburner_official
