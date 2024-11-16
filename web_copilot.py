from oscopilot import FridayWebAgent
from oscopilot import ToolManager
from oscopilot import FridayWebExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run
from selenium_utils.create_driver import create_driver
args = setup_config()
if not args.query:
    args.query = "Goto HKTV mall website in 'https://www.hktvmall.com/hktv/en/', search for 'rice' products, then add any products with quantity 2 to cart."
    # args.query = "Goto HKTV mall website in 'https://www.hktvmall.com/hktv/en/', search for 'rice' and 'egg' products, then add both products to cart."
    # args.query = "Goto HKTV mall website in 'https://www.hktvmall.com/hktv/en/', search for 'xbox', 'ps5' and 'switch' products, then add all products to cart."
    # args.query = "Goto HKTV mall website in 'https://www.hktvmall.com/hktv/en/', search for 'xbox', 'basketball', 'rice' and 'fanta' products, then add all products to cart."
    # args.query = "I want to cook 'lemonade', tell me the recipe, just return the names of ingredients to me only, output the ingredients to ['ingredient 1 ','ingredient 2',...]. If the output is ['ingredient 1','ingredient 2',...], then goto HKTV mall website 'https://www.hktvmall.com/hktv/en/', search for ingredients, and add all products to cart."
task = setup_pre_run(args)

driver = create_driver()

agent = FridayWebAgent(FridayPlanner, FridayRetriever, FridayWebExecutor, ToolManager, config=args)
agent.run(task=task)
