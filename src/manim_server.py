import subprocess
import tempfile
import os
import shutil
from mcp.server.fastmcp import FastMCP
import sys

mcp = FastMCP()

# Get Manim executable path from environment variables or assume it's in the system PATH
# Set executable to "python" to use python.
MANIM_EXECUTABLE = os.getenv("MANIM_EXECUTABLE", "manim")   #MANIM_PATH "/Users/[Your_username]/anaconda3/envs/manim2/Scripts/manim.exe"

TEMP_DIRS = {}
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "media")
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure the media folder exists

@mcp.tool()
def execute_manim_code(manim_code: str) -> str:
    """Execute the Manim code"""
    # tmpdir = tempfile.mkdtemp()  # Creates a temp directory that won't be deleted immediately
    tmpdir = os.path.join(BASE_DIR, "manim_tmp")  
    os.makedirs(tmpdir, exist_ok=True)  # Ensure the temp folder exists
    script_path = os.path.join(tmpdir, "scene.py")
    
    try:
        # Write the Manim script to the temp directory
        with open(script_path, "w") as script_file:
            script_file.write(manim_code)
        
        # Determine which command to run: either custom executable or python -m manim
        if MANIM_EXECUTABLE.lower() == "python":
            command = [sys.executable, "-m", "manim", "-p", script_path]
        else:
            command = [MANIM_EXECUTABLE, "-p", script_path]
        
        # Execute Manim with the determined command
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            cwd=tmpdir
        )

        if result.returncode == 0:
            TEMP_DIRS[tmpdir] = True
            print(f"Check the generated video at: {tmpdir}")

            return "Execution successful. Video generated."
        else:
            return f"Execution failed: {result.stderr}"

    except Exception as e:
        return f"Error during execution: {str(e)}"



@mcp.tool()
def cleanup_manim_temp_dir(directory: str) -> str:
    """Clean up the specified Manim temporary directory after execution."""
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            return f"Cleanup successful for directory: {directory}"
        else:
            return f"Directory not found: {directory}"
    except Exception as e:
        return f"Failed to clean up directory: {directory}. Error: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="stdio")




