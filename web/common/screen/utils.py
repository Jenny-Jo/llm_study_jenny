from dotenv import load_dotenv
from common.screen.history import init_history
from common.screen.display import print_history_message
from common.screen.input import chosen_llms, chosen_provider

def init_page():
    load_dotenv()
    init_history()
    
def init_display():
    # 이력 데이터를 프린트트
    print_history_message()
    selected_provider = chosen_provider()
    chosen_llm = chosen_llms(selected_provider)
    return selected_provider, chosen_llm