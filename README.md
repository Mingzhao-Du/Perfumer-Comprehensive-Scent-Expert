# Perfumer — Comprehensive Scent Expert

This project implements a rule-based chatbot that simulates a personalized perfume consultant. The chatbot recommends perfumes based on scent preferences or zodiac signs, responds to user moods using sentiment analysis, and offers brand knowledge, jokes, and conversational support. Based on insights from a university NLP course, this project has been enhanced with clean code principles, modular design, documentation, and testing.

## Features

**Scent-based Recommendations**: Recommends perfumes by matching user input against a curated scent keyword dictionary.
**Zodiac-Based Suggestions**: Offers fragrance styles based on astrological signs.
**Sentiment-Aware Interaction**: Uses VADER sentiment analysis to adjust responses based on the user's emotional tone (happy, upset, angry).
**Perfume Jokes and Brand Trivia**: Shares humor and curated brand/history facts from the perfume domain.
**Fallback Handling**: Provides fallback responses when input is unclear or unrecognized.
**TF-IDF Similarity Matching**: As a fallback, performs cosine similarity matching between user keywords and perfume descriptions when direct matching fails.
**Modular Design**: Codebase is structured across `chatbot_base`, `intent_chatbot`, and `perfume_chatbot` modules for clarity and scalability.
**Unit Testing**: Comprehensive unittest suite verifies core components, ensures new changes don't break existing functionality, and provides documentation of code behavior.

## Dependencies

To run this project, install the following:

```bash
pip install pandas scikit-learn nltk
```

Additionally, ensure that the following NLTK lexicon is downloaded:

```python
import nltk
nltk.download('vader_lexicon')
```

## Setup Instructions

1. Clone the repository and enter the directory:

```bash
git clone https://git.arts.ac.uk/24004238/Data-Science-in-the-Creative-Industries_Project_MingzhaoDu
cd perfumer-chatbot
```

2. Create and activate a virtual environment:

```bash
conda create --name nlp python=3.10
conda activate nlp
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the chatbot:

```bash
python run_chatbot.py
```

## Example Conversation

```
You: Hello  
Bot: Hello, all the best!  
My functions are as follows:  
[1] I can recommend perfumes for you, just need to tell me what [scents] you like or your [zodiac sign].  
[2] I can also share perfume-related jokes, or tell you about some perfume brands or their history.  
[3] Of course, I can also get time; help you relieve your emotions; introduce myself, etc.  

You: I like woody scents like cedar and ebony  
Bot: How about [Mon Nom Est Rouge Eau de Parfum] from [Majda Bekkali]? Its [ Pepper, lemon, elemi, pink pepper, metallic affect, Turkish rose, geranium, cardamom, cumin, cinnamon, ginger, incense, woody balsamic, cedar, sandalwood, amber, vanilla, labdanum, patchouli, tonka bean, musk] will make you feel like you're wearing a little slice of luxury every day. 
Do you have any other favourite flavours? I can continue to recommend them for you.

You: Any recommendations for saffron flavoured perfumes? 
Bot: Here's a thought: why not try [Bois de Borneo Oud] from [Ensar Oud]? The [Agarwoord, Honeysuckle, Borneo chips, Malinau, Creamy, Smoky, Resinous, Oriental ] are fresh and lively, just the kind of scent that might brighten your day.
Do you have any other favourite flavours? I can continue to recommend them for you.

You: I'm really happy today.  
Bot: Since you are in such a good mood today, why don't you try letting me recommend a perfume for you?

You: I'm in a terrible mood tonight.
Bot: Life is full of setbacks, may you get out of it soon. Shall I tell you a joke to cheer you up?

You: Tell me a joke. 
Bot: One perfume bottle asked another, 'Why are you so quiet?' It replied, 'I’m just bottling it up.'

You: I'm an Aquarius, any suggestions?
Bot: Based on your zodiac sign (aquarius), I suggest a perfume with: Unique and unconventional, with aquatic and metallic notes. Of course, you don't have to pay attention to my advice if you have a favourite scent, it's most important to pursue what you like!
Are you satisfied with the answer? You can keep asking me questions.

You: Goodbye
Thank you for using customised perfume Journeys. We wish you a wonderful day in beautiful fragrances. Remember to give me a good review!
```

## Notes

- This project does not include any API keys, credentials, or large binary files. If needed, use environment variables or a `.env` file (not tracked in version control).
- All configuration values (e.g., dataset path, scent categories) are centralized in the `data/` folder or class initializers.
- The scent keyword classification logic is stored in a JSON file and is easy to update or extend.

## License

This project is for **educational and non-commercial use only**.  
© 2025 Mingzhao Du. All rights reserved.  
Please contact the author for permission before redistribution or reuse.