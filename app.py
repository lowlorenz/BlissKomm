from getpass import getpass
from langchain.llms import AlephAlpha
from langchain import PromptTemplate, LLMChain

ALEPH_ALPHA_API_KEY = getpass()


template = """
Task:
Please write an announcement like the following and adapt to the given information, including the additional hints.

Example:
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

Information:
6 pm - paper of the week: pretraining without natural images
7 pm - speaker: Pedro Mercado, talking about Time Series Analysis

Hints:
The speaker is working at AWS AI Labs, which we should highlight
make every section at least 3 sentences long

Output:

Dear BLISSERS,

We are excited to announce our upcoming gathering on Tuesday.
We have some engaging activities planned for you that we think you will enjoy.

At 6 pm, we will be discussing the paper of the week titled "Pretraining Without Natural Images," led by @Jarek in #reading-group-st-23 :brille:. This week's paper explores how pretraining techniques can be used without relying on natural images, which is particularly relevant for fields like computer vision.

Following the discussion, at 7 pm, we are pleased to welcome Pedro Mercado as our guest speaker. Pedro works at AWS AI Labs, where he specializes in Time Series Analysis. During his presentation, he will share his expertise on how to analyze and make predictions based on time-series data, which is crucial for various applications such as finance and climate modeling. We encourage everyone to join in, ask questions, and learn from his experiences.

We hope you will join us for what promises to be an informative and enjoyable evening. See you all there!
Best regards,
Lorenz

#######
Task:
Please write an announcement like the following and adapt to the given information, including the additional hints.

Example:
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

Information:
6 pm - paper of the week: {paper_name}
7 pm - speaker: {speaker_name}, talking about {speaker_topic}

Hints:
{hint}

Output:
"""

prompt = PromptTemplate(template=template, input_variables=["paper_name", "speaker_name", "speaker_topic", "hint"])


llm = AlephAlpha(model="luminous-base", maximum_tokens=300, stop_sequences=["Task"], aleph_alpha_api_key=ALEPH_ALPHA_API_KEY)

llm_chain = LLMChain(prompt=prompt, llm=llm)

paper_name = "LoRA: Low-Rank Adaptation of Large Language Models"
speaker_name = "Aray Karjauv"
speaker_topic = "Self-supervised representation learning using StyleGAN"
hint = "The speaker is from TU Berlin"


#result = llm_chain({"paper_name": paper_name, "speaker_name": speaker_name, "speaker_topic": speaker_topic, "hint": hint})
print(result)