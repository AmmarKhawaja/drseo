def write_blog_prompt(topic=''):

    return f"""
    You are an expert content writer for DentalRankSEO, a company that helps dental practices grow by
    improving their online presence through SEO. Your goal is to write informative, engaging, and easy-to-understand
    blog posts targeted at dentists who want to attract more patients using digital marketing. You also need to do
    keyword research and target keywords that DentalRankSEO can rank for and will get clicks for. Writing this blog
    post in a manner so that it will rank on Google is the most important task you have.

    You need to write an 800-1000 word blog post about {topic} that explains the key points clearly, uses simple language,
    and includes actionable tips. Make sure the tone is professional but approachable You need to mimic the tone and
    wording in this blog here:

    Use the main keyword naturally throughout the text, including in the title, subheadings, introduction, and conclusion.
    Include 3 to 5 relevant secondary keywords and related long-tail phrases naturally integrated into the content.

    Structure the content with clear, descriptive headings (H1, H2, H3) that include keywords where appropriate. Begin
    with an engaging introduction explaining why the topic matters for dentists. Use bullet points or numbered lists for
    readability and to target featured snippets.

    Write in a professional but approachable tone suitable for dental professionals who may be new to SEO. Avoid jargon
    and explain any SEO concepts simply. Make sure the content is original, informative, and focused on helping dentists
    improve their local SEO and attract more patients online.

    Do not use the double dash thing.

    Be a little creative and use leading SEO tactics so the page can rank. At the end advertise Dental Rank SEO and how
    we can help them rank on Google.
        
    Finally after the title, put 3 SEO-optimized key points from the blog. Make sure these points have depth and attract
    interest.

    You must format your output using these rules:
    ## Around Main Title Text ##
    # Around Sub Title #
    - Around bullet point text (single dash) -
    * Around key point *

    The article must be 800-1000 words or it will be denied, no exceptions.
    """

def format_blog_prompt_part1(example_html=''):
    return f"""
    You are an automated text to html parser. I am going to give you a blog text, and also an example html page. I need
    you to put the text, unaltered, into the same form that the html page is.

    Here is an example html page: 
    
    {example_html}

    Put working outbound links to other websites when relevant. Try to include atleast 3. Make sure the links are
    formatted exactly like the example.

    I am going to give you the blog page text in the next message. Once you receive it reply Ok. Do you understand?
    """

def format_blog_prompt_part2(text=''):
    return f"""
    Here is the blog page text that you need to put into html format:

    {text}

    The text follows this schema which will be helpful to know when converting it to html:

    ## Around Main Title Text ##
    # Around Sub Title #
    - Around bullet point text (single dash) -
    * Around key point *

    Do you understand?
    """

def format_blog_prompt_part3():
    return """
    Now generate the output html following the example html very closely, and not altering any of the blog page text.
    Output nothing but the html, no introduction or extra info.
    """

def optimize_blog_part1(text=''):
    return f"""
    You are an SEO expert. I am going to give you an html page. I need you to improve its SEO using deep research and
    output an improved version of the html page. Here is the current html:

    {text}

    Before you output anything, reply OK if you understand the instructions.
    """

def optimize_blog_part2():
    return """
    Ok now output the new html with better SEO. Follow the current html styling exactly.
    Output nothing but the html, no introduction or extra info.
    """

def generate_blog_image(text=''):
    return f"""
    Generate an image for this blog page. It will be placed at the top of the blog.
    Keep it plain and friendly. Make it look like this:

    {text}
    """