python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name goto_url
python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name search_products
python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name scrap_products
python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name pick_one_product
python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name add_item_to_cart
python oscopilot/tool_repository/manager/tool_manager.py --delete --tool_name check_out_page

python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name goto_url --tool_path agent_simulation/tools_to_add/goto_url.py
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name search_products --tool_path agent_simulation/tools_to_add/search_products.py
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name scrap_products --tool_path agent_simulation/tools_to_add/scrap_products.py
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name pick_one_product --tool_path agent_simulation/tools_to_add/pick_one_product.py
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name add_item_to_cart --tool_path agent_simulation/tools_to_add/add_item_to_cart.py
python oscopilot/tool_repository/manager/tool_manager.py --add --tool_name check_out_page --tool_path agent_simulation/tools_to_add/check_out_page.py