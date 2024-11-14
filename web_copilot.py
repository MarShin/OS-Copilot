from oscopilot import FridayWebAgent
from oscopilot import ToolManager
from oscopilot import FridayWebExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run
from selenium_utils.create_driver import create_driver
args = setup_config()
if not args.query:
    args.query = '''Goto HKTV mall website in 'https://www.hktvmall.com/hktv/en/', 
    search for 'tea' products, then add any one product to cart '''
task = setup_pre_run(args)

driver = create_driver()

agent = FridayWebAgent(FridayPlanner, FridayRetriever, FridayWebExecutor, ToolManager, config=args)
agent.run(task=task)

#Run below command to keep the log
# rm log/web_copilot.log; rm log/web_copilot_console.log; python web_copilot.py --logging_filename web_copilot.log &>> log/web_copilot_console.log
