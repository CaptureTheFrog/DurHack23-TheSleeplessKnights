# from AI.LLM import LLM
from utils.lyric_fetcher import get_lyrics

# model = LLM()
# model.set_lyrics("A duck walked up to a lemonade stand And he said to the man runnin' the stand 'Hey! [(bam bam bam)] Got any grapes?' The man said: 'No, we just sell lemonade But it's cold, and it's fresh, and it's all homemade! Can I get you a glass?' The duck said, 'I'll pass.' Then he waddled away - waddle waddle 'Til the very next day 'Bom bom bom bom bom babom' When the duck walked up to the lemonade stand And he said to the man runnin' the stand Hey! (bam bam bam), got any grapes? The man said: 'No, like I said yesterday We just sell lemonade, okey? Why not give it a try?' The duck said. Goodbye Then he waddled away - waddle waddle Then he waddled away - waddle waddle Then he waddled away - waddle waddle 'Til the very next day When the duck walked up to the lemonade stand And he said to the man runnin' the stand 'Hey! (bam bam bam) Got any grapes?' The man said: 'Look, this is gettin' old I mean, lemonade's all we've ever sold Why not give it a go?' The duck said: 'How about - no.' Then he waddled away - waddle waddle Then he waddled away - waddle waddle waddle Then he waddled away - waddle waddle 'Til the very next day When the duck walked up to the lemonade stand And he said to the man runnin' the stand: 'Hey! [(bam bam bam)] Got any grapes?'") # Test prompt to make sure the LLM can understand prompts
# print(model.generate())

print(get_lyrics('Gorillaz', 'Feel Good Inc.'))
