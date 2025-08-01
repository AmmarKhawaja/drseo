import gpt
import prompts
from datetime import datetime
import requests
import concurrent.futures
from PIL import Image
from io import BytesIO

def create_blog(name='text.html', topic='', reference_path='1-boost-your-dental-seo-today-3-quick-fixes'):
    output = ''
    with open(f'./blogs/{reference_path}.html', 'r', encoding='utf-8') as f:
        output = gpt.trail_prompt(prompts=[prompts.format_blog_prompt_part1(f.read()),
                                        prompts.format_blog_prompt_part2(text=gpt.generate_text(
                                            prompt=prompts.write_blog_prompt(topic=topic))),
                                        prompts.format_blog_prompt_part3()])
    
    with open(f'./blogs/{name}-{datetime.now().strftime("%Y%m%d-%H%M%S")}.html', 'w', encoding='utf-8') as f:
        f.write(output)

def improve_existing_blog(blog_name):
    output = ''
    with open(f'./blogs/{blog_name}.html', 'r', encoding='utf-8') as f:
        output = gpt.trail_prompt(prompts=[prompts.optimize_blog_part1(text=f.read()), prompts.optimize_blog_part2()])
    
    with open(f'./blogs/{blog_name}-{datetime.now().strftime("%Y%m%d-%H%M%S")}.html', 'w', encoding='utf-8') as o:
        o.write(output)

def generate_blog_images(context):
    def generate_and_save(i):
        img_url = gpt.generate_blog_image(prompt=prompts.generate_blog_image(text=context))
        image = Image.open(BytesIO(requests.get(img_url).content))
        image.save(f"img/{context.replace(' ', '-')}-{i}.webp", format='WEBP')

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(generate_and_save, range(5))

#improve_existing_blog(blog_name='5-seo-for-cosmetic-dentists-in-2025')
# create_blog(name='6-cosmetic-dentist-digital-marketing-seo',
#             topic='Cosmetic Dentist Digital Marketing SEO',
#             reference_path='2-seo-for-pediatric-dentists-full-optimization-guide')
generate_blog_images('a cosmetic dentist taking care of a patient')