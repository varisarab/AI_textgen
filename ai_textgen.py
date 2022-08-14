import gradio as gr

title = "GPT-J-6B"
description = "GPT-J 6B, a transformer model trained using Ben Wang's Mesh Transformer JAX.'6B' is the number of trainable parameters. Add your text, or click one of the examples to load them."
article = "<p style='text-align: center'><a href='https://github.com/kingoflolz/mesh-transformer-jax' target='_blank'>GPT-J-6B: A 6 Billion Parameter Autoregressive Language Model</a></p>"

examples = [
    ['A space ranger encounters a strange silhouette.'],
    ["A day on Saturn is 10 hours and 14 minutes."],
    ["There's no oxygen on Saturn, but roughly 75% hydrogen and 25% helium."]]

gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", inputs=gr.inputs.Textbox(lines=5, label="Input Text"),title=title,description=description,article=article, examples=examples,enable_queue=True).launch()

