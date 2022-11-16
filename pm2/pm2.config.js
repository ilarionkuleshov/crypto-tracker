const path = require("path");

if (process.platform === "win32") python_script = path.join("..", "src", ".venv", "Scripts", "python.exe");
else python_script = path.join("..", "src", ".venv", "bin", "python");

module.exports = {
    apps: [
        {
            name: "crypto_tracker",
            script: python_script,
            args: "run.py",
            cwd: path.join("..", "src"),
            log_file: path.join("..", "logs", "crypto_tracker.log"),
            cron_restart: "*/30 * * * *",
            autorestart: false
        }
    ]
}
