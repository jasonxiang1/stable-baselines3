# Visualization
Because scripts are run within development containers, it may not be possible to open a visualization window to view the gym environments live. As such, I am using `matplotlib` to render frames with the `rgb_array` rendering mode. 

# Adding debugpy DAP functionality

To setup DAP debugging functionality, add the following `.vs_code/launch.json` file:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "DebugPy",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "localhost",
            "logToFile": true,
            "subProcess": true,
        }
    ]
}
```