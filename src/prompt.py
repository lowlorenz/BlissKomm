def slack_speaker_prompt(date, paper, speaker, topic, institute):
    return f"""Task:
    Please write an announcement for our slack community, similar to the ones given in the example section. Be sure to adapt to the given information. The announcements should not feel repetitive, so please use synonyms and rephrase sentences where appropriate. Do not try to explain what the paper is about, but rather a general description of the topic that the paper is about. Use emojis if appropriate.

    Example 1:
    Dear BLISSERS,
    We are thrilled to inform you about our upcoming gathering on Tuesday, as usual in room EB302.
    We have some exciting activities planned for you:

    Starting at 6 pm, @Jarek will lead a reading group discussion in #reading-group-st-23 :brille:.
    This is an excellent opportunity to delve into the latest research in your field and keep up with the most recent trends. This week's paper is on Reflexion: an autonomous agent with dynamic memory and self-reflection.

    Following this, at 7 pm, Paul Hagemann will present about normalizing flows :sprechblase:.
    Normalizing flows transform a simple probability distribution into a more complex distribution using invertible transformations, and are used for tasks such as density estimation and generative modeling.

    We hope to see you all there!
    Best regards,
    Lorenz

    Example 2:
    Dear BLISSERS,

    We are excited to announce our upcoming gathering on Tuesday.
    We have some engaging activities planned for you that we think you will enjoy.

    At 6 pm, we will be discussing the paper of the week titled "Pretraining Without Natural Images," led by
    @Jarek in #reading-group-st-23 :brille:. This week's paper explores how pretraining techniques can be used without relying on natural images, which is particularly relevant for fields like computer vision.

    Following the discussion, at 7 pm, we are pleased to welcome Pedro Mercado as our guest speaker. Pedro works at AWS AI Labs, where he specializes in Time Series Analysis. During his presentation, he will share his expertise on how to analyze and make predictions based on time-series data, which is crucial for various applications such as finance and climate modeling. We encourage everyone to join in, ask questions, and learn from his experiences.

    We hope you will join us for what promises to be an informative and enjoyable evening. See you all there!
    Best regards,
    Lorenz

    Example 3:
    Dear BLISSERS,

    We are excited to announce our upcoming meet-up on Tuesday at WiWi Cafe (EB 302)! :rakete:
    Here's what we have planned for you:

    At 6 pm, we will be hosting a reading group organized by @Jarek -->  #reading-group-st-23 :brille:.
    This is a great opportunity to discuss the latest research in your field and stay up-to-date with the latest trends.

    Following this, at 7 pm, we will have a Meet and Greet and Thesis talk :sprechblase:. We have invited PhDs from multiple labs, including WIAS, HHI, and TU ML Group, who are looking for students to join their research projects. This is an excellent opportunity to explore potential thesis topics or find a student position in your area of interest.

    If you're not searching, don't worry! You can still enjoy the interesting discussions and learn about cutting-edge research in the field. :nerd-gesicht:

    We look forward to seeing you there!
    Best,
    Lorenz

    Information:
    6 pm - paper of the week: {paper}
    7 pm - speaker: {speaker} from institute: {institute} will be talking about {topic} 
    Date of event: {date}

    Output:
    
    Dear BLISSERS,"""
    
def twitter_speaker_prompt(date, paper, speaker, topic, institute):
    return f"""Task:
    Please write an announcement for our Twitter community, similar to the ones given in the example section. It must be as short as possible. Be sure to adapt to the given information. The announcements should not feel repetitive, so please use synonyms and rephrase sentences where appropriate. Use a maximum of 50 tokens.

    Example 1:
    📢 Join us for an engaging evening on Tuesday! 🕕 6 pm: Reading group on "Self-Supervised Reinforcement Learning for Recommender Systems." 🕖 7 pm: Kaggle Challenge. Bring a charged laptop if possbile and prep your Kaggle account!

    Example 2:
    Join us on Tuesday for a fun and productive evening! At 6 pm, we'll discuss "Recurrent World Models Facilitate Policy Evaluation" and at 7 pm, showcase your coding projects at our Github Repo Blitz event. Don't miss out on this amazing opportunity!

    Example 3:
    Exciting news! Bliss has a reading group starting at 6 pm followed by a speaker session on Normalizing Flows by Paul Hageman at 7 pm. Join us for an insightful evening of learning and discussion! #readinggroup #speaker #normalizingflows #learning #discussion

    Information:
    6 pm - paper of the week: {paper}
    7 pm - speaker: {speaker} will be talking about {topic} 
    Date of event: {date}

    Output:
    """
    
