from oscopilot import FridayAgent
from oscopilot import ToolManager
from oscopilot import FridayExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run

args = setup_config()
# args.query = "Create a new folder named 'test_friday' using bash command and confirm the existence of the created directory. please execute your plans."
# args.query = "create a python script that prints the current working directory"
# args.query = "create a text file named 'bye.txt' in the working directory."
# args.query = "Create a new folder named 'found' inside the working directory. Copy any text file located in the working_dir/document directory that contains the word 'agent' to working_dir/found directory."
args.query = "Go to iherb.com and get the first 5 whey protein products and their prices. Please use selenium to fetch the website. Selenium and webdriver is already installed. avoid printing the html content directly or try to clean up before printing, otherwise the output will be very large and exceed the sequence length limit of LLMs."


if not args.query:
    args.query = "Copy any text file located in the working_dir/document directory that contains the word 'agent' to a new folder named 'found' inside the working directory. Create the new foler if it does not exist."
task = setup_pre_run(args)
agent = FridayAgent(FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args)
agent.run(task=task)
