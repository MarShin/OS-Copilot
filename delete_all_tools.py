import json
from oscopilot.tool_repository.manager.tool_manager import delete_tool, ToolManager

def delete_all_tools(json_file):
    # Read JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)

    toolManager = ToolManager("oscopilot/tool_repository/generated_tools")
    # Run the function for each key in the JSON
    for key, value in data.items():
        delete_tool(toolManager, key)

if __name__ == "__main__":
    json_file = 'oscopilot/tool_repository/generated_tools/generated_tools.json'
    delete_all_tools(json_file)