def linkedin_speaker_prompt(date, paper, speaker, topic, institute):
    return f"""Task:
    Please write an announcement for our LinkedIn community, similar to the ones given in the example section. Be sure to adapt to the given information and keep the structure of the text. The announcements should not feel repetitive, so please use synonyms and rephrase sentences where appropriate. Do not try to explain what the paper is about, but rather a general description of the topic. Use emojis if appropriate.

    Example 1:
    📢 Join us for an exciting evening on Tuesday!

    At 6 pm, be part of our reading group as we discuss the paper "Self-Supervised Reinforcement Learning for Recommender Systems." Explore the latest techniques and share insights with fellow enthusiasts.

    At 7 pm, it's time for the Kaggle Challenge! Showcase your data science skills, collaborate, and connect with like-minded individuals. Please bring your charged laptop and make sure that you have an account on https://kaggle.com/ !

    Don't miss out!

    🗓️ Date: Tuesday, 23.05
    ⏰ Time:
    6:00 pm: Paper of the week - "Self-Supervised Reinforcement Learning for Recommender Systems"
    7:00 pm: Kaggle Challenge
    📍 Location: EB302 Technische Universität Berlin

    Example 2:
    📢 We are excited to announce this week's program for BLISS! We have some exciting events lined up for you, and we can't wait for you to join us.

    Our reading group will start at 6 pm as usual. This week, we will be discussing the paper "Pretraining Without Natural Images." This paper explores an innovative approach to pretraining neural networks without relying on natural images. We look forward to a lively discussion and hearing everyone's perspectives on the topic.

    At 7 pm, we have a special guest speaker, Pedro Mercado, joining us. Pedro is a distinguished data scientist and machine learning expert working at Amazon Web Services (AWS) AI Labs. He will be sharing his insights on Time Series Analysis, drawing on his extensive experience in the field. Pedro has worked on a wide range of time series analysis and forecasting projects and has published several papers on the subject. His talk promises to be both informative and inspiring, and we encourage you to attend.
    
    🗓️ Date: Tuesday, 16.05
    ⏰ Time:
    6:00 pm: Paper of the week: "Pretraining Without Natural Images"
    7:00 pm: Talk "Time Series Analysis" - by Pedro Mercado from AWS AI Labs  
    📍 Location: EB302 Technische Universität Berlin

    #machinelearning #event #aws

    Example 3:
    📢 We are thrilled to announce today's program for BLISS! We have curated two fantastic events for you.

    First on the list, our reading group will convene at 6 pm. We tackle the paper "Reflexion: an autonomous agent with dynamic memory and self-reflection", which deals with the question how LLM's can learn from past mistake and reflect on their experiences.

    At 7 pm, we have a remarkable speaker session with Paul Hagemann. Paul, a PhD candidate at Technische Universität Berlin, is doing fascinating research on normalizing flows and diffusion models. He will be sharing his insights and experiences with us, providing a deeper understanding of this intriguing topic.
    
    🗓️ Date: Tuesday, 16.05
    ⏰ Time:
    6:00 pm: Paper of the week: "Reflexion: an autonomous agent with dynamic memory and self-reflection"
    7:00 pm: Talk "Normalizing Flows" - by Paul Hagemann from TU Berlin
    📍 Location: EB302 Technische Universität Berlin

    Information:
    6 pm - paper of the week: {paper}
    7 pm - speaker: {speaker} from institute: {institute} will be talking about {topic} 
    Date of event: {date}

    Output:
    
    """