import sys
import os
import pandas as pd

# Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chatbot.perfume_chatbot import PerfumeChatbot


if __name__ == "__main__":
    # Load the perfume dataset
    dataset: pd.DataFrame = pd.read_csv(
        "data\\perfume_dataset.csv",
        encoding='ISO-8859-1',
        on_bad_lines='skip'
    )

    # Initialize the chatbot
    bot: PerfumeChatbot = PerfumeChatbot(name="Perfumer", dataset=dataset)

    # Start the chatbot
    bot.respond()