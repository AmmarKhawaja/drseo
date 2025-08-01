import openai
import secret

openai.api_key = secret.OPENAI_KEY

def generate_text(prompt, temp=1):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp,
    )
    
    text = response['choices'][0]['message']['content']
    return text

def trail_prompt(prompts, temp=1):
    messages = []
    for i, prompt in enumerate(prompts, 1):
        messages.append({"role": "user", "content": f"Prompt {i}: {prompt}"})

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=temp,
    )

    text = response.choices[0].message.content
    return text

def generate_blog_image(prompt, size="1792x1024"):
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size=size
    )
    image_url = response.data[0].url
    return image_url